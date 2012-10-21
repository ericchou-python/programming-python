#!/usr/bin/env python

fin = open('words.txt', 'r')

for line in fin.readlines():
    if len(line.strip()) > 20:
        print line.strip()


