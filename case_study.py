#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 12:01:12 2020

@author: steinacker
"""

file = 'fungusAssembly.single.fna'

def load_fasta(fasta):
    dictionary = dict()
    with open(fasta) as f:
        for line in f:
            if line.startswith('>'):
                head = line.strip('>').split(' ',1)[0].strip('\n')
                #Remember to strip all the invisible characters too!
                seq = next(f)
                dictionary[head] = seq
    return dictionary

fastaDict = load_fasta(file)


gff = './binp16/Data/fungus_scaffold.gff'

def get_feature_coords(file, pattern):
    coords_list = []
    with open(file, 'r') as a:
        for line in a:
            row = line.split('\t')
            if len(row) > 2 and row[2] == pattern:
                tup = (row[0],row[2],row[3],row[4])
                coords_list.append(tup)
    return coords_list

ls = get_feature_coords(gff, 'CDS')
                