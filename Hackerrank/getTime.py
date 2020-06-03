# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 11:17:52 2020

@author: lalit
"""

def getTime(a,b,c,d):
    t=sorted([a,b,c,d])
    r = ''
    while len(t)!=0:
        if 2 in t:
            r= "2"
            t.remove(2)
            if 3 in t:
                r = r+"3:"
                t.remove(3)
            elif 2 in t:
                r = r+"2:"
                t.remove(2)
            elif 1 in t:
                r = r+"1:"
                t.remove(1)
            elif 0 in t:
                r = r+"0:"
                t.remove(0)
        elif 1 in t:
            r = r+"1" + str(max(t))+":"
            t.remove(max(t))
            t.remove(1)
        elif 0 in t:
            r = r+"0" + str(max(t))+":"
            t.remove(max(t))
            t.remove(0)
        if min(t)>5:
            return "NOT POSSIBLE"   
        if max(t)<=5:
            r = r+str(max(t))+str(min(t))
        else:
            r= r + str(min(t)) + str(max(t))
        
        return(r)
        
#print(getTime(1,8,3,2))
#print(getTime(2,4,0,0))
#print(getTime(3,0,7,0))
print(getTime(9,1,9,7))
