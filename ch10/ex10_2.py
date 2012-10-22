#!/usr/bin/env python

def to_upper(t):
    newList = []
    for i in t:
        for j in i:
            word = j.upper()
            newList.append(word)
    return newList

l = [['this', 'is', 'an'], ['ExAmple', 'oF', 'a'] , ['nested', 'list', 'of', 'strings']]

result = to_upper(l)
print result

