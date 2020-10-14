#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 13:13:12 2020

@author: inf-34-2020
"""

import re
#%% (a)
string = str(input('Enter anything: '))

s = re.search('\s',string)
if s != None:
    print('contains whitespace')
    
n = re.search('\d',string)
if n != None:
    print('contains numbers')
    
l = re.search('[a-z]',string)
if l != None:
    print('contains lowercase letters')
    
u = re.search('[A-Z]',string)
if u != None:
    print('contains uppercase letters')
    
# None is different from 'None'!!!
    
#%% (b)



#%% (c)
