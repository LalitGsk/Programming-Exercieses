# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 23:42:18 2019

@author: lalit
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.
"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count('1')
	
if __name__ == '__main__':
	s=Solution()
	x=1
	y=4
	print(s.hammingDistance(x,y))