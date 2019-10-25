# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 17:41:03 2019

@author: lalit
Given 2 strings s and t, 
Determine the number of ways exactly one digit could be removed from one of the strings so that
s is lexicographically smaller than t after the removal 
"""

def removeOneDigits(s, t):
	count = 0
	for i in range(len(t)):
		if t[i].isdigit():
			if s < (t[:i]+t[i+1:]):
				count+=1
				
	for i in range(len(s)):
		if s[i].isdigit():
			if (s[:i][i+1:]) < t:
				count+=1
				
	return count