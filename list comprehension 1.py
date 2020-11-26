# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 11:36:43 2020

@author: 91852
"""

print('enter no. of input')
n=int(input())
print('enter 3 numbers of list')
a=int(input())
b=int(input())
c=int(input())
l=[]
for x in range(0,a+1):
    for y in range(0,b+1):
        for z in range(0,c+1):
            if x+y+z!=n:
                l.append([x,y,z])
print(l)