# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 19:22:51 2020

@author: lalit
917. Given a string S, return the "reversed" string 
where all characters that are not a letter stay in the same place, 
and all letters reverse their positions.
"""

def reverseOnlyLetters(S: str):
	S = list(S)
	left =0
	right = len(S)-1
	
	while left<right:
		if not S[left].isalpha():
			left+=1
		elif not S[right].isalpha():
			right-=1
		else:
			S[left], S[right] = S[right], S[left]
			left+=1
			right-=1
	result = "".join(S)
	return result

a = "Test1ng-Leet=code-Q!"
print(reverseOnlyLetters(a))