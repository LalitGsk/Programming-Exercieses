# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 18:36:40 2019

@author: lalit
9: Determine whether an integer is a palindrome.
 An integer is a palindrome when it reads the same backward as forward.
"""

def isPalindrome(x):
	s = str(x)
	rev_s = s[::-1]
	if s==rev_s:
		return True
	return False

print(isPalindrome(121))