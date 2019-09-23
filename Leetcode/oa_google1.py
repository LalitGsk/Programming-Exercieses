# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 15:35:32 2019

@author: lalit
given string A (which contains M strings delimited by ',') 
and string B (which contains N strings delimited by ','),
 returns an array C of N integers.
 For 0 ≤ J < N, values of C[J] specify the number of strings in A which are strictly smaller than the comparison J-th string in B (starting from 0).
A = "abcd,aabc,bd" B = "aaa,aa" op:[3,2]
"""

import sys

def solution(A, B):
  """Your solution goes here."""
  #remove spaces from the string
  A = A.replace(" ", "")
  B = B.replace(" ", "")
  
  #split the words separated by ','
  A = A.split(",")
  B = B.split(",")

  result = []
  for current in B:
    count = 0
    min_B = sorted(current)[0]
    # retrieve the count of smallest character in a string in B
    count_min_B = current.count(min_B)
    
    #compare the string in B with strings in A
    for word in A:
        min_A = sorted(word)[0]
        # retrieve the count of smallest character in a string in B
        count_min_A = word.count(min_A)
         # comparing the freq of smallest char in string in B
        if (count_min_B > count_min_A):
            count += 1
    #add the count to resulting array
    result.append(count)
    
  return(result)


def main():
  """Read from stdin, solve the problem, write answer to stdout."""
  input = sys.stdin.readline().split()
  A = input[0]
  B = input[1]
  sys.stdout.write(",".join([str(i) for i in solution(A, B)]))


if __name__ == "__main__":
  main()
