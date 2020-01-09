# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 10:58:49 2020

@author: Administrator
"""

import os
files = os.listdir()
for fname in files:
    if fname.endswith(".bib"):
        newlines = []
        with open(fname,'r',encoding='utf-8') as fr:
            for line in fr:
                if r":E$" in line:
                    print(line)
                    line = line.replace(r":E$", r":C$")
                newlines.append(line)
        with open(fname,'w',encoding='utf-8') as fw:
            fw.writelines(newlines)
                    