#!/usr/bin/env python
"""
RF detector from the skyworks application note:
http://www.skyworksinc.com/products_display_item.asp?did=2064
"""

from eispice import *
from schottkydiodes import SMS7630

class Detector(Subckt):

    def __init__(self,rf_in,video_out):

        self.Crf = C(rf_in,self.node(1),"1000p")
        self.D = SMS7630(0,self.node(1))
        self.L = L(self.node(1),video_out,"100n")
        self.Cv = C(video_out,0,"1000p")
    

if __name__=="__main__":

    cir = Circuit()
    cir.detector = Detector("rf","video")
    cir.generator = V("emk",0,0,Sin(0,1,100e6))
    cir.source_resistance = R("emk","rf",50)
    cir.load_resistance = R("video",0,50)

    cir.tran("1n","100ns")
    plot(cir)

    

