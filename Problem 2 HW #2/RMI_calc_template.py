# HOMEWORK 2 Reading from a data file. Fill in the area for the integrand.
from numpy import loadtxt
from pylab import plot, show, xlim, legend, xlabel, ylabel, title

data = loadtxt('data1.txt')  # loads the data file
T_plot = data[0]  # plot of temperatures
E_1 = data[1]  # plot of first energy
E_2 = data[3]  # plot of second energy
E_3 = data[5]  # plot of third energy

count = len(T_plot)  # number of temperature points

deltaT = 0.1

# Fill in this space with the calculation of RMI for each temperature:
### CODE ##

import numpy as np
from pylab import*

def f(x):
    return (2*E_1[x]-E_2[x]+2*E_3[x])/T_plot[x]**2

def RMI(i):
    h=.1
    S1 = 0
    S2 = 0
    
    for k in range (i,998):
        S1 = f(k) + S1

    for n in range (i,998,2):
        S2 = f(n) + S2
        
    return h/3*(f(i)+f(997)+ 4*S1 + 2*S2)

def RMI2(i):   
    h=.2
    S1 = 0
    S2 = 0
    
    for k in range (i,498):
        S1 = f(k) + S1

    for n in range (i,498,2):
        S2 = f(n) + S2
        
    return h/3*(f(i)+f(997)+ 4*S1 + 2*S2)



### CODE ###

plot(T_plot, E_1, label='Energy 1')
plot(T_plot, E_2, label='Energy 2')
plot(T_plot, E_3, label='Energy 3')
xlabel('Temperature (K)')
ylabel('Energy (J)')
title('Energy')
xlim(0, 100)
legend()
show()

### Error ###
F1 = []
F2 = []

for k in range(0,998):
    F1.append(RMI(k))
for k in range (0,998):
    F2.append(RMI2(k))
    
error = abs(F1[0]-F2[0])/15

np.plot(T_plot,F1)

show()

print("the error is ",error)
