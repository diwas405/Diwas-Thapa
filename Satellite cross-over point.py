# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 12:08:46 2020

@author: Diwas
"""
# week 2 Q1: finding crossover point for two satellites
#=========================
#       Modules
#==========================

import numpy as np
import matplotlib.pyplot as plt

#-------------functions

def fct_f( c, t, t0):
    return c*( t-t0)
def fct_g( A, t, t0):
    return A*t+t0

#=========================
#       Parameters
#==========================
tmin, tmax = -10, 10
f_dt = 1e-2
i_n = int( (tmax-tmin)/f_dt)
t0 = 2.5
a = 5
c = 1.1
i_n = 1000
e=0.1

#=========================
#       Compute
#==========================
f_curr_t = tmin
for i in range( i_n):
    f_curr_g = fct_g( f_curr_t, a, t0)
    f_curr_f = fct_f( f_curr_t, c, t0)
    if abs( f_curr_g - f_curr_f) < e:
        print( 'cross over point at t = %.4f, g(t) = %.3f, f(t) = %.3f'%( f_curr_t, f_curr_f))     
f_curr_t += f_dt

#=========================
#       plot
#==========================
a_t = np.linspace( tmin, tmax, i_n)
a_g = fct_g( a_t, a, t0)
a_f = fct_f( a_t, c, t0)

plt.figure( 1)
plt.plot( a_t, a_g, 'r', label = 'g(t)')
plt.plot( a_t, a_f, 'b', label = 'f(t)')
plt.legend()
plt.xlabel( 'Time')
plt.ylabel( 'Position')
plt.show()
plt.clf()
