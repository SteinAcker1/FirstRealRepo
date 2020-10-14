#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 15:13:49 2020

@author: inf-34-2020
"""

import re
import sys
exp = re.compile('[A-Z][A-Za-z0-9_]+')
tree = sys.argv[1]
output = sys.argv[2]
ID_list = []

with open('pgi.tre') as tree:
    tree = tree.read()
    tree = tree.split(':')
    for line in tree:
        ID = exp.search(line)
        if ID != None:
            ID_list.append(ID.group())
                
with open(output, 'w') as c:
    for line in ID_list:
        c.write(line + '\n')