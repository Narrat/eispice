#!/usr/bin/env python
"""
Test Circuit and Program to test rfdetector.py
"""

from eispice import *

cir = Circuit()
cir.Crf = C("rf",1,"1000p")
cir.Vmeas = V(1,'1x')
cir.D =  D(0,'1x',IS = 5e-6,RS = 20,N = 1.05,TT = 1e-11,CJO = 0.14e-12,
		M = 0.4,BV = 2,VJ = 0.34,FC=0.5)
cir.L = L(1,"video","100n")
cir.Cv = C("video",0,"1000p")
cir.generator = V("emk",0,0,Sin(0,1,500e6))
cir.source_resistance = R("emk","rf",50)
cir.load_resistance = R("video",0,1e3)
cir.tran("0.005n",1.2525e-9)
#~ plot_current(cir, 'Vmeas')

for (t, i) in cir.current('Vmeas'):
	print "%e %e" % (t, i)
