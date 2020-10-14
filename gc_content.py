#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 16:02:35 2020

@author: steinacker
"""

import sys
import re

input_file = sys.argv[1] #'paxillus.fna' 
allGC = []
allBases = []
seq = ''

with open(input_file, 'r') as r:
    for line in r:
        if line.startswith('>'):
            continue
        else:
            seq += line
allGC = len(re.findall('[GCgc]',seq))
allBases = len(re.findall('[ACGTacgt]',seq))
#            allGC.append(GC)
 #           allBases.append(bases)

GC_content = round(allGC * 100 / allBases,4)
print('The GC content of this sequence is {0}%.'.format(GC_content))