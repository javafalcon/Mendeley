# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 13:47:41 2020

@author: Administrator
"""

import os
files = os.listdir()
for fname in files:
    if fname.endswith(".bib"):
        newlines = []
        with open(fname,'r',encoding='utf-8') as fr:
            for line in fr:
                if r":C$" in line:
                    print(line)
                    line = line.replace(r":C$", r":E$")
                newlines.append(line)
        with open(fname,'w',encoding='utf-8') as fw:
            fw.writelines(newlines)