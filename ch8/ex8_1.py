#!/usr/bin/env python

def backwards(x):
    index = 0
    while abs(index) < len(x):
        index -= 1
        letter = x[index]
        print letter


i = raw_input('Enter a word: ')
backwards(i)

