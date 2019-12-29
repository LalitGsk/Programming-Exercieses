# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 01:52:52 2019

@author: lalit
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains the most water.
"""

def maxArea(height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) -1
        area = 0

        while left < right: 
            # Calculating the max area 
            area = max(area, min(height[left], height[right]) * (right - left)) 

            if height[left] < height[right]: 
                left += 1
            else: 
                right -= 1
        return area
	
ht = [1,8,6,2,5,4,8,3,7]
print(maxArea(ht))