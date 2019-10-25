# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 17:38:27 2019

@author: lalit
Given an array of positive integers, find the number of integers with even number of digits
"""
import math

def evenDigitsNumber(a):
	result=0
	for i in a:
		digit_count = int(math.log10(i))+1
		if digit_count%2==0:
			result+=1
	
	return result