#!/usr/bin/env python

def do_twice(f, value):
    f(value)
    f(value)

def print_twice(x):
    print x * 2

def do_four(f, value):
    do_twice(f, value)
    do_twice(f, value)

print("Reult of do_twice: ")
do_twice(print_twice, 'spam')

print("Result of do_four: ")
do_four(print_twice, 'spam')
