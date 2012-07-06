import eispice

cct = eispice.Circuit("Non-Linear Capacitor Test")

wave = eispice.Pulse('1n', '10n', '10n', '5n', '3n', '5n', '25n')
cct.Vc = eispice.V(3, 0, '1n', wave)

cct.Vx = eispice.V(1, 0, 4, 
	eispice.Pulse(4, 8, '10n', '2n', '3n', '5n', '20n'))
cct.Cx = eispice.BC(1, 0, 'v(3)*10')

cct.tran('0.5n', '100n')

eispice.plot(cct)

print "%s... Pass" % cct.title
