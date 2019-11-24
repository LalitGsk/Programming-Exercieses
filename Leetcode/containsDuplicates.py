# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 23:51:15 2019

@author: lalit
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.
"""

class Solution:
    def containsDuplicate(self, nums):
        """hmaps={}
        for num in nums:
            if num not in hmaps:
                hmaps[num]=1
            else:
                return True
        return False"""
        return True if len(nums) > len(set(nums)) else False
	
s = Solution()
nums = [1,1,1,3,3,4,3,2,4,2]
ans = s.containsDuplicate(nums)
print(ans)