from math import*

Y=0
sup = -1000
a1 = 15.8
a2 = 18.3
a3 =.714
a4 = 23.2
N=0

for Z in range (1,100):
    sup=-1000
    for A in range (Z,3*Z):
    
        if A%2 == 0:
            a5 = 12*(-1)**Z
        else:
            a5 = 0
        
        B=a1*A - a2*A**(2/3) - (a3*Z**2)/A**(1/3)- (a4*(A-2*Z)**2)/A+a5/A**(1/2)

        if B/A > sup:
            sup = B/A
            X = A
            Y=Z
            if sup>N:
                N = sup
                R = Z
                
                
                
        
            
                
          
    print (X, "is the most stable value for ",Z)
print (R, "is the atomic number with the maximum binding energy per nucleon")


   




        
    
