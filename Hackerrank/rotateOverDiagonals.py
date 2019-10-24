# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 17:43:57 2019

@author: lalit
"""

def rotateOverDiagonals(m, k):
	result = m
	for i in range(k):
		result = rotateMatrix(result)
		
	return result

def rotateMatrix(A):
	 N = len(A[0])
	 
	 for i in range(N//2):
		 for j in range(i, N-i-1):
			 if i==j:
				 pass
			 else:
				 temp = A[i][j]
				 temp, A[i][j], A[N-1-j][i], A[N-1-i][N-1-j], A[j][N-1-i] = A[i][j], A[N-1-j][i], A[N-1-i][N-1-j], A[j][N-1-i], temp
				 
	 return A

	

mat = [[1,2,3],[4,5,6],[7,8,9]]
k=1
print(rotateOverDiagonals(mat, k))