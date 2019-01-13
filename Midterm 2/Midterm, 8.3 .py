#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 10:28:06 2017

@author: elijahbarnes
"""

import numpy as np
import pylab as py


sigma = 10
r = 28
b = 8/3
R = np.array([0,1,0],float)
h = .01

t_pts = np.arange(0,100,.01)
x_pts = []
y_pts = []
z_pts = []

def F(R,t): #one function treated for the three differential equations
    x = R[0]
    y = R[1]
    z = R[2]
    fx = sigma*(y-x)
    fy = r*x - y - x*z
    fz = x*y - b*z
    return np.array([fx,fy,fz],float)

for t in t_pts: #Runge Method
    x_pts.append(R[0])
    y_pts.append(R[1])
    z_pts.append(R[2])				
    k1 = h*F(R,t)
    k2 = h*F(R + (1/2) * k1,t + (1/2)*h)
    k3 = h*F(R + (1/2) * k2,t + (1/2)*h)
    k4 = h*F(R + k3,t + h)
    
    R += (k1+2*k2+2*k3+k4)/6

#plot
"""
py.plot(t_pts,y_pts)
py.show()
"""
py.plot(z_pts,x_pts)
py.show()
