# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 23:48:25 2019

@author: lalit
Given an array of 2n integers, your task is to group these integers into n pairs of integer, 
say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) 
for all i from 1 to n as large as possible.
"""

def arrayPairSum(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=[]
        nums = sorted(nums)
        i=1
        while i < len(nums):
            res.append(min(nums[i-1],nums[i]))
            i+=2
        
        return sum(res)
	
A=[4,1,3,2]
print(arrayPairSum(A))