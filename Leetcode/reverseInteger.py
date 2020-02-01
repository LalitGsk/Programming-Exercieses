# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 00:41:54 2020

@author: lalit
7. Given a 32-bit signed integer, reverse digits of an integer.
"""

class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if x[0]=='-':
            x = x[0] + x[:0:-1]
        else:
            x = x[::-1]
        #print(x)
        if int(x)<-2**31 or int(x)>2**31:
            return 0
        return(int(x))
		
s = Solution()
print(s.reverse(-123))