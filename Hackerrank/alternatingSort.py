# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 13:49:33 2019

@author: lalit
"""
import math

def alternatingSort(a):
	b=[0]*len(a)
	b[0] =a[0]
	b[1] = a[-1]
	
	for i in range(2,len(a)):
		if i%2!=0:
			b[i]=a[-math.ceil(i/2)]
		else:
			b[i]=a[int(i/2)]
			
	return sorted(set(b)) == b

#a = [1,3,5,6,4,2]
a = [-92, -23, 0, 45, 89, 96, 99, 95, 89, 41, -17, -48]
print(sorted(a))
print(alternatingSort(a))