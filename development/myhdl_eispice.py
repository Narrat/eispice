#!/usr/bin/env python
"""
Combined MyHDL and eispice Simulation
"""

debug=1
 
import threading
from myhdl import *
import eispice
 
triggerfrequency = 10e6
myhdl_timestep = 0.2e-9
 
simulationlen = 100e-9
 
eispice_time = 0
myhdl_time = 0
catchup = threading.Event()
continue_sim = threading.Event()
eispice_finished =0
 
devicecnt=0
catchedupcnt=0
 
class EispicePort(eispice.PyB):
 
 
    def __init__(self, pNode, nNode,function,outputtype):
        global devicecnt
        eispice.PyB.__init__(self, pNode, nNode, outputtype,self.v(pNode), self.v(nNode), eispice.Time)
        self.output=0
        devicecnt+=1
        self.myhdl=function
 
    def model(self, vP, vN, time):
        global catchup, eispice_time, devicecnt, catchedupcnt
        if debug: print eispice_time,"Eispice Interface callback"
        eispice_time = time
 
        if myhdl_time==0:
            if debug: print "eispice: waiting for myhdl start"
            return self.output
 
        if (eispice_time <  myhdl_time) and (myhdl_time - eispice_time)<myhdl_timestep:
            if debug: print "eispice: not yet reached myhdl time"
            catchup.clear()
            return self.output
 
        if catchedupcnt:
            catchedupcnt-=1
        if not catchedupcnt:
            continue_sim.clear()
            catchup.set()
            catchedupcnt=devicecnt
            if debug: print "eispice: catched up"
        self.output=self.myhdl(vP,vN,time)
        return self.output
 
    def myhdl(vP,vN,time):
        return 0
 
 
def triggerout(vP,vN,time):
        if debug: print "triggerout",clk.val," time=",time
        output = float(clk.val)
        adc.next = 2**15+int(vP-vN)
        return output
 
def detectorout(vP,vN,time):
        if debug: print "detectorout",detector.val,"time=",time
        return 100*float(detector.val)
 
class EispiceThread(threading.Thread):
 
    def __init__(self):
        threading.Thread.__init__(self)
 
        self.setDaemon(0)
        self.start()
        
    def run(self):
        global eispice_finished
        cir  = eispice.Circuit("Mixed Mode Test")
        ### here we do the analog circuit description ###
        cir.L = eispice.L(1,0,27e-9)
        cir.R = eispice.R(1,0,820)
        cir.C = eispice.C(1,0,47e-12)
        cir.Rout = eispice.R(2,0,100)
 
        ### now we define our two MyHDL ports ###
        cir.TriggerOut = EispicePort(1,0,triggerout,eispice.Current)
        cir.DetectorOut = EispicePort(2,0,detectorout,eispice.Voltage)
 
        ### starting the simulation ###
        cir.tran(myhdl_timestep,simulationlen)
 
        ### plotting the results ###
        eispice.plot(cir)
        print "Eispice Simulation finished"
        catchup.set()
        eispice_finished=1
           
def mixedmode():
    global clk,adc,detector
    clk=Signal(bool(0))
    detector = Signal(bool(0))
    adc = Signal(intbv(0)[16:])
 
    @instance
    def clkgen():
        clk.next=0
        yield delay(1)
        while (1):
            clk.next = not clk
            yield delay(int(1.0/myhdl_timestep/triggerfrequency/2))
 
    @always(adc)
    def detection():
        if adc > 2**15-10:
            detector.next=1
        else:
            detector.next=0
 
    @always(delay(1))
    def timer():
        global myhdl_time
        myhdl_time+=myhdl_timestep
        if debug: print myhdl_time,"myhdl:Waiting for eispice to catch up"
        if not eispice_finished:
            catchup.wait()
            catchup.clear()
            continue_sim.set()
        if debug: print "myhdl: got catchup notify"
 
    ### Starting the eispice thread ###
    eispice_thread = EispiceThread()
    Simulation(instances()).run(int(simulationlen/myhdl_timestep))
    print "Simulation finished"
 
mixedmode()