#!/usr/bin/env python

def print_hello():
    print "Hello World"

# *args will give you a tuple of the arguments
# **kws will give you a dictionary of arguments

def do_n(func, *args):
    for i in range(args[0]):
       func()
        

if __name__ == "__main__":
    do_n(print_hello, 5)


