#!/usr/bin/env python

import os

# example from http://www.doughellmann.com/PyMOTW/os/index.html#module-os

root = raw_input("Enter the root of the dirctory you want to walk> ")

#The function walk() traverses a directory recursively and for each directory 
#generates a tuple containing the directory path, any immediate sub-directories 
#of that path, and the names of any files in that directory.

for dir_name, sub_dirs, files in os.walk(root):
    print '\n', dir_name
    # list comprehension with subdirectories
    sub_dirs = ['%s/' % n for n in sub_dirs ]
    # Mix the directory contents together
    contents = sub_dirs + files
    contents.sort()
    for c in contents:
        print '\t%s' % c


# Another way of looking

print("*" * 10)
for dir_name, sub_dirs, files in os.walk(root):
    print "Directory Name: ", dir_name
    print "All subdirectories: ", sub_dirs
    print "Files: ", files

