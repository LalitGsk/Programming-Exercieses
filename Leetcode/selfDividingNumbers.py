# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 18:43:12 2020

@author: lalit
728. A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.
Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.
"""

class Solution:
    def selfDividingNumbers(self, left: int, right: int):
        def self_dividing(n):
            for d in str(n):
                if d == '0' or n % int(d) > 0:
                    return False
            return True
       
        ans = []
        for n in range(left, right + 1):
            if self_dividing(n):
                ans.append(n)
        return ans
	
s = Solution()
print(s.selfDividingNumbers(1, 22))
