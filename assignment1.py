# -*- coding: utf-8 -*-

#Simple data types: Arithmetic
# 1) Before evaluating the expressions in Python, discuss what these expressions will return
#%%
# 5/0 will likely result in an error
5 / 0

#%%
# round(-3.6) will likely result in -4
print(round(-3.6))

#%%
# round(4.5) will likely result in 5
print(round(4.5))

#%%
# round(5.5) will likely result in 5
# Was wrong last time; decimal must be >5 to round up
print(round(5.5))
# Was wrong again... Python rounds to nearest even whole

#%%
# 5%-2 will likely return -1
print(5%-2)

#%%
# -5%2 will also likely return -1
print(-5%2)
# No, it returned 1

#%%
# -5%-2 will likely return -1
print(-5%-2)

#%%
# 2) Will these expressions return the same result?

# round(int(4.6))
# int(round(4.6))

# No they will not; the first will return 4 and the second will return 5

print(round(int(4.6)))
print(int(round(4.6)))

#%%
# 3) Programming languages often have a function called floor which returns the nearest integer less than the floating point number.
# There is also a function ceil which does the opposite.
# These functions are provided by the math module.

import math

print(int(-3.1)) #probably -3
math.floor(-3.1) #probably -4
math.ceil(3.1) #probably 4

#Simple data types: Strings

#%%
# 1) Will this work: len(5)?
# No, because len() requires a string. 5 is an integer.
len(5)

#%%
# 2) Figure out what len(str(len('len'))) returns, then test.
# It will return 1, as this command returns the length of the string version of the length of string 'len'

print(len(str(len('len'))))

#%%
# 3) Exploring string operations
# Turning "ATGC" to "ATCGXXX"
my_string = "ATGC"
print(my_string + "XXX")

#%%
# Turning "ATGC" to "ATGCATGCATGCATGC"
my_string = my_string * 4
print(my_string)

#%%
# Calculate length of new string
print(len(my_string))

#%%
# Calculate positions of different substrings
my_string = "AAAAGGAAAAGGAAAA"
print(my_string.index("GG")) #first position
import re
print([m.start() for m in re.finditer("GG",my_string)]) # all positions

#%%
# Find positions of "A", "AA", etc.
print(my_string.count("A"))
print(my_string.count("AA"))
print(my_string.count("AAA"))
print(my_string.count("AAAA"))
# Python looks for the first instance of each of these it can find and then continues. It does not consider overlapping instances.

#%%
a = "AcgT"
b = "acGT"

print(a.count(b))
#Python does not think these strings contain the same letters.

#%%
# Format method
string = "My name is {name} {surname}"
txt1 = string.format(name = "Karl", surname = "Johansson")
print(txt1)

txt2 = string.format(surname = "Karl", name = "Johansson")
print(txt2)

txt3 = string.format(name = "Karl"*2, surname = "Johansson")
print(txt3)

txt4 = string.format(name = "Karl"*2, surname = "Johansson"[:5])
print(txt4)


#%%
import random
ls = []
#Create blank list
for i in range(1000):
        randomlist = random.choices(['A','C','T','G'],k=3)
        #Generate random 3 bases
        codon = randomlist[0] + randomlist[1] + randomlist[2]
        #Concatenate 3 bases into a codon
        ls.append(codon)
        #Append codon to list
codonSet = set(ls)
#Convert codon list to set to get rid of duplicates
codonList = list(codonSet)
codonList = sorted(codonList)

print(codonList)

#%%
#Get leucine codons from codon list
leucine

#%%
#Collection data types: Dictionaries

d = dict()
d['banana'] = 27
d = {'dragonfruit': 65, 'apples': 12, 'lingonberry': 43}
d['apples'] += 4
print(d['apples'])
friend_week_fruits = {'apples':2, 'pears':1, 'oranges':2,
'waxberry':4}

d.update(friend_week_fruits)
print(d)

#%%
input_num1 = int(input("Give me the first number"))
input_num2 = int(input("Give me the second number"))
try:
    x = input_num1 * input_num2


#%%
    
list1 = [0,1]

while list1[-1] + list1[-2] < 1000:
    x = list1[-1] + list1[-2]
    list1.append(x)

list2 = []

for i in range(len(list1)-1):
    if list1[i]%2== 0:
        list2.append(list1[i])

print(sum(list2))
        





 

