# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 22:47:38 2020

@author: lalit
"""

def compute_number_score(number):
    score = 0

    str_nums = str(number)
    for char in str_nums:
        if int(char) == 9:
            score += 4

    str_nums = str(number)
    start, end = 0, 0
    for _ in str_nums:
        if str_nums[start] != str_nums[end] != 1:
            score += (end - start - 1) * 5
            start = end
        end += 1
    score += (end - start - 1) * 5

    str_nums = str(number)
    start, end = 0, 1
    pointer = 0
    while end < len(str_nums):
        if int(str_nums[pointer]) + 1 == int(str_nums[end]):
            pointer += 1
            end += 1
        else:
            score += pow(end - start, 2)
            start = end
            pointer += 1
            end += 1

    score = score + pow(end - start, 2)

    if number % 7 == 0:
        score += 1

    str_nums = str(number)
    for char in str_nums:
        if int(char) % 2 == 0:
            score += 2

    return score

print(compute_number_score(967851162))