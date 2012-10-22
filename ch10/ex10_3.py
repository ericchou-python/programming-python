#!/usr/bin/env python

def cum_sum(l):
    total = 0
    newList = []
    #combine range and length function to perform
    #action on every item of a list
    #in this case it is calculating a comulative total
    #and append to a new list
    for i in range(len(l)):
        total += l[i]
        newList.append(total)
    return newList


l = [1, 2, 3, 4, 5, 6]
s = cum_sum(l)
print s

