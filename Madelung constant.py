from math import*

M=0
L=100
for i in range (-L,L):
    for j in range (-L,L):
        for k in range (-L,L):
            if i==j==k==0:
                M=M
            else:
                M+=(-1)**(i+j+k)/(sqrt(i**2 + j**2 + k**2))

print (M)
    
