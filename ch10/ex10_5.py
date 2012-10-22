#!/usr/bin/env python

# remove by element
def chop(x):
    firstElement = x[0]
    lastElement = x[len(x)-1]
    x.remove(firstElement)
    x.remove(lastElement)
    print x

l = [1,2,3,4]

chop(l)
