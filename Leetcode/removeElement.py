# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 18:55:22 2019

@author: lalit
27: Given an array nums and a value val, 
remove all instances of that value in-place and return the new length.
"""

def removeElement(nums, val):
	i=0
	while(i<len(nums)):
		if nums[i]==val:
			nums.pop(i)
		else:
			i+=1
	return(len(nums))
	
a=[0,1,2,2,3,0,4,2]
p=2
print(removeElement(a,p))