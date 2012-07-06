#!/usr/bin/env python
"""
Collection or RF Schottky Diodes

Does not include Ls!
"""

from eispice import *

class AbsoluteMaximumRatings:
    IF = 50e-3
    PD = 75e-3


class SMS7621(D):
    """
    Forward current at 270 mV
    >>> c = Circuit()
    >>> c.D = SMS7621(1,0)
    >>> c.V = V(1,0,270e-3)
    >>> c.op()
    >>> print "%3.3e"%round(-c.current("V")[0][1],8)
    6.294e-04

    >>> del(c)

    Reverse current at 2V
    >>> c = Circuit()
    >>> c.D = SMS7621(1,0)
    >>> c.V = V(1,0,-2)
    >>> c.op()
    >>> print "%3.3e"%round(-c.current("V")[0][1],8)
    4.900e-07
    """
    url = "http://www.skyworksinc.com/products_detailpop2.asp?pid=5494"

    amr = AbsoluteMaximumRatings()

    def __init__(self,pNode,nNode):
        D.__init__(self,pNode,nNode,
                IS = 4e-8,
                RS = 12,
                N = 1.05,
                TT = 1e-11,
                CJO = 0.1e-12,
                M = 0.35,
                #EG = 0.69,
                #XTI = 2,
                #FC = 0.5,
                BV = 3,
                #IBV = 1e-5,
                VJ = 0.51,
                )


class SMS1546(D):
    """
    Forward current at 270 mV
    >>> c = Circuit()
    >>> c.D = SMS1546(1,0)
    >>> c.V = V(1,0,270e-3)
    >>> c.op()
    >>> print "%3.3e"%round(-c.current("V")[0][1],8)
    3.862e-03

    >>> del(c)

    Reverse current at 2V 
    >>> c = Circuit()
    >>> c.D = SMS1546(1,0)
    >>> c.V = V(1,0,-2)
    >>> c.op()
    >>> print "%3.3e"%round(-c.current("V")[0][1],8)
    3.670e-06
    """
    url = "http://www.skyworksinc.com/products_detailpop2.asp?pid=5494"

    amr = AbsoluteMaximumRatings()

    def __init__(self,pNode,nNode):
        D.__init__(self,pNode,nNode,
                IS = 3e-7,
                RS = 4,
                N = 1.04,
                TT = 1e-11,
                CJO = 0.38e-12,
                M = 0.36,
                #EG = 0.69,
                #XTI = 2,
                #FC = 0.5,
                BV = 3,
                #IBV = 1e-5,
                VJ = 0.51,
                )


class SMS7630(D):
    """
    Forward current at 270 mV 
    >>> c = Circuit()
    >>> c.D = SMS7630(1,0)
    >>> c.V = V(1,0,270e-3)
    >>> c.op()
    >>> print "%3.3e"%round(-c.current("V")[0][1],8)
    4.322e-03

    >>> del(c)

    Reverse current at 2V 
    >>> c = Circuit()
    >>> c.D = SMS7630(1,0)
    >>> c.V = V(1,0,-2)
    >>> c.op()
    >>> print "%3.3e"%round(-c.current("V")[0][1],8)
    1.840e-04

    Note: RS in http://www.skyworksinc.com/products_display_item.asp?did=2064 is 30 Ohm
    instead of 20 Ohm in the datasheet.
    """
    url = "http://www.skyworksinc.com/products_detailpop2.asp?pid=5494"

    amr = AbsoluteMaximumRatings()

    def __init__(self,pNode,nNode):
        D.__init__(self,pNode,nNode,
                IS = 5e-6,
                RS = 20,
                N = 1.05,
                TT = 1e-11,
                CJO = 0.14e-12,
                M = 0.4,
                #EG = 0.69,
                #XTI = 2,
                #FC = 0.5,
                BV = 2,
                #IBV = 1e-5,
                VJ = 0.34,
                )

        
class SMS3922(D):
    """
    Forward current at 270 mV 
    >>> c = Circuit()
    >>> c.D = SMS3922(1,0)
    >>> c.V = V(1,0,270e-3)
    >>> c.op()
    >>> print "%3.3e"%round(-c.current("V")[0][1],8)
    4.139e-04

    >>> del(c)

    Reverse current at 2V 
    >>> c = Circuit()
    >>> c.D = SMS3922(1,0)
    >>> c.V = V(1,0,-2)
    >>> c.op()
    >>> print "%3.3e"%round(-c.current("V")[0][1],8)
    -6.000e-08
    """

    url = "http://www.skyworksinc.com/products_detailpop2.asp?pid=5489"

    amr = AbsoluteMaximumRatings()

    def __init__(self,pNode,nNode):
        D.__init__(self,pNode,nNode,
                IS = 3e-8,
                RS = 9,
                N = 1.08,
                TT = 8e-11,
                CJO = 0.7e-12,
                M = 0.26,
                #EG = 0.69,
                #XTI = 2,
                #FC = 0.5,
                BV = 20,
                #IBV = 1e-5,
                VJ = 0.595,
                )

class SMS3923(D):
    """
    Forward current at 270 mV 
    >>> c = Circuit()
    >>> c.D = SMS3923(1,0)
    >>> c.V = V(1,0,270e-3)
    >>> c.op()
    >>> print "%3.3e"%round(-c.current("V")[0][1],8)
    9.978e-05

    >>> del(c)

    Reverse current at 2V 
    >>> c = Circuit()
    >>> c.D = SMS3923(1,0)
    >>> c.V = V(1,0,-2)
    >>> c.op()
    >>> print "%3.3e"%round(-c.current("V")[0][1],12)
    -1.000e-08
    """

    url = "http://www.skyworksinc.com/products_detailpop2.asp?pid=5489"

    amr = AbsoluteMaximumRatings()

    def __init__(self,pNode,nNode):
        D.__init__(self,pNode,nNode,
                IS = 5e-9,
                RS = 11,
                N = 1.05,
                TT = 8e-11,
                CJO = 0.9e-12,
                M = 0.24,
                #EG = 0.69,
                #XTI = 2,
                #FC = 0.5,
                BV = 46,
                #IBV = 1e-5,
                VJ = 0.64,
                )


class SMS3924(D):
    """
    Forward current at 270 mV 
    >>> c = Circuit()
    >>> c.D = SMS3924(1,0)
    >>> c.V = V(1,0,270e-3)
    >>> c.op()
    >>> print "%3.3e"%round(-c.current("V")[0][1],8)
    3.200e-07

    >>> del(c)

    Reverse current at 2V 
    >>> c = Circuit()
    >>> c.D = SMS3924(1,0)
    >>> c.V = V(1,0,-2)
    >>> c.op()
    >>> print "%3.3e"%round(-c.current("V")[0][1],12)
    -4.000e-11
    """

    url = "http://www.skyworksinc.com/products_detailpop2.asp?pid=5489"

    amr = AbsoluteMaximumRatings()

    def __init__(self,pNode,nNode):
        D.__init__(self,pNode,nNode,
                IS = 2e-11,
                RS = 11,
                N = 1.08,
                TT = 8e-11,
                CJO = 1.5e-12,
                M = 0.4,
                #EG = 0.69,
                #XTI = 2,
                #FC = 0.5,
                BV = 100,
                #IBV = 1e-5,
                VJ = 0.84,
                )

def _test():
    import doctest
    # doctest.testmod(verbose=True)   
    doctest.testmod()        # use -v at the command line if you want to see something

if __name__=="__main__":        

    _test()

