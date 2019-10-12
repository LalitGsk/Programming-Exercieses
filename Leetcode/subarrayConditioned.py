# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 23:53:20 2019

@author: lalit
"""

def solve(A):
    c = 0
    l = len(A)

    for i in range(l):
        min_i = A[i]
        max_i = A[i]
        for j in range(i, l):
            min_i = min(min_i, A[j])
            max_i = max(max_i, A[j])

            if (max_i - min_i) == (j - i):
                # print(A[i:j+1], max_i - min_i, j - i)
                c += 1

    return c


	