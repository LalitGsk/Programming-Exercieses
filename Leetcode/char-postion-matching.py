# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 12:54:21 2019

@author: lalit
Write a function to return a hint according to the secret number and friend's guess, 
use A to indicate the bulls and B to indicate the cows.

your secret number exactly in both digit and position (called "bulls") and 
how many digits match the secret number but locate in the wrong position (called "cows").

Input: secret = "1123", guess = "0111"
Output: "1A1B"
Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.
"""

from collections import defaultdict
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        num_bulls = 0
        num_cows = 0
        s_dic = defaultdict(int)
        g_dic = defaultdict(int)
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                num_bulls+=1
            else:
                s_dic[secret[i]] +=1
                g_dic[guess[i]]+=1

        for g in g_dic:
            if g in s_dic:
                num_cows += min(g_dic[g],s_dic[g])
        return str(num_bulls)+'A'+str(num_cows)+'B'

'''secret = list(secret)
        A=0
        B=0
        sec_d = {}
        for i in range(0,len(secret)):
            if secret[i] not in sec_d:
                sec_d[secret[i]] = [i]
            else:
                sec_d[secret[i]].append(i)
                
        for i in range(0, len(guess)):
            if guess[i] in sec_d:
                if i in sec_d[guess[i]]:
                    #if i == sec_d[guess[i]].index(sec_d[guess[i]][i]):
                    sec_d[guess[i]].pop(0)
                    sec_d[guess[i]].append('#')
                    #print(sec_d[guess[i]])
                    A+=1
                elif len(sec_d[guess[i]])!=0:
                    sec_d[guess[i]].pop(0)
                    sec_d[guess[i]].append('#')
                    #print(sec_d[guess[i]])
                    B+=1
        res=str(A)+'A'+str(B)+'B'                
        return(res)
		
		
secret = '11'
guess = '11'

print(getHint(secret,guess))'''