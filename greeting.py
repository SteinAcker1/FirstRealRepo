#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 13:19:55 2020

@author: inf-34-2020
"""
greetingStein = str('Very nice to see you again, Stein!')
greetingNotStein = str('Hello {0}')
greetingFriend = str('Glad to see you, {0}')
friends = {'Matt','Kim','Nisha'}
name = str(input("Please enter your name: "))
if name == 'Stein':
    print(greetingStein)
elif name in friends:
    print(greetingFriend.format(name))
else:
    print(greetingNotStein.format(name))