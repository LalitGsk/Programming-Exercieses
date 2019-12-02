# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 19:21:05 2019

@author: lalit
26: Given a sorted array nums, remove the duplicates in-place such that each element appear only once 
and return the new length.
"""

def removeDuplicates(nums):
	i = 0
	for j in range(1, len(nums)):
		if nums[i] != nums[j]:
			nums[i+1] = nums[j]
			i += 1
	return i + 1

a = [0,0,1,1,1,2,2,3,4]
print(removeDuplicates(a))