#!/usr/bin/env python
"""
Test Circuit and Program to test rfdetector.py
"""

import pylab as pl
from eispice import *
from numpy import *
from rfdetector import Detector

tstop = 100e-9
uavg = []
dbms = arange(-30.0,10,2.5)
#pl.ion()
for dbm in dbms:
    print dbm
    emk = 2 * sqrt( 10**((dbm-30)/10) * 50.0)
    print emk
    cir = Circuit()
    cir.detector = Detector("rf","video")
    cir.generator = V("emk",0,0,Sin(0,emk,500e6))
    cir.source_resistance = R("emk","rf",50)
    cir.load_resistance = R("video",0,1e3)
    cir.tran("0.005n",tstop)
    
    videovoltage = cir.voltage("video")[:,1]
    times = cir.voltage("video")[:,0]
    lv = len(videovoltage)
    #pl.semilogy()
    pl.plot(times,videovoltage,".")
    #pl.show()
    uavg.append(average(videovoltage[lv/2:]))
    del (cir)


pl.show()
raw_input("press key")
uavg = array(uavg)   
pl.clf()
pl.semilogy()
pl.plot(dbms, uavg)
pl.show()
raw_input()
