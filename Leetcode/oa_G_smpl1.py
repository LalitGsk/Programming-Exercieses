# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 17:34:31 2019

@author: lalit
Write a function that, given a non-empty array A containing N integers, 
denoting the heights of the students, returns the minimum number of rows created.
A = [5, 4, 3, 6, 1] op: 1-[5,4,3,1] ; 2-[6]
"""

def solution(A):
  """Your solution goes here."""
  pivot=A[0]
  counter=1
  
  for student in range(1,len(A)):
    if A[student] > pivot:
      counter+=1
      pivot=A[student]
    else:
      pass
  
  return counter
