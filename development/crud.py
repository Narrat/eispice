
FC = 0.5
VJ = 0.34
CJO = 0.14e-12
M = 0.4
Vd = FC*VJ*0.1

Cj = (CJO/(1-FC)**(1+M))*(1-FC*(1+M)+(M*Vd)/VJ)
print Cj

Cj = CJO/(1-Vd/VJ)**M
print Cj

