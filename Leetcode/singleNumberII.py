# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 17:28:45 2019

@author: lalit
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. 
Find the two elements that appear only once.
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        occur = {}
        ret = []
        for num in nums:
            if num not in occur:
                occur[num] = 1
            else:
                occur[num] += 1
        for elem in occur:
            if occur[elem] == 1:
                ret.append(elem)
                break
        return ret[0]
    
    '''class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a=nums[0]
        for i in range(1,len(nums)):
            if a==nums[i]:
                a = a& nums[i]
            else:
                a ^= nums[i]
        return a
        #return int((3*sum(set(nums))-sum(nums))/2)
        '''
        
s = Solution()
nums = [0,1,0,1,0,1,99]
print(s.singleNumber(nums))