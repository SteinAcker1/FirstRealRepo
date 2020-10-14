#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 10:55:16 2020

@author: steinacker
"""

import sys

fasta = sys.argv[1]
output = sys.argv[2]
newFasta = []

with open(fasta) as f:
    for line in f:
        if line.startswith('>') == False:
            line = line.strip('\n')
        else:
            line = '\n' + line
            #be sure not to just have line.strip()! be sure to save the stripped line!
        newFasta.append(line)
            
with open(output, 'w') as o:
    for line in newFasta:
       o.write(line)
