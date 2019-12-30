# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 01:55:10 2019

@author: lalit
Given a string, find the length of the longest substring without repeating characters.
"""

def lengthOfLongestSubstring(s):
	#print('input: ',s)
	sliding_window = []
	max_len = 0
	
	for letter in s:
		if letter in sliding_window:
			max_len = max(len(sliding_window),max_len)
			sliding_window = sliding_window[sliding_window.index(letter)+1:]
		sliding_window.append(letter)
            
	return max(len(sliding_window),max_len)

s = "abcabcbb"
print(lengthOfLongestSubstring(s))