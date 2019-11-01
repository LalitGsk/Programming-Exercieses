# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 23:26:28 2019

@author: lalit
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.
"""

class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)
        result = set()
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            target = 0 - nums[i]
            while l < r:
                if nums[l] + nums[r] == target:
                    result.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return list(result)
	
a = [-1, 0, 1, 2, -1, -4]
s = Solution()
print(s.threeSum(a))