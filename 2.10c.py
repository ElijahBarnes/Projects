from math import*

sup=-1000
a1 = 15.8
a2 = 18.3
a3 =.714
a4 = 23.2
b=[]
print ("Please input the atomic number ")
Z = int(input ())
sup=-1000
for A in range (Z,3*Z):
    
    if A%2 == 0:
        a5 = 12*(-1)**Z
    else:
        a5 = 0
        
    B=a1*A - a2*A**(2/3) - (a3*Z**2)/A**(1/3)- (a4*(A-2*Z)**2)/A+a5/A**(1/2)

    if B/A>sup:
        sup = B/A
        X = A
print (sup," is the binding energy per nucleon")       
print (X," is the most stable nucleus")


   




        
    
