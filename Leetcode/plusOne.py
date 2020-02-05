# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 18:53:54 2020

@author: lalit
66. Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
"""

class Solution:
    def plusOne(self, digits):
        s=''
        for i in range(len(digits)):
            s=s+str(digits[i])
        result = str(int(s)+1)
        return list(result)
	
s = Solution()
d = [9,9,9]
print(s.plusOne(d))
