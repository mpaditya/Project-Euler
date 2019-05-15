# -*- coding: utf-8 -*-
"""
Created on Tue May 14 06:51:09 2019

@author: Aditya
"""

import math

num = 600851475143
max = 0

while (num % 2 == 0):
    max = 2
    num = num/max

for i in range (3, int(math.sqrt(num))):
    if (num % i == 0):
        max = i
        num = num/max
        
    i = i +2

print (max)