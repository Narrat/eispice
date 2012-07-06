#!python ./eide.py

# This is the test code I used to write the tline_w model. It will probably
# make more sense if you read it along with the c code, which has more
# comments and refrences and useful things like that.

import scipy
import scipy.linalg
from numpy import matrix
#~ import pylab

def tester():

	# This was used to help develop / test the W-Element Algorithums

	R0 = scipy.array([[0.861113, 0], [0, 0.861113]], dtype=scipy.complex128)
	L0 = scipy.array([[231.832e-9, 38.1483e-9],[38.1483e-9, 231.819e-9]], dtype=scipy.complex128)
	G0 = scipy.array([[0,0],[0,0]], dtype=scipy.complex128)
	C0 = scipy.array([[156.163e-12, -8.60102e-12],[-8.60102e-12, 156.193e-12]], dtype=scipy.complex128)
	Rs = scipy.array([[0.368757e-3, 0],[0, 0.368757e-3]], dtype=scipy.complex128)
	Gd = scipy.array([[0,0],[0,0]], dtype=scipy.complex128)

	length = 0.0265

	M = 9	# Order of the aproximation
	K = M*2 + 1	# Number of samples required
	N = 2		# Number of pins

	fK = 1e9 # Maximum frequency
	fgd = 1e100	# Dielectric loss cut-off

	fk = []
	Y = []
	Z = []

	#~ print scipy.sqrt(C0/L0)
	print scipy.linalg.inv(R0)*(1/length)

	#~ for k in range(0,K):
		#~ fk.append(fK * (1 - scipy.cos((scipy.pi*k)/(2*(K-1)))))

		#~ Y.append(scipy.empty((N,N), dtype=scipy.complex128))
		#~ Z.append(scipy.empty((N,N), dtype=scipy.complex128))

		#~ for j in range(0 , N):
			#~ for i in range(0 , N):
				#~ Y[-1].real[i,j] = G0[i,j] + (fk[-1]/scipy.sqrt(1+(fk[-1]/fgd)))*Gd[i,j]
				#~ Y[-1].imag[i,j] = 2*scipy.pi*fk[-1]*C0[i,j]
				#~ Z[-1].real[i,j] = R0[i,j] + scipy.sqrt(fk[-1])*Rs[i,j]
				#~ Z[-1].imag[i,j] = scipy.sqrt(fk[-1])*Rs[i,j] + 2*scipy.pi*fk[-1]*L0[i,j]
				#~ if Y[-1].real[i,j] == 0:
					#~ Y[-1].real[i,j] = 1E-100;
				#~ if Z[-1].real[i,j] == 0:
					#~ Z[-1].real[i,j] = 1E-100;

	#~ W = []
	#~ for k in range(0,K):
		#~ W.append(scipy.dot(Y[k],Z[k]))

	#~ for k in range(0,K):
		#~ W[k] = scipy.linalg.sqrtm(W[k])

	#~ Yc = []
	#~ for k in range(0,K):
		#~ Yc.append(scipy.linalg.solve(Z[k],W[k]))


	#~ Td = scipy.dot(C0,L0)
	#~ Td = scipy.linalg.sqrtm(Td)

	#~ for k in range(0,K):
		#~ W[k] = length*(Td*2*scipy.pi*fk[k] - W[k])
		#~ W[k] = scipy.linalg.expm2(W[k])

	#~ for k in range(0,K):
		#~ print "W"
		#~ print W[k]
		#~ print "Yc"
		#~ print Yc[k]
	#~ print "Td"
	#~ print Td

	#~ W[0] = matrix([[1,-1.008858e-16],[-1.008858e-16,1]])

	#~ print -2*(matrix([[1,0],[0,1]]) - W[0]*W[0]).I*W[0]*Yc[0]

	#~ b = scipy.zeros(K,dtype=scipy.double)
	#~ for k in range(0,K):
		#~ for j in range(0,N):
			#~ for i in range(0,N):
				#~ b[k] += Yc[k].real[i,j]


	#~ A = scipy.zeros((K,K),dtype=scipy.double)
	#~ for j in range(0,K):
		#~ for i in range(0,K):
			#~ if j == 0:
				#~ A[i,j] = 1.0
			#~ elif i == 0:
				#~ A[i,j] = 0.0
			#~ elif j <= M:
				#~ A[i,j] = fk[i]**(2*j)
			#~ else:
				#~ A[i,j] = -1*(fk[i]**(2*(j-M)))*b[i]


	#~ scipy.linalg.solve(A,b,overwrite_b=True)

	#~ a = scipy.zeros(M+1,dtype=scipy.double)
	#~ a[-1] = 1.0
	#~ for i in range(0,M):
		#~ a[i] = b[K-i-1]

	#~ rts = scipy.roots(a)

	#~ # The roots solver sucks so using the solution from the toms solver
	#~ rts[0] = -4.854694e+11
	#~ rts[1] = -2.348122e+14
	#~ rts[2] = -2.493474e+15
	#~ rts[3] = -1.194260e+16
	#~ rts[4] = -4.123450e+16
	#~ rts[5] = -1.224192e+17
	#~ rts[6] = -3.507643e+17
	#~ rts[7] = -1.124769e+18
	#~ rts[8] = -6.079402e+18


	#~ fc2 = scipy.zeros(M,dtype=scipy.double)
	#~ fc = scipy.zeros(M,dtype=scipy.double)
	#~ j = 0
	#~ for i in range(0,M):
		#~ if rts.imag[i] == 0 and rts.real[i] < 0:
			#~ fc2[j] = -rts.real[i]
			#~ fc[j] = scipy.sqrt(fc2[j])
			#~ j += 1
	#~ M = j

	#~ fc2.resize(M)
	#~ fc.resize(M)

	#~ print fc
	#~ print fc2
	#~ print fk

	#~ A = scipy.zeros((K*2-1,M),dtype=scipy.double)
	#~ for k in range(0,K):
		#~ A[k,0] = 1.0
	#~ for k in range(K,(K*2-1)):
		#~ A[k,0] = 0.0
	#~ for j in range(1,M):
		#~ A[0,j] = 1.0;
		#~ for k in range(1,K):
			#~ A[k,j] = 1/(1+(fk[k]**2)/fc2[j])
		#~ for k in range(K,(K*2 -1)):
			#~ A[k,j] = -(fk[k-K+1]/fc[j])/(1+((fk[k-K+1]**2)/fc2[j]))

	#~ print A
	#~ At = scipy.transpose(A)
	#~ A = scipy.dot(At,A)
	#~ A = scipy.linalg.inv(A)
	#~ A = scipy.dot(A,At)
	#~ #print A



	#~ aYc = []
	#~ aW = []
	#~ for i in range(0, N):
		#~ b = scipy.zeros((K*2-1),dtype=scipy.double)
		#~ for j in range(0, N):
			#~ for k in range(0, K):
				#~ b[k] = Yc[k][j,i].real;
			#~ for k in range(K, (K*2 -1)):
				#~ b[k] = Yc[k-K+1][j,i].imag;

			#~ aYc.append(scipy.dot(A,b))
			#~ print aYc[-1]

			#~ for k in range(0, K):
				#~ b[k] = W[k][j,i].real;
			#~ for k in range(K, (K*2 -1)):
				#~ b[k] = W[k-K+1][j,i].imag;

			#~ aW.append(scipy.dot(A,b))
			#~ print aW[-1]

	#~ ycA = scipy.zeros(K, dtype=scipy.complex128)
	#~ ycB = scipy.zeros(K, dtype=scipy.complex128)
	#~ for k in range(0,K):
		#~ ycA[k] = aYc[0][0]
		#~ for j in range(1,M):
			#~ ycA[k] += aYc[0][j]/(1+((fk[k]*1.j)/fc[j]))
		#~ ycB[k] = Yc[k][0,0]

	#~ pylab.figure(1)
	#~ pylab.subplot(211)
	#~ pylab.plot(fk,ycA.real,'ro',fk,ycB.real,'bx')
	#~ pylab.subplot(212)
	#~ pylab.plot(fk,ycA.imag,'ro',fk,ycB.imag,'bx')
	#~ #pylab.show()

	#~ wA = scipy.zeros(K, dtype=scipy.complex128)
	#~ wB = scipy.zeros(K, dtype=scipy.complex128)
	#~ for k in range(0,K):
		#~ wA[k] = aW[0][0]
		#~ for j in range(1,M):
			#~ wA[k] += aW[0][j]/(1+((fk[k]*1.j)/fc[j]))
		#~ wB[k] = W[k][0,0]

	#~ pylab.figure(1)
	#~ pylab.subplot(211)
	#~ pylab.plot(fk,wA.real,'ro',fk,wB.real,'bx')
	#~ pylab.subplot(212)
	#~ pylab.plot(fk,wA.imag,'ro',fk,wB.imag,'bx')
	#~ pylab.show()

tester()
