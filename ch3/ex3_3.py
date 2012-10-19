#!/usr/bin/env python

def right_justify(x):
    rightSpace = 70 - len(x)
    print " " * rightSpace + x


if __name__ == '__main__':
    right_justify('Eric')

