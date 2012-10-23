#!/usr/bin/env python

import string 

def readFile(x):
    file = open(f, 'r')
    fileWords = []
    exclude = set(string.punctuation)
    for line in file.readlines():
        line = line.strip()
        for w in line.split():
            #http://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
            w = ''.join(ch for ch in w if ch not in exclude)
            fileWords.append(w)

    return fileWords

f = 'beowulf.txt'
g = readFile(f)

print g

