#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 09:18:15 2017

@author: elijahbarnes
"""

import numpy as np
import pylab as py

pi = np.pi

def V(x_1,x_2,x_1p,x_2p):
    if (x_1p == 1/2 or x_1p == -1/2 and x_2p < 1/2 and x_2p > -1/2) or (x_2p == 1/2 or x_2p == -1/2 and x_1p > -1/2 and x_1p < 1/2):
        rho = 1
    else:
        rho = 0    
    S = (((x_1 - x_1p + 1e-6)**2 + (x_2 - x_2p + 1e-6)**2)**(-1/2))
    return rho*S

def HTrap(x_1,x_2,x_2p):
    h = .01
    N = len(np.arange(-1/2,1/2,h))
    Delta = 1e-6
    Epsilon = 1
    I_1 = 0
    I_2 = 0
    S_2 = 0
    I_1 = V(x_1,x_2,-1/2,x_2p)/2 + V(x_1,x_2,1/2,x_2p)/2 
    
    for k in range (N):
        I_1 += V(x_1,x_2,-1/2 + k*h,x_2p)  
    I_1 = h*I_1            
    while Epsilon > Delta:
        h= h/2
        N= 2*N
        for k in range (1,N,2):
            S_2+= V(x_1,x_2,-1/2+k*h,x_2p)
            I_2 = I_1/2 + h*S_2
        Epsilon = (I_2-I_1)/3
        I_1 = I_2
                    
    return I_1

def VTrap(x_1,x_2,x_1p):
    h = .01
    N = len(np.arange(-1/2,1/2,h))
    Delta = 1e-6
    Epsilon = 1
    I_1 = 0
    I_2 = 0
    S_2 = 0
    I_1 = V(x_1,x_2,x_1p,-1/2)/2 + V(x_1,x_2,x_1p,1/2)/2 
    
    for k in range (N):
        I_1+= V(x_1,x_2,x_1p,-1/2+k*h) 
    I_1 = h*I_1         
    while Epsilon > Delta:
        h= h/2
        N= 2*N
        for k in range (1,N,2):
            S_2+= V(x_1,x_2,x_1p,-1/2+k*h)
            I_2 = I_1/2 + h*S_2
        Epsilon = (I_2-I_1)/3
        I_1 = I_2
                    
    return I_1

def Potential(x_1,x_2):
    P = HTrap(x_1,x_2,-1/2) + HTrap(x_1,x_2,1/2) + VTrap(x_1,x_2,-1/2) + VTrap(x_1,x_2,1/2)
    return P

print ("The potential at (0,0) is ",Potential(0,0))
print ("The potential at (3/2,0)is ",Potential(3/2,0))

def E_1(x_1,x_2):
    h = 1e-3
    S = -(Potential(x_1 + h,x_2) - Potential(x_1,x_2))
    return S/h
def E_2(x_1,x_2):
    h = 1e-3
    S = -(Potential(x_1,x_2 + h) - Potential(x_1,x_2))
    return S/h

print ("The Electrc Field at (0,0) is (",E_1(0,0),",",E_2(0,0),")")
print ("The Electrc Field at (0,0) is (",E_1(3/2,0),",",E_2(3/2,0),")")

M= 100
Image = np.zeros([M,M],float)
for i in range(M):
    for j in range(M):
        M[i,j] = Potential(4*i/M-2,4*j/M-2)
        
py.imshow(M,extent = [-2,2,-2,2])
py.show()