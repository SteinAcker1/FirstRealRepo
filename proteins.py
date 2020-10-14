#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 13:57:25 2020

@author: inf-34-2020
"""


#%%
d = {}
with open('ProtSeqs.txt') as ProtSeqs:
    for line in ProtSeqs:
        (key, seq) = line.split()
        d[key] = seq
#%%
for key in d:
    print(d[key])
#%%
for key in d:
    if 'W' in d[key]:
        print(d[key])
#%%
for key in d:
    if 'X' not in d[key]:
        print(d[key])