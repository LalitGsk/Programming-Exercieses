# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 23:38:07 2019

@author: lalit
"""

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums = sorted(nums, reverse = True)
        return(nums[k-1])
		
if __name__ == '__main__':
	nums = [25,23,1,2,3,4,5,6,7,8,9,10,76,80]
	s=Solution()
	print(s.findKthLargest(nums, 4))