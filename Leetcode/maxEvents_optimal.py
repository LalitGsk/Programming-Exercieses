# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 08:06:31 2020

@author: lalit
1353. Given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.

You can attend an event i at any day d where startTimei <= d <= endTimei. Notice that you can only attend one event at any time d.

Return the maximum number of events you can attend.
"""
import heapq

def maxEvents(events):
        events.sort(reverse=1)
        h = []
        res = d = 0
        while events or h:
            if not h:
                d = events[-1][0]
            while events and events[-1][0] <= d:
                heapq.heappush(h, events.pop()[1])
            heapq.heappop(h)
            res += 1
            d += 1
            while h and h[0] < d:
                heapq.heappop(h)
        return res
	
e = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]
print(maxEvents(e))