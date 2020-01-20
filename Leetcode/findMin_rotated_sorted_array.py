# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 18:58:00 2020

@author: lalit
153. Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
Find the minimum element.
"""

def findMin(nums):
	l, r = 0, len(nums)-1
        
	while r-l>1:
		m = (l+r)//2
		if nums[m] < nums[r]:
			r = m
		elif nums[m] > nums[r]:
			l = m
	return min(nums[l], nums[r])
	
a = [4,5,6,7,0,1,2]
print(findMin(a))