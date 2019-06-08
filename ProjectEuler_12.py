# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 17:04:00 2019

@author: PrabhakaronA
"""

import math

div = 0
a = 1
tri = 0

while div < 501:
    div = 0
    tri = 0
    for i in range(1, a+1):
        tri = tri + i
    
    #print ("The triangular number is ", tri)
    for j in range(1, int(math.sqrt(tri) + 1)):
        if (tri % j == 0):
            div = div + 1
    
    div = div*2    # Each divisor's complimentary divisor
    #print ("The number of divisors is ", div)
    a = a + 1
