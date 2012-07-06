import scipy
import scipy.special
import pylab

v1 = 0
v2 = 3.3
td = 2
tr = 1
tf = 0.5
pw = 5
per = 12

t3r = (tr/0.672)*0.281*2
t3f = (tf/0.672)*0.281*2

T = scipy.arange(0,20,0.01)

V = scipy.zeros(len(T))

for i in range(0,len(T)):
	t = T[i] % per
	V[i] = v1
	V[i] += 0.5 * (v2-v1) * (1 + scipy.special.erf(((t-(t3r/0.281)*0.672-td)/t3r)))
	V[i] += 0.5 * (v1-v2) * (1 + scipy.special.erf(((t-(t3f/0.281)*0.672-td-pw)/t3f)))

for i in range(0,len(T)-1):
	if V[i] < 0.2 and V[i+1] > 0.2:
		print T[i]
	if V[i] < 0.8 and V[i+1] > 0.8:
		print T[i]

pylab.plot(T,V)
pylab.show()
