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

stat = {}  # create dictionary for statistic
# example start = {'п':{'р':500,'ё':5,},'р':{'н':250,'й':1000,'о':1,}}

analysis_count = 4  # count of sequence

sequence = ' ' * analysis_count  # previous char
with open(file_name, 'r', encoding='utf-8') as file:
    for line in file:  # read line in our file
        line = line[:-1]
        for char in line:  # read char in our file
            if sequence in stat:  # if we already have char in the dictionary, we increase the vale
                if char in stat[sequence]:
                    stat[sequence][char] += 1
                else:
                    stat[sequence][char] = 1
            else:
                stat[sequence] = {char: 1}
            sequence = sequence[1:] + char  # in the previous char we enter the one that was in front of it

totals = {}  # dictionary to count all char for prev_char
stat_for_generate = {}
for sequence, char_stat in stat.items():
    totals[sequence] = 0
    stat_for_generate[sequence] = []
    for char, count in char_stat.items():
        totals[sequence] += count
        stat_for_generate[sequence].append([count, char])
    stat_for_generate[sequence].sort(reverse=True)

N = 1000  # volume char
printed = 0

sequence = ' ' * analysis_count
spaces_printed = 0
while printed < N:
    char_stat = stat_for_generate[sequence]
    total = totals[sequence]
    dice = randint(1, total)
    pos = 0
    for count, char in char_stat:
        pos += count
        if dice <= pos:
            break
    print(char, end='')
    if char == ' ':
        spaces_printed += 1
        if spaces_printed >= 10:
            print()
            spaces_printed = 0
    printed += 1
    sequence = sequence[1:] + char
