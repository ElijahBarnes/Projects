#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 11:59:27 2017

@author: elijahbarnes
"""

import numpy as np
import pylab as py

M = 320
Epsilon = 1
Delta = 1e-6

Phi = np.zeros([M,M],float)
Phi_prime = np.zeros([M,M],float)

def Rho(x,y):
    if ((x == 3*(M/8) or x == 5*(M/8))  and (3*(M/8)<= y <= 5*(M/8))) or ((y == 3*(M/8) or y == 5*(M/8)) and (3*(M/8)<= x <= 5*(M/8))):
        rho = 1
    else:
        rho = 0
    return rho

while Epsilon > Delta:
    for y in range(M):
        for x in range(M):
            if y <= M/4 or x<=M/4 or y>=3*(M/4) or x>= 3*(M/4):
                Phi_prime[y,x] = Phi[y,x]
            else:
                Phi_prime[y,x] = Phi[(y+1)%M,x] + Phi[(y-1)%M,x] + Phi[y,(x+1)%M] + Phi[y,(x-1)%M]
                Phi_prime[y,x] = (1/4)*Phi_prime[y,x] + (.01**2/4)*(Rho(x,y))
    Epsilon = np.max(np.abs(Phi-Phi_prime))
    Phi,Phi_prime = Phi_prime,Phi
 
py.imshow(Phi,extent=[-3,3,-3,3])
py.show()

def E_1(x,y):
    E = -(Phi[y+1,x] - Phi[y,x])*(320/4)
    return E
def E_2(x,y):
    E = -(Phi[y,x+1] - Phi[y,x])*(320/4)
    return E

print ("The Potential at (0,0) is ", Phi[int(int(M/2)),int(M/2)])
print ("The Potential at (.75,0) is ",Phi[int(M/2),int((11/16)*M)])
print ("The Electric Field at (0,0) is (",E_1(int(M/2),int(M/2)),",",E_2(int(M/2),int(M/2)),")")
print ("The Electric Field at (0,0) is (",E_1(int((11/16)*M),int(M/2)),",",E_2(int((11/16)*M),int(M/2)),")")
    
