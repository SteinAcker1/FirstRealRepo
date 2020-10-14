#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 14:23:41 2020

@author: inf-34-2020
"""
d = {}
r = open('regions.fna')
fasta = r.read()
#with open('regions.fna') as r:
for line in range(len(fasta)):
    if fasta[line].startswith('>') == True:
        print(fasta[line])