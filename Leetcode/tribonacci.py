# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 00:37:01 2020

@author: lalit
1137. The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
"""
class Solution:
	def tribonacci(self, n: int) -> int:
		if n <= 1:
			return n
		self.cache = {0: 0, 1: 1, 2:1}
		return self.memoize(n)
	
	def memoize(self, n: int) -> {}:
		if n in self.cache.keys():
			return self.cache[n]
		self.cache[n] = self.memoize(n-1) + self.memoize(n-2) + self.memoize(n-3)
		return self.memoize(n)
	
s = Solution()
print(s.tribonacci(25))