# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 17:44:23 2019

@author: lalit
A function that takes in a list of line segments and returns True if all segments link together and form a polygon
"""

from collections import Counter

def findChains(lines):
	point = []
	for line in lines:
		point.append((line[0],line[1]))
		point.append((line[2],line[3]))
		
	a = Counter(point)
	for val in a.values():
		if val%2!=0:
			return False
	return True

if __name__ == '__main__':
	lines = [[0,0,1,0],[1,1,1,0],[0,0,1,1]]
	print(findChains(lines))