# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 02:05:03 2019

@author: lalit
Given a string containing digits from 2-9 inclusive, 
return all possible letter combinations that the number could represent.
"""

def letterCombinations(digits):
	phone = {'2': "abc",
		     '3': "def",
             '4': "ghi",
             '5': "jkl",
             '6': "mno",
             '7': "pqrs",
             '8': "tuv",
             '9': "wxyz"}

	def backtrack(combination, next_digits):
		if len(next_digits) == 0:
			output.append(combination)
		else:
			for letter in phone[next_digits[0]]:
				backtrack(combination + letter, next_digits[1:])
				
	output = []
	if digits:
		backtrack("", digits)
	return(output)
        
if __name__ == '__main__':
	dig = '23'
	print(letterCombinations(dig))