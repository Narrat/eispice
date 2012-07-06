from eispice import *
from numpy import matrix

R0 = [[0.861113, 0], [0, 0.861113]]
L0 = [[231.832e-9, 38.1483e-9],[38.1483e-9, 231.819e-9]]
G0 = [[0,0],[0,0]]
C0 = [[156.163e-12, -8.60102e-12],[-8.60102e-12, 156.193e-12]]
Rs = [[0.368757e-3, 0],[0, 0.368757e-3]]
Gd = [[0,0],[0,0]]

cct = Circuit("TlineW Test")

cct.Vs1 = device.V('vs1', GND, 1,
	waveform.Pulse(1, 0, '5n', '1n', '1n', '5n', '10n'))
cct.Vs2 = device.V('vs2', GND, 1,
	waveform.Pulse(1, 0, '5n', '1n', '1n', '5n', '10n'))

cct.Rs1 = device.R('vs1', 'vi1', 1)
cct.Rs2 = device.R('vs2', 'vi2', 1)

cct.Tg = device.W(('vi1','vi2'), GND, ('vo1','vo2'), GND,
	0.0265, R0, L0, C0, G0, Rs, Gd, M=9)

cct.Rl1 = device.R('vo1', GND, '10k')
cct.Rl2 = device.R('vo2', GND, '10k')

#~ cct.Vs1 = device.V('vs1', GND, 1)
#~ cct.Vs2 = device.V('vs2', GND, 1)
#~ cct.Tg = device.W(('vs1','vs2'), GND, ('vo1','vo2'), GND,
		#~ 0.0265, R0, L0, C0, G0, Rs, Gd, M=9)
#~ cct.Rl1 = device.R('vo1', GND, 0.022819)
#~ cct.Rl2 = device.R('vo2', GND, 0.022819)

cct.tran('0.5n', '2n')
eispice.plot(cct)

print cct.v['vo1'](0)
print cct.v['vo2'](0)
