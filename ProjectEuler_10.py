# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 11:36:48 2019

@author: PrabhakaronA
"""
import math
n = 2
count = 0
a = []

while (n < 2*(10**6)):
    temp = 0
    for i in range(2, int(math.sqrt(n) + 1)):
        if (n%i == 0):
            temp = 1
            break
        else:
            continue
    
    if (temp == 0):
        count = count + n
    
    n = n+1
    

print ("the sum of prime numbers upto 2 million is: ", count)
