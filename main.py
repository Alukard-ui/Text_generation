# -*- coding: utf-8 -*-

# This is a text generator based on statistic

import zipfile

# zip_file_name = str(input('Your name of zip file')) # name of your file
#
# zfile = zipfile.ZipFile(zip_file_name,'r') # open file
# for filename in zfile.namelist():
#     zfile.extract(filename)
from pprint import pprint
from random import randint

file_name = str(input('Your file name \n'))

stat = {} # create dictionary for statistic
# example start = {'п':{'р':500,'ё':5,},'р':{'н':250,'й':1000,'о':1,}}

prev_char = ' ' #previous char
with open(file_name,'r',encoding='utf-8') as file:
    for line in file: # read line in our file
        for char in line: # read char in our file
            if prev_char in stat: # if we already have char in the dictionary, we increase the vale
                if char in stat[prev_char]:
                    stat[prev_char][char] +=1
                else:
                    stat[prev_char][char] = 1
            else:
                stat[prev_char] = {char:1}
            prev_char = char # in the previous char we enter the one that was in front of it

totals = {} # dictionary to count all char for prev_char
stat_for_generate = {}
for prev_char, char_stat in stat.items():
    totals[prev_char] = 0
    stat_for_generate[prev_char] = []
    for char,count in char_stat.items():
        totals[prev_char] += count
        stat_for_generate[prev_char].append([count,char])
    stat_for_generate[prev_char].sort(reverse=True)



N = 1000 # volume char
printed = 0

prev_char =' '
while printed < N:
    char_stat = stat_for_generate[prev_char]
    total = totals[prev_char]
    dice = randint(1,total)
    pos = 0
    for count,char in char_stat:
        pos += count
        if dice <= pos:
            break
    print(char,end='')
    printed += 1
    prev_char = char
