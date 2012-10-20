#!/usr/bin/env python

def find(word, letter, place):
    index = place
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

result = find('eric', 'e', 2)
print result

