# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 17:18:34 2019

@author: lalit
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character but a character may map to itself.
Input: s = "paper", t = "title"
Output: true
Input: s = "foo", t = "bar"
Output: false
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))
    
    '''    if len(s)!=len(t):
            return False
        st_map = {}
        ts_map = {}
        for i in range(len(s)):
            if s[i] not in st_map:
                st_map[s[i]]=t[i]
            elif st_map[s[i]]!=t[i]:
                   return False
            if t[i] not in ts_map:
                ts_map[t[i]]=s[i]
            else:
                if ts_map[t[i]]!=s[i]:
                    return False            
        return True'''