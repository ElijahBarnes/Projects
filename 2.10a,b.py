from math import*

a1 = 15.8
a2 = 18.3
a3 =.714
a4 = 23.2

print ("Please input the mass number ")
A = float(input ())
print ("Please input the atomic number ")
Z = float(input ())

if A%2 == 0:
    a5 = 12*(-1)**Z
else:
    a5 = 0

B=a1*A - a2*A**(2/3) - (a3*Z**2)/A**(1/3)- (a4*(A-2*Z)**2)/A+a5/A**(1/2)


print (B,"Is the total binding energy of the atom")
print (B/A, "is the binding energy per nucleon")
        
    
