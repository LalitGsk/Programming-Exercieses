# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 21:46:59 2019

@author: lalit
Given an integer n, calculate the alternating sum of its digits.
"""

def numberSigningSum(n):
	a = str(n)
	res=0
	for i in range(len(a)):
		if i%2!=0:
			res = res - int(a[i])
		else:
			res+= int(a[i])
			
	return(res)
	
if __name__ == '__main__':
	n=104956
	print(numberSigningSum(n))