#!/usr/bin/env python

a = int(raw_input("Enter the value of a: \n"))
b = int(raw_input("Enter the value of b: \n"))
c = int(raw_input("Enter the value of c: \n"))

n = int(raw_input("Enter the vlaue of n: \n"))

if n > 2: 
    if (a**n + b**b == c**n): 
        print "Holy smoke, Fermat was wrong!"
    else: 
        print "No, that doesnt work"
else: 
    print "Please enter a n value greater than 2"

