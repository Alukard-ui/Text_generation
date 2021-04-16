# -*- coding: utf-8 -*-

# This is a text generator based on statistic

import zipfile

# zip_file_name = str(input('Your name of zip file')) # name of your file
#
# zfile = zipfile.ZipFile(zip_file_name,'r') # open file
# for filename in zfile.namelist():
#     zfile.extract(filename)
from pprint import pprint

file_name = str(input('Your file name'))

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
pprint(stat)

totals = {} # dictionary to count all char for prev_char
for prev_char, char_stat in stat.items():
    totals[prev_char] = 0
    for char,count in char_stat.items():
        totals[prev_char] += count

pprint(totals)