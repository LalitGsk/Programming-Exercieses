# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 17:15:42 2019

@author: lalit
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0:
            return []
        hmaps ={}
        for i in range(len(nums)):
            if (target - nums[i]) in hmaps:
                return([hmaps[target-nums[i]], i])
            hmaps[nums[i]] = i
        return []