# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 18:22:13 2019

@author: lalit
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
"""

class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        if sum(nums)==(n*(n+1))/2:
            return 0
        else:
            return int((n*(n+1))/2 - sum(nums))
        
s = Solution()
nums = [9,6,4,2,3,5,7,0,1]
print(s.missingNumber(nums))