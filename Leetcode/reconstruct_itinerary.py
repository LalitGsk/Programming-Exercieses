# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 18:03:59 2020

@author: lalit
332. Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], 
reconstruct the itinerary in order. 
All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.
"""

import collections
class Solution:
    def findItinerary(self, tickets):
        tickets.sort()
        adj = collections.defaultdict(list)
        for route in tickets:
            adj[route[0]].append(route[1])
           
        res = []
        def dfs(dep):
            q = adj[dep]
            while(q and len(q) > 0):
                dfs(q.pop(0))
            
            res.insert(0,dep)
        dfs('JFK')
        return res

s= Solution()
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
print(s.findItinerary(tickets))