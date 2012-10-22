#!/usr/bin/env python

def createDict(x):
    fin = open(x, 'r')
    newDict = {}
    for i in fin:
        newDict[i.strip()] = 'value'
    return newDict

fileName = 'words.txt'
new = createDict(fileName)

if 'expands' in new:
    print "'expands' is in the new dictionary"

