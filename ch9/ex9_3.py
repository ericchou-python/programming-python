#!/usr/bin/env python

def avoids(w):
    total_count = 0
    forbidden_count = 0
    for i in w:
        fin = open('words.txt', 'r')
        for line in fin.readlines():
            total_count += 1
            if line.find(i) == True:
                forbidden_count += 1
    print forbidden_count
    print total_count
    print("Forbidden word percentage: ", float(forbidden_count)/float(total_count)*100)


forbidden = raw_input("Enter a string of forbidden letters: ")

avoids(forbidden)
