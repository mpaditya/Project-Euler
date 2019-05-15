# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

i = 1
j = 2
sum = 2
k=0

while (j < 4000000):
    
    k = i + j
    
    if (k % 2 == 0):
        sum = sum + k
        
    i = j
    j = k
    
print (sum)