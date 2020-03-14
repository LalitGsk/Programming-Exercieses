# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 21:23:17 2019

@author: lalit
"""
def concatenationSum(a):
#V1
    i = 0
    result = 0
    range_ = len(a)

    while i < range_:
        temp = str(a[i])
        for j in range(range_):
            result += (int(temp+str(a[j])))
        i+=1
    return result
#    
#V2  
#    import math
#    result=[]
#    for i in range(len(a)):
#        for j in range(len(a)):
#            temp = (a[i]*(10**(int(math.log10(a[j]))+1))+a[j])
#            result.append(temp)
#    return sum(result)
#
#
#V3
#    result=0
#    for i in range(len(a)):
#        for j in range(len(a)):
#            temp = a[i]*(10**int(len(str((a[j])))))+a[j]          
#            result+=temp
#    return(result)

a=[987153, 239178, 389649, 469261, 130806]
print(concatenationSum(a))