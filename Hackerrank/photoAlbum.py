# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 09:36:45 2020

@author: lalit
"""

def photoAlbum(images, idx):
	res = []
	for i in range(len(images)):
		res.insert(idx[i],images[i])
		
	return res

img = [0,1,2,3,4]
idx = [0,1,2,1,2]
print(photoAlbum(img,idx))