# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 09:44:47 2019

@author: lalit
"""

def maxTime(s):
    r = ''
    for i in range(len(s)):
        if s[i] == '?':
            if i == 0:
                r = '2' if s[1] == '?' or int(s[1]) <= 3 else '1'
            elif i == 1:
                r = r + '3' if r[0] == '2' else r + '9'
            elif i == 3:
                r += '5'
            elif i == 4:
                r += '9'
        else:
            r += s[i]
    return r

print(maxTime('23:5?')) # 23:59
print(maxTime('2?:22')) # 23:22
print(maxTime('0?:??')) # 09:59
print(maxTime('1?:??')) # 19:59
print(maxTime('?4:??')) # 14:59
print(maxTime('?3:??')) # 23:59
print(maxTime('??:??')) # 23:59