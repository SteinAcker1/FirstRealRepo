#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 13:34:28 2020

@author: inf-34-2020
"""

x = int(input('Enter a number: '))

#for x in range(1,101):
while x > 0:
    if x%3 == 0 and x%5 == 0:
        print('FizzBuzz')
    elif x%3 == 0:
        print('Fizz')
    elif x%5 == 0:
        print('Buzz')
    else:
        print(x)
    x = int(input('Enter a number: '))