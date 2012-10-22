#!/usr/bin/env python

def histogram(s):
    d = {}
    for c in s:
        d[c] = d.get(c, 0) #default value of 0, real value is existing
        d[c] += 1 #every c value gets 1 if it exist in the string
    t = d.keys()
    newT = sorted(t)
    for i in newT: 
        print i, d[i]

histogram('brontosaurus')


