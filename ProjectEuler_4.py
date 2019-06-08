# -*- coding: utf-8 -*-
"""
Created on Tue May 14 07:36:49 2019

@author: Aditya
"""


n = 100

""" Mathematically, we can derive the formula for difference between the sum of the squares
 of the first 'n' natural numbers and the square of the sum to be equal to 
 
 S = [n * (n+1) * (n-1) * (3n+2)]/12
 
 """
 
sum = (n * (n+1) * (n-1) * (3*n+2))/12

print (sum)