#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 15:18:28 2017

@author: elijahbarnes
"""

import numpy as np
import pylab as py
import random as rand
N = 20
J = 1
step = 100000

def EM(T):
    E = -2*N*N
    M = N*N
    E_meas = 0
    M_meas = 0
    z = 0
    S = np.ones([N,N],float)
    for i in range(step):
        k_1 = rand.randrange(N)
        k_2 = rand.randrange(N)
        dE = S[k_1,(k_2 + 1)%N]+S[k_1,(k_2 - 1)%N]+S[(k_1 + 1)%N,k_2]+S[(k_1 - 1)%N,k_2]
        dE *= 2*J*S[k_1,k_2]
        R = np.exp(-dE/T)
        if (R > 1 or rand.random() < R):
            E += dE
            S[k_1,k_2] = -S[k_1,k_2]
            M += 2*S[k_1,k_2]
        if i > 20000 and i%(N*N) == 0:
            E_meas += E
            M_meas += np.abs(M)
            z += 1
    return E_meas/z, M_meas/z

E_pts = []
M_pts = []
Temp = np.arange(.1,4,.1)

for t in Temp:
    V = EM(t)
    E_pts.append(V[0])
    M_pts.append(V[1])
"""    
py.plot(Temp,E_pts)
py.plot(Temp,M_pts)
py.show()
"""
py.plot(Temp,np.gradient(E_pts))
py.show()   
            
            