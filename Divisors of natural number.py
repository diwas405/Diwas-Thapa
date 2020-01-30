# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 11:54:39 2020

@author: Diwas
"""
# find all the divisors for a natural number between 2 and 9
#==============================================
#           modules
#==============================================
import numpy as np
import matplotlib.pyplot as plt
#------------------function
def fct_find_divisor( n):
    a_testdiv = np.arange( 2, 10, 1)
    l_truediv = []
    for curr_div in a_testdiv:
       # print( curr_div, i_n%curr_div)
        if i_n%curr_div == 0:
           l_truediv.append( curr_div)
    return l_truediv
#==============================================
#           parameters, variables
#==============================================
i_Number= int(input("Enter number:"))
#==============================================
#           compute pi
#==============================================
print( 'all divisors of %i :'%(i_Number), fct_find_divisor( i_Number) )
