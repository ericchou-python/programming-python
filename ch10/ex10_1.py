#!/usr/bin/env python

def nested_sum(t):
    total = 0
    for i in t:
        for j in i:
            total += j
    return total

l = [[1,2,3], [1,2,3] , [1,2,3]]

total = nested_sum(l)
print total

