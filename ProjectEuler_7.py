# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 11:36:48 2019

@author: PrabhakaronA
"""
import math
n = 2
count = 1
a = []

while (count < 10002):
    temp = 0
    for i in range(2, int(math.sqrt(n) + 1)):
        if (n%i == 0):
            temp = 1
            break
        else:
            continue
    
    if (temp == 0):
        count = count + 1
        a.append(n)
    
    n = n+1
    

print ("the 10001th prime number is: ", a[-1])