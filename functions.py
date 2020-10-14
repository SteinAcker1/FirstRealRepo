#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 13:20:56 2020

@author: inf-34-2020
"""
#%% 1

def print_line():
    print('This is a function!')
print_line()

#%% 2

def print_line():
    return 'This is a function!'

a = print_line()
print(a)
print(a[0])

#%% 3

def greet(name1,name2):
    return 'Hello {0} and {1}!'.format(name1,name2)

b = greet('Björn', 'Dag')
print(b)

#%% 4

def greet(name1 = '?',name2 = '?'):
    return 'Hello {0} and {1}!'.format(name1,name2)

b = greet('Björn', 'Dag')
print(b)
b = greet('Björn')
print(b)

#%% 5

def add(a,b):
    return a+b
def multiply(a,b):
    return a*b

print(add(2,3))
print(multiply(2,3))

#%% 6

def calculate(a,b,operation):
    if operation == 'multiply':
        return a*b
    elif operation == 'add':
        return a+b

print(calculate(2,3,'add'))
print(calculate(2,3,'multiply'))
    
#%% 7
import re
def get_gc(DNA):
    GC = len(re.findall('[GCgc]',DNA))
    tot = len(DNA)
    content = GC * 100 / tot
    return(content)
    
print(get_gc('GACAGACCGAGAACATAGACTGCATCGCATCAGATAGGCTTA'))

#%% 8
def many_hi(hi = 10):
    for i in range(hi):
        print('hi')

many_hi()

#%% 9
def list_hi(hi = 10):
    ls = []
    for i in range(hi):
        ls.append('hi')
    return ls

print(list_hi())

#%% 10
def list_hi(hi = 10,greet = 'hi'):
    ls = []
    for i in range(hi):
        ls.append(greet)
    return ls

print(list_hi(15,'hei'))

#%% 11
seqs = {'header1.1':'ATGCTAGCTAGCTAGCTACG','header1.2':'ACGTAGCTAGCTAGCAC','header2.1':'AGCTAGCTAGCTATTATCTACT'}

#%% 12
for i in range(3):
    print('Entry {0} has header: {1} and sequence: {2}'.format(i + 1, list(seqs.keys())[i], seqs[list(seqs.keys())[i]]))
    
#%% 13
def load_fasta(fasta):
    dictionary = dict()
    with open(fasta) as f:
        for line in f:
            if line.startswith('>'):
                head = line.strip('>').split(' ',1)[0]
                seq = next(f)
                dictionary[head] = seq
    return dictionary

#%%
genes = load_fasta('reads.fna')
sequences = list(genes.values())

for i in sequences:
    print('{0}: {1}'.format(i,get_gc(i)))









