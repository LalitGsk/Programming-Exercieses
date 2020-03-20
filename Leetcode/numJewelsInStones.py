# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 17:43:54 2020

@author: lalit
771. Jewels and Stones
You're given strings J representing the types of stones that are jewels, and S representing the stones you have. 
Each character in S is a type of stone you have.  
You want to know how many of the stones you have are also jewels.
The letters in J are guaranteed distinct, and all characters in J and S are letters. 
Letters are case sensitive, so "a" is considered a different type of stone from "A".
"""

def numJewelsInStones(J, S):
	res=0
	for ch in J:
		res += S.count(ch)
		S.replace(ch,'')
	return res

J = 'aA'
S = 'aAAbbbbb'
print(numJewelsInStones(J, S))