#!/usr/bin/env python

fin = open('words.txt', 'r')

total_line = 0
line_with_e = 0

for line in fin.readlines():
    total_line += 1
    if line.find('e') == True:
        print line.strip()
        line_with_e += 1

print "Total Lines:", total_line
print "Lines with e:", line_with_e

# Remember for math functions use float for all the numbers
print "Percentage:", float(line_with_e) / float(total_line) * 100

