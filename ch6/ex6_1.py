#!/usr/bin/env python

def compare(x, y):
    if x > y: 
        return 1
    elif x == y:
        return 0
    elif x < y: 
        return -1

if __name__ == "__main__":
    x = raw_input("enter x value: ")
    y = raw_input("enter y value: ")
    answer = compare(x, y)
    print answer
