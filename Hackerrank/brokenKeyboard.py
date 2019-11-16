# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 21:52:12 2019

@author: lalit
Given an array letters representing the working letter keys,
and a string text; Determine how many words from text can by typed using broken keyboard.
"""

def brokenKeyboard(text, letters):
	t = text.lower().split()
	res=len(t)
	for word in t:
		for ch in word:
			if ch not in letters and not ch.isalpha():
				res-=1
				break
	return(res)
	
if __name__ == '__main__':
	text = "2 + 3 = 5"
	letters = ['o','l','r', 'e', 'w', 'd'] 
	print(brokenKeyboard(text, letters))