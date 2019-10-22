# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 17:28:40 2019

@author: lalit
Let's define a function f(s) over a non-empty string s, which calculates the frequency of the smallest character in s.
For example, if s = "dcce" then f(s) = 2 because the smallest character is "c" and its frequency is 2.

Now, given string arrays queries and words, return an integer array answer, 
where each answer[i] is the number of words such that f(queries[i]) < f(W), where W is a word in words.

Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
Output: [1,2]
Explanation: On the first query only f("bbb") < f("aaaa"). On the second query both f("aaa") and f("aaaa") are both > f("cc").
"""

from bisect import bisect_left

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:  
        queries = [-w.count(min(w)) for w in queries]
        words = sorted([-w.count(min(w)) for w in words])
        return [bisect_left(words, q) for q in queries]