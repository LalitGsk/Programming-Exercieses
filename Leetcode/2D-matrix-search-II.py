# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 23:15:37 2019

@author: lalit
"""

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if (len(matrix) == 0 or len(matrix[0]) == 0):
            return False
            
        height = len(matrix)
        width = len(matrix[0])
        
        row = height - 1
        col = 0
        
        
        while (col < width and row >= 0):
            if matrix[row][col] > target:
                row = row - 1
            elif matrix[row][col] < target:
                col = col + 1
            else:
                #print(matrix[row][col])
                return True
            
        return False
	
mat = [[1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]]
value = 5

if __name__ == '__main__':
	s = Solution()
	print(s.searchMatrix(mat, value))