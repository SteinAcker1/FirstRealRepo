#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 15:22:25 2020

@author: steinacker
"""

import sys

input_file = sys.argv[1] #str(input('Enter the name of the file you want to open: '))
output_file = sys.argv[2]

IDs = []
with open(input_file,'r') as r:
    for line in r:
        if line.startswith('>'):
            line = line.strip('>').split(' ',1)[0]
            IDs.append(line)

with open(output_file,'w') as output:
    for line in IDs:
        output.write(line + '\n')