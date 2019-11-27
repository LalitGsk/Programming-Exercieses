# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 23:45:59 2019

@author: lalit
Reverse bits of a given 32 bits unsigned integer.
"""

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int(str(bin(n))[::-1].split('b')[0] + '0'*(32 - len(str(bin(n))[::-1].split('b')[0])),2)
	
s = Solution()
result = s.reverseBits(43261596)
print(result)