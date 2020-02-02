# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 18:28:00 2020

@author: lalit
1207. Given an array of integers arr, 
write a function that returns true if and only if the number of occurrences of each value in the array is unique.
"""

import collections
class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        cnt = collections.Counter(arr)
        return(len(list(cnt.values()))==len(set(cnt.values())))
		
s = Solution()
arr = [-3,0,1,-3,1,1,1,-3,10,0]
print(s.uniqueOccurrences(arr))