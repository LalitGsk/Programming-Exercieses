# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 19:01:38 2020

@author: lalit
80. Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice 
and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
"""

def removeDuplicates(nums):
    i=2
    while i<len(nums):
        if(nums[i]==nums[i-2]):
            #nums.append(nums[i+1])
            nums.pop(i)
        else:
            i+=1
    return len(nums)

a = [0,0,1,1,1,1,2,3,3]
print(removeDuplicates(a))