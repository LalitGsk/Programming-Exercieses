# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 23:24:55 2019

@author: lalit
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.
"""

class Solution:
    def jump(self, nums):
        if nums[0] == 0:
            return 0
        if len(set(nums)) == 1:
            return len(nums)//nums[0]-1
        goal = len(nums)-1
        time = 0
        while goal > 0:
            for i,j in list(enumerate(nums)):
                if i+j > goal or i+j == goal:
                    goal = i
                    time +=1
                    break
        return time
	
a = [2,3,1,1,4]
s = Solution()
print(s.jump(a))