# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 16:54:04 2019

@author: lalit
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
"""

class Solution:
    def singleNumber(self, nums):
        a = 0
        for i in nums:
            a ^= i
        return a
        '''hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]
		return 2*sum(set(nums))-sum(nums)'''
    
s = Solution()
nums = [4,1,2,1,2]
print(s.singleNumber(nums))