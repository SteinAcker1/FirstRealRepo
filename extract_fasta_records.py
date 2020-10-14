#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 13:53:03 2020

@author: inf-34-2020
"""

import re
import sys

newFasta = []

fasta = sys.argv[1]
string = str(sys.argv[2])
output = sys.argv[3]

with open(fasta) as f:
    flag = True
    for line in f:
        if line.startswith('>'):
            seq = next(f)
            #Next() can only be used once per iteration; use it wisely
            if re.search('{0}'.format(string.upper()),seq) != None:
                newFasta.append(line)
                newFasta.append(seq)
                
with open(output,'w') as o:
    for line in newFasta:
        o.write(line)