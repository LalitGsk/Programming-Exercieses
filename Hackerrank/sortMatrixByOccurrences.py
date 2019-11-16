# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 22:10:07 2019

@author: lalit
Given a square matrix of integers m, rearrange its numbers in foll way,
First, sort in ascending order of the number's frequency and sort by values if frequencey is equal.
Second, place the sorted numbers diagonally, starting from the bottom right corner.
"""

def sortMatrixByOccurrences(m):
    ROW = len(m)
    COL = len(m[0])
    flat_arr = []
    
    for i in range(ROW):
        for j in range(COL):
            flat_arr.append(m[i][j])
    
    flat_arr = sorted(flat_arr, key=lambda s: (flat_arr.count(s),s), reverse=True)
    
    #print(flat_arr)
    c = 0
    for line in range(1, (ROW + COL)) :  
            start_col = max(0, line - ROW)   
            count = min(line, (COL - start_col), ROW) 
            for j in range(0, count) : 
                m[start_col + j][min(ROW, line) - j - 1] = flat_arr[c]
                c+=1
                
    return(m)
    
if __name__ == '__main__':
    a = [[1,4,-2],[-2,3,4],[3,1,3]]
    print(sortMatrixByOccurrences(a))