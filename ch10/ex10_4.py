#!/usr/bin/env python

# remove by index
def middle(x):
    x.pop(len(x)-1)
    x.pop(0)
    newList = x
    return newList

l = [1,2,3,4]

result = middle(l)
print result

