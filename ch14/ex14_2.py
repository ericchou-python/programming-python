#!/usr/bin/env python

import re

# re substitution usage:
# input = 'this is a file'
# output = re.sub('is', 'was', input)
# print output => thwas was a file

def sed(pattern, replace, inputFile, outputFile):
    try: 
        inputFile = open(inputFile, 'r')
        outputFile = open(outputFile, 'w')
        for line in inputFile.readlines():
            line = re.sub('pattern', 'replace', line)
            outputFile.write(line)
    except:
        print "Something went wrong."

pattern = raw_input('Pattern> ')
replace = raw_input('Replacement> ')

sed(pattern, replace, 'inputFile.txt', 'outputFile.txt')

