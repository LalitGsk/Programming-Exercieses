# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 06:12:20 2020

@author: lalit
1353. Given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.

You can attend an event i at any day d where startTimei <= d <= endTimei. Notice that you can only attend one event at any time d.

Return the maximum number of events you can attend."""

def maxEvents(events):
        events.sort(reverse =1)
        print(len(events))
        print(events)
        maxi = events[0][1]
        print(maxi)
        qq = [False]*(maxi+1)
        print(qq)
        c=0
        for i in events:
            for j in range(i[0],i[1]+1):
                if(qq[j]==False):
                    qq[j]=True
                    c+=1
                    break
        return c


e = [[1,2], [3,4], [3,5], [2,2], [3,4], [3,3],[4,4 ]]    
print(maxEvents(e))