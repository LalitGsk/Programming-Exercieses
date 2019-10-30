# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 17:06:19 2019

@author: lalit
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)==0:
            return 0
        low = 0
        high = len(needle)
        while(low+high<=len(haystack)):
            if haystack[low:low+high]==needle:
                return low
            low+=1
        return -1            
        
s = Solution()
h='hello'
n='ll'
print(s.strStr(h, n))