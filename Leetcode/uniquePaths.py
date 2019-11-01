# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 23:29:13 2019

@author: lalit
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time.
 The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?
"""
import math
class Solution:
    def uniquePaths(self, cols, rows):
        
        moves = [[0] * cols for row in range(rows)]
        for row in range(rows):
            for col in range(cols):
                if row == 0 or col == 0:
                    moves[row][col] = 1
                else:
                    moves[row][col] = moves[row - 1][col] + moves[row][col - 1]
        return moves[rows - 1][cols - 1]
        
#        return int(math.factorial(cols+rows-2)/ (math.factorial(cols-1)* math.factorial(rows-1)))
	
m = 3
n = 7
s = Solution()
print(s.uniquePaths(m, n))