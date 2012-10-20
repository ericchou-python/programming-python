#!/usr/bin/env python

import math

def square_root(a):
    y = 0
    result = 0
    while (a - result) > x:
        result = y*y
        y += 0.01
    answer = y-0.01 #we need the iteration before last
    print "%f %f %f %f" % (a, answer, math.sqrt(a), abs(answer-math.sqrt(a)))

x = 0.001

if __name__ == '__main__':
    q = raw_input('Find the square root up to: ')
    i = 1
    while i <= int(q): #took a while to figure out q was str to being with, and int is alway sless than str 
                       #end up in an infinite loop
        square_root(float(i))
        i += 1

