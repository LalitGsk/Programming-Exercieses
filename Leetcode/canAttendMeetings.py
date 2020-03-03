# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 08:14:29 2020

@author: lalit
252. Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
determine if a person could attend all meetings.
"""

def canAttendMeetings(intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        if len(intervals) <= 1:
            return True
        intervals.sort(key=lambda i: i[0])

        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False

        return True
	
a = [[0,30],[5,10],[15,20]]
print(canAttendMeetings(a))