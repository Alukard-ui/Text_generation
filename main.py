# -*- coding: utf-8 -*-

# This is a text generator based on statistic

import zipfile

from pprint import pprint
from random import randint

class Chatter:

    def __init__(self, file_name, analysis_count):
        self.file_name = file_name # name of your file
        self.analysis_count = analysis_count # count of sequence
        self.stat = {} # dictionary of statistic

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name,'r') # open file
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def collect(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        sequence = ' ' * self.analysis_count  # previous char
        with open(self.file_name, 'r', encoding='utf-8') as file:
            for line in file:  # read line in our file
                line = line[:-1]
                for char in line:  # read char in our file
                    if sequence in self.stat:  # if we already have char in the dictionary, we increase the vale
                        if char in self.stat[sequence]:
                            self.stat[sequence][char] += 1
                        else:
                            self.stat[sequence][char] = 1
                    else:
                        self.stat[sequence] = {char: 1}
                    sequence = sequence[1:] + char  # in the previous char we enter the one that was in front of it

    def prepare(self):
        self.totals = {}  # dictionary to count all char for prev_char
        self.stat_for_generate = {}
        for sequence, char_stat in self.stat.items():
            self.totals[sequence] = 0
            self.stat_for_generate[sequence] = []
            for char, count in char_stat.items():
                self.totals[sequence] += count
                self.stat_for_generate[sequence].append([count, char])
            self.stat_for_generate[sequence].sort(reverse=True)

    def Chat(self,N,out_file_name = None):
        printed = 0
        if out_file_name is not None:
            file = open(out_file_name,'w',encoding='utf-8')
        else:
            file = None

        sequence = ' ' * analysis_count
        spaces_printed = 0
        while printed < N:
            char_stat = self.stat_for_generate[sequence]
            total = self.totals[sequence]
            dice = randint(1, total)
            pos = 0
            for count, char in char_stat:
                pos += count
                if dice <= pos:
                    break
            if file:
                file.write(char)
            else:
                print(char, end='')
            if char == ' ':
                spaces_printed += 1
                if spaces_printed >= 10:
                    if file:
                        file.write('\n')
                    else:
                        print()
                    spaces_printed = 0
            printed += 1
            sequence = sequence[1:] + char
        if file:
            file.close()


file_name = str(input('Your zipfile name \n'))
analysis_count = int(input('Count of sequence \n'))

chatter = Chatter(file_name=file_name, analysis_count=analysis_count)
chatter.collect()
chatter.prepare()
chatter.Chat(N=10000,out_file_name='out.txt')
