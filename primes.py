#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 15:10:06 2020

@author: inf-34-2020
"""

ls = [2,3,5,7,11,13,17,19,23]
nums = list(range(2,23))
while len(ls) < 1000:
    nums.append(nums[-1] + 1)
    x = nums[-1]
    d = list(range(2,round(x**0.5) + 1))
    for i in d:
        rem = x%i
        if rem == 0:
            prime = False
            break
        elif i == d[-1] and rem != 0:
            prime = True
    if prime == True and x > ls[-1]:
        ls.append(x)

print(ls)