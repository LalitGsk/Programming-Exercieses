# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 23:38:26 2019

@author: lalit
"""

days = [1,2,1,2,0,1,1,0,0,0,4]

i = 0

while i< len(days)-1:
    if days[i] == -1:
        print("NO")
        break
    if days[i]%2 == 1:
        days[i] = 0
        days[i+1]-=1
        i+=1
    elif days[i] %2 == 0:
        days[i] = 0
        i+=1
        
if days[-1] % 2 == 0:
    days[-1] = 0
    
if days.count(0) == len(days):
    print("YES")
else:
    print("NO")