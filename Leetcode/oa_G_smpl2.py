# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 17:37:19 2019
@author: lalit

Write a function that, given an array A of N integers, 
of which represents loads caused by successive processes,
the function should return the minimum absolute difference of server loads.
A=[1,2,3,4,5] op: 1,2,4 & 5,3
"""

def solution(A):
  """Your solution goes here."""
  A=sorted(A, reverse=True)
  proc1=[]
  proc1.append(A[0])
  proc2=[]
  proc2.append(A[1])
  proc1.append(A[2])
  
  for load in range(3,len(A)):
    if sum(proc1)>sum(proc2):
      proc2.append(A[load])
    else:
      proc1.append(A[load])
    
  return(abs(sum(proc1)-sum(proc2)))
