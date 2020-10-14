#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 13:35:19 2020

@author: inf-34-2020
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


gff = 'fungus_scaffold.gff'

def get_feature_coords(file, pattern):
    coords_list = []
    with open(file, 'r') as a:
        for line in a:
            row = line.split('\t')
            if len(row) > 2 and row[2] == pattern:
                tup = (row[0],row[2],row[3],row[4])
                coords_list.append(tup)
    return coords_list

featureCoords = get_feature_coords(gff, 'CDS')

def extractFeatures(genome_dict, coords):
    dictionary = dict()
    for s in coords:
        scaffold = s[0]
        start = int(s[2])
        end = int(s[3])
        fullseq = genome_dict[scaffold]
        seq = fullseq[start:end]
        dictionary['{0} {1}-{2}'] = seq
    return dictionary

geneDict = extractFeatures(fastaDict,featureCoords)
        

        
















