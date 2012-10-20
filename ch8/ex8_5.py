#!/usr/bin/env python

def count(x, word):
    word = word
    count = 0
    for letter in word:
        if letter == x:
            count += 1
    print count

count('a', 'bananna')

