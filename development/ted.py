import eispice

cct1 = eispice.Circuit("Ted's Circuit 1")
cct1.V18 = eispice.V(eispice.GND, 1, 18)
cct1.V7 = eispice.V(2, eispice.GND, 7)
cct1.I5m = eispice.I(1, 2, 0.005)

cct1.op()

print '-- Circuit 1 --'
print 'V18 Current: %gA' % cct1.i['V18'](0)
print 'V7 Current: %gA' % cct1.i['V7'](0)
print 'I5m Voltage: %gV' % (cct1.v[1](0) - cct1.v[2](0))

cct2 = eispice.Circuit("Ted's Circuit 2")
cct2.In5 = eispice.I(eispice.GND, 1, (20-25-5))
cct2.V60 = eispice.V(2, 1, 60)
cct2.V100 = eispice.V(2, eispice.GND, 100)

cct2.op()

print '-- Circuit 2 --'
print 'V60 Current: %gA' % cct2.i['V60'](0)
print 'V100 Current: %gA' % cct2.i['V100'](0)
