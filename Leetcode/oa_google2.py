# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 17:39:38 2019

@author: lalit
Write a function that, given a zero-indexed array A consisting of N integers and an integer K,
 returns the largest contiguous subarray of length K from all the contiguous subarrays of length K.
input: A = [1, 4, 3, 2, 5] k=4
"""

import sys

def solution(N, K):
  """Your solution goes here."""
  if len(N)<K or len(N)==0:
    return([])
  N_mat=[]
  start = 0
  end = K

  '''List of all possible contigous subarrays with length K'''
  while(end < len(N)+1):
    N_mat.append(N[start:end])
    start = start+1
    end = end+1

  '''Sorting the contigous subarrays in non-increasing order'''
  N_mat = sorted(N_mat, reverse = True)

  return(N_mat[0])

def main():
  """Read from stdin, solve the problem, write answer to stdout."""
  input = sys.stdin.readline().split()
  N = [int(x) for x in input[0].split(",")]
  K = int(input[1])
  sys.stdout.write(",".join([str(i) for i in solution(N, K)]))


if __name__ == "__main__":
  main()
