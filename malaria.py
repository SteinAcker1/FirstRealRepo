#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Title: malaria.py
Author: Stein Acker
Date: 09-10-2020

Description:
    This script will attach protein descriptions gathered by BLASTX to the
    proteins' respective FASTA headers. The FASTA and BLASTX files to input are
    decided by the user.

List of user-defined functions:
    None.

List of non-standard modules:
    sys: Allows python script to easily interface with bash commands in a
    terminal.

Procedure:
    1. Convert BLASTX file to a dictionary containing sequence IDs as keys and
    hit descriptions as values.
    2. Use dictionary to attach hit descriptions to headers in the FASTA
    sequences based on sequence ID.
    3. Output modified FASTA data as text file.

Usage:
    ./malaria.py sequences.fna proteins.blastx.tab chosen_output_name.file
"""

import sys

fasta = sys.argv[1]
#Import FASTA data as system argument 1
blastx = sys.argv[2]
#Import BLASTX data as system argument 2
output = sys.argv[3]
#Assign output file as system argument 3
newFasta = []
#Create blank list to populate with modified FASTA data
blastxDict = dict()
#Create blank dictionary to populate with cleaned-up BLASTX data

with open(blastx, 'r') as a:
    for line in a:
        row = line.split('\t')
        #Turn each row in the BLASTX file into a tab-separated list
        blastxDict[row[0]] = row[9]
        #Create new entry in dictionary for each protein, with sequence ID as 
        #key and protein description as value

with open(fasta, 'r') as b:
    for line in b:
        line = line.strip('\n')
        #Strip the "new line" indicator from each line in the FASTA sequence
        if line.startswith('>'):
        #If the line contains a sequence ID...
            row = line.split('\t',1)
            #...turn each line into a list of 2 items, with sequence ID as the 
            #first and the rest of the line as the second...
            hitDescrip = blastxDict[row[0][1:]]
            #...define a new variable as the dictionary value returned by the 
            #protein's query name...
            if hitDescrip != 'null':
                #...check to make sure this variable doesn't have a null 
                #value...
                line = line + '\t protein={0}'.format(hitDescrip)
                #... and create a new line with this variable added to the end.
        newFasta.append(line)
        #Append all lines, both sequences and modified headers, to the 
        #previously blank newFasta list.

with open(output, 'w') as c:
    for line in newFasta:
        c.write(line + '\n')
        #Convert the newFasta list into a text file with line breaks.
