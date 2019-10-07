# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 19:09:40 2019

@author: lalit
"""

class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace("-", "").upper()
        right = len(S)- K
        while(right > 0):
            S = S[:right] + "-" + S[right:]
            right = right-K
        return(S)