# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 22:03:41 2019

@author: lalit
Given an array of integers a, count the number of pairs i and j where (i<j<a.length),
such that a[i] and a[j] are digit anagrams.
"""

def digitAnagrams(a):
	res = 0
	
	for i in range(len(a)):
		a[i] = str(a[i])
		
	for i in range(len(a)):
		for j in range(i+1, len(a)):
			if sorted(a[i]) == sorted(a[j]):
				res+=1
				
	return res

if __name__ == '__main__':
	a = [25,35,872,63,53,278,872]
	print(digitAnagrams(a))