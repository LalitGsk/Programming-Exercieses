# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 23:19:39 2020

@author: lalit
13. Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
"""

def romanToInt(s):
	map = {
		"I": 1,
		"V": 5,
		"X": 10,
		"L": 50,
		"C": 100,
		"D": 500,
		"M": 1000,
		}
	
	last = "M"
	res = 0
	
	for symbol in s:
		res += map[symbol]
		if map[symbol] > map[last]:
			res -= 2 * map[last]
		last = symbol
		
	return res