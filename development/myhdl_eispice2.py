#!/usr/bin/env python
"""
Combined MyHDL and eispice Simulation
"""
 
from myhdl import *
import eispice
 
triggerfrequency = 10e6
myhdl_timestep = 0.2e-9 
eispice_step = 0.05e-9
 
simulationlen = 100e-9
 
myhdl_time = 0
 
class EispicePort(eispice.PyB):
 
 
    def __init__(self, pNode, nNode,function,outputtype):
        global devicecnt
        eispice.PyB.__init__(self, pNode, nNode, outputtype,self.v(pNode), self.v(nNode), eispice.Time)
        self.output=0
        self.myhdl=function
        
    def model(self, vP, vN, time):
        self.output=self.myhdl(vP,vN,time)
        return self.output            
 
    def myhdl(vP,vN):
        return 0 
 
 
def triggerout(vP,vN, time):        
        output = float(clk.val)
        adc.next = 2**15+int(vP-vN)
        return output
 
def detectorout(vP,vN, time):
        return 100*float(detector.val) 
 
def circuit():
        cir  = eispice.Circuit("Mixed Mode Test")
        #cir.Vx = eispice.V(1,0,4)
        cir.L = eispice.L(1,0,27e-9)
        cir.R = eispice.R(1,0,820)
        cir.C = eispice.C(1,0,47e-12) 
        cir.Rout = eispice.R(2,0,100)
        cir.TriggerOut = EispicePort(1,0,triggerout,eispice.Current)
        cir.DetectorOut = EispicePort(2,0,detectorout,eispice.Voltage)
        return cir
 
 
 
            
def mixedmode():
    global clk,adc,detector
    clk=Signal(bool(0))
    detector = Signal(bool(0))
    adc = Signal(intbv(0)[16:])
    cir = circuit()
 
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
 
    @instance
    def timer():
        global myhdl_time
        while (myhdl_time < simulationlen):
            myhdl_time+=myhdl_timestep
            cir.tran(eispice_step,myhdl_time,restart=False)
            yield delay(1)
 
    cir.tran(eispice_step, myhdl_timestep,restart=True)
    Simulation(instances()).run(int(simulationlen/myhdl_timestep))
    eispice.plot(cir)
    
    
 
mixedmode()