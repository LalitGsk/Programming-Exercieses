# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 18:59:30 2019

@author: lalit
Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it. 
Find and return the shortest palindrome you can find by performing this transformation.

Example 1:

Input: "aacecaaa"
Output: "aaacecaaa"
"""

class Solution:
    def shortestPalindrome(self, s: str):
        l, r = s, ""
        rev_s = s[::-1]
        n = len(s)
        while(rev_s != r + l and n > 1):
            r += l[-1]
            l = l[:n - 1]
            n -= 1
        return r + s
    
s = Solution()
a = 'aabba'
print(s.shortestPalindrome(a))