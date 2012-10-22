#!/usr/bin/env python

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def reverse_lookup(d, v):
    t = []
    for k in d:
        if d[k] == v:
            t.append(k)
    return t

h = histogram('parrot')
k = reverse_lookup(h, 2)
print k


