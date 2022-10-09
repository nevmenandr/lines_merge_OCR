#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import sys

SOURCE = sys.argv[1]
TARGET = '{}_merged'.format(SOURCE)
PUNCT_SPACE = re.compile('\s+([.,»!?;])')
PUNCT_SPACE2 = re.compile('([«])\s+')
PUNCT_PARAS = re.compile('[•}^$■]')
PUNCT_POINT = re.compile('\.{4,}')
PUNCT_DASH = re.compile('(-—)|(—-)')
PUNCT_DASH2 = re.compile('([^ ])—')
PUNCT_DASH3 = re.compile('—([^ ])')

def clean_punct(line):
    line = PUNCT_SPACE.sub('\\1', line)
    line = PUNCT_SPACE2.sub('\\1', line)
    line = PUNCT_PARAS.sub('', line)
    line = PUNCT_POINT.sub('...', line)
    line = PUNCT_DASH.sub('—', line)
    return line

def dash(line):
    line = PUNCT_DASH2.sub('\\1 —', line)
    line = PUNCT_DASH3.sub('— \\1', line)
    return line

def main():
    lst = os.listdir(SOURCE)
    os.mkdir(TARGET)
    for file in lst:
        if not file.endswith('.txt'):
            continue
        with open(os.path.join(SOURCE, file), encoding='utf-8') as file_read, open(os.path.join(TARGET, file), "w", encoding='utf-8') as file_write:
            for line in file_read:
                line = line.lstrip()
                if len(line) < 3:
                    file_write.write(line)
                    continue
                if line[-2] == '\xad' or line[-2] == '-':
                    line = line[:-2]
                line = clean_punct(line)
                line = dash(line)
                if '====page====' in line:
                    file_write.write('\n\n{}\n\n'.format(line))
                else:
                    file_write.write(line)
    return 0

if __name__ == '__main__':
    main()
