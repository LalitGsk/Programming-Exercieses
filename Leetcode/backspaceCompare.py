# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 17:22:10 2019

@author: lalit
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c"
"""

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        if len(S)==0 or len(T)==0:
            return False
        S = list(S)
        T=list(T)
        #print(S,T)
        S  = removeBackspaces(S)
        #S=str(S).replace('#','')
        T = removeBackspaces(T)
        #T=str(T).replace('#','')   
        if S==T:
            return True
        else:
            return False
            
def removeBackspaces(A):
    i=0
    while i<len(A):
        #print(i)
        if A[i]=='#':
            if i==0:
                del A[i]
                #i=i-1
            else:
                del A[i-1:i+1]
                i=i-1
        else:
            i+=1
    return A