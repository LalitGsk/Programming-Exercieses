# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 18:24:48 2020

@author: lalit
1002. Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  
For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.
"""

class Solution:
    def commonChars(self, A):
        result = []

        for c in set(A[0]):
            count = A[0].count(c)
            occurences = 1
            for i in range(1,len(A)):
                if c in A[i]:
                    count = min(count,A[i].count(c))
                    occurences += 1
                else:
                    break
                if occurences == len(A):
                    for i in range(count):
                        result.append(c)

        return(result)
		
s = Solution()
#A = ["bella","label","roller"]
A = ["acabcddd","bcbdbcbd","baddbadb","cbdddcac","aacbcccd","ccccddda","cababaab","addcaccd"]
print(s.commonChars(A))