# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 17:33:43 2019

@author: lalit
Given array of integers, find the number of contiguous subarrays of length m containing pair of integers with a sum equal to k
"""

def findPairsSummingToK(a, m, k):
	low =0
	m_=m
	answer = 0
	if len(a)==0:
		return 0
	if m>len(a):
		return checkTwoSum(a, k)
	
	while(m_<=len(a)):
		answer+=checkTwoSum(a[low:m_], k)
		low+=1
		m_+=1
		
	return answer

def checkTwoSum(sub_arr, k):
	h={}
	for i, num in enumerate(sub_arr):
		n = k - num
		if n not in h:
			h[num]=i
		else:
			return 1
	return 0