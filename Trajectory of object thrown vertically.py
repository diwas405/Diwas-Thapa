# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 11:47:22 2020

@author: Diwas
"""
# Week 1 Question 2
# maximum height of a ball thrown vertically

#==================================
#          modules
#==================================
import numpy as np
import matplotlib.pyplot as plt

#==================================
#          parameters
#==================================
v0 = 5
g = 9.81
i_n = 2000
a_t = np.linspace( 0, 2, i_n)

#==================================
#           Compute error
#==================================
a_y = v0*a_t-0.5*g*a_t**2
for i in range(1, i_n, 1):
    if a_y[i] > a_y[i-1]:
        f_ymax = a_y[i]
        f_tmax = a_t[i]
    else:
       break
print( "max height: %.3f n"%( f_ymax),"t at ymax= %.4f"%( f_tmax))
    
#==================================
#          plot
#==================================
plt.figure(1)
plt.plot( a_t, a_y, 'b-')
plt.plot( [f_tmax], [f_ymax], 'rw')
plt.xlabel( 'Time [s]')
plt.ylabel( 'Height of object [m]')
plt.show()