# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 18:03:13 2019

@author: lalit
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. 
Assume that there is only one duplicate number, find the duplicate one.
"""

class Solution:
    def findDuplicate(self, nums):
		#return sum(nums)-sum(set(nums))
        h={}
        for i in nums:
            if i not in h:
                h[i] = 1
            else:
                h[i] +=1
                
        for i in h:
            if h[i]>1:
                return i
			
s = Solution()
nums = [2,2,2,2,2]
print(s.findDuplicate(nums))