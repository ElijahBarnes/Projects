#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 10:40:40 2017

@author: elijahbarnes
"""

import numpy as np
import pylab as py

M = 100
V = 1
omega = 0.9
error = 1
delta = 1e-6

Phi = np.zeros([M+1,M+1],float)

while error > delta:
    for x in range(0,M):
        for y in range(0,M):
            
            if x == 20 and y>20 and y<80:
                Phi[y,x] = V
            if x == 80 and y>20 and y<80:
                Phi[y,x] = -V
            else:
                Phi[y,x] = (Phi[y+1,x] + Phi[y,x-1]+ Phi[y,x+1]+Phi[y-1,x])/4 - Phi[y,x]
                error = Phi[y,x]
                Phi[y,x] = (1 + omega) * Phi[y,x]
            if error > delta:
                delta = error
                
py.imshow(Phi,origin='lower')
py.gray()
        


