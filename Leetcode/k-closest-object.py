# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 23:23:38 2019

@author: lalit
"""

total_crates = 6
points = [[3,6], [2,4], [5,3], [2,7], [1,8], [7,9]]
K = 3

if len(points)==0 or K>total_crates or points==None:
	print(0)
else:
	points.sort(key = lambda P: P[0]**2 + P[1]**2) #sorting wrt to shortest distance to objects(x,y)
	print(points[:K])		#returning  K closest objects