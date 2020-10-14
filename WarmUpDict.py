#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 11:05:45 2020

@author: inf-34-2020
"""
# Exercise 1
this_week_fruits = dict()
this_week_fruits['apples'] = 4
this_week_fruits['pears'] = 2
this_week_fruits['oranges'] = 2

this_week_fruits = {'apples':4,'pears':2,'oranges':2}

#Exercise 2
this_week_fruits['oranges'] += 5
this_week_fruits['watermelons'] = 1

#Exercise 3
print('We have:')
for i in this_week_fruits.keys():
    print('{0} {1}'.format(this_week_fruits[i], i))
    
#Exercise 4
fruits = list(this_week_fruits.keys())
fruits.sort()
print('We have:')
for i in fruits:
    print('{0} {1}'.format(this_week_fruits[i], i))

#Exercise 5
friend_week_fruits = {'apples':2, 'pears':1, 'oranges':2, 'waxberry':4}
for i in friend_week_fruits.keys():
    if i in fruits:
        this_week_fruits[i] += friend_week_fruits[i]
    else:
        this_week_fruits[i] = friend_week_fruits[i]
        
#Exercise 6
print('We have:')
for i in this_week_fruits.keys():
    print('{0} {1}'.format(this_week_fruits[i], i))

#Exercise 7
with open('fruitDict.txt','w') as f:
    f.write('key\tvalue')
    for i in this_week_fruits.keys():
        f.write('\n{0}\t{1}'.format(i,this_week_fruits[i]))
        
#Exercise 8
fruitDict = dict()
with open('fruitDict.txt','r') as f:
    for line in f:
        line = line.strip('\n')
        line = line.split('\t')
        if line[0] != 'key':
            fruitDict[line[0]] = line[1]
            
#Exercise 9
import statistics
avgPrice = statistics.mean([int(i) for i in fruitDict.values()]) 

#Exercise 10
print('Above')
for i in fruitDict.keys():
    val = int(fruitDict[i])
    if val > avgPrice:
        print(i)
        
print('Below')
for i in fruitDict.keys():
    val = int(fruitDict[i])
    if val < avgPrice:
        print(i)








