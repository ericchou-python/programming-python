#!/usr/bin/env python

import random

def sort_by_length(words):
    t = []
    for word in words:
        t.append((len(word)+random.random(), word))

    t.sort(reverse=True)

    res = []
    for length, word in t:
        res.append(word)
    return res


words = ['one', 'eno', 'two', 'owt', 'three', 'eerht']
result = sort_by_length(words)
print result

