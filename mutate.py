#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 15:00:13 2020

@author: inf-34-2020
"""
from random import sample
seq = list(input('Enter a nucleotide sequence: '))
b = sample(range(len(seq)-1),1)
seq[b[0]] = sample('ACTG',1)[0]
seq = str(seq).strip(" >,'")
seq.strip(" >,'")
print(seq)