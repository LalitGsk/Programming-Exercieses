# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 01:18:28 2019

@author: lalit
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.
"""

def lengthOfLastWord(s):
	return len(s.strip().split(' ')[-1])
		
print(lengthOfLastWord(" "))