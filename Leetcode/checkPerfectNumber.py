# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 08:52:05 2020

@author: lalit
We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
"""

def checkPerfectNumber(num):
	if num <= 1: return False
	res,sq=0,int(num**0.5)
	for i in range(2,sq+1):
		if num % i == 0:
			print(num//i)
			print(i)
			res += i + num//i
			print(i+num//i)
	res += 1
	return res == num

a=28
print(checkPerfectNumber(a))

