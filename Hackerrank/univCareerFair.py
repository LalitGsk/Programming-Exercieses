# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 09:45:57 2020

@author: lalit
"""

def univCareerFair(arrival, duration):
	maplist = sorted(list(zip(arrival, duration)), key=lambda p: (p[0],p[1]))
	print(maplist)
	
	start, end = 0, -float('inf')
	
	for a,d in maplist:
		if a >= end:
			start, end = start+1, a+d
	return start
	
arrival = [1,3,3,4,5,7]
duration = [2,2,1,1,2,1]
print(univCareerFair(arrival, duration))