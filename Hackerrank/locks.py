# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 10:27:24 2020

@author: lalit
"""

strings = ["ACQUIRE 123","ACQUIRE 364", "ACQUIRE 84", "RELEASE 84", "RELEASE 364","ACQUIRE 789", "RELEASE 456", "RELEASE 364"]
strings = ["ACQUIRE 364", "ACQUIRE 84", "ACQUIRE 364", "RELEASE 364"]

stack = []
result = 0
for index, lock in enumerate(strings):
    lock = lock.split()
    if lock[0] == "ACQUIRE":
        if lock[1] in stack:
            result = index+1
            break
        stack.append(lock[1])
    if lock[0] == "RELEASE":
        if not lock[1] == stack.pop():
            print(lock[1], not lock[1], stack.pop())
            result = index+1
            break
    print(stack)
#if len(stack):
#    result = len(strings)+1
print(result)
print(stack)