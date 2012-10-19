#!/usr/bin/env python

def print_boundary():
    print '+ '+'- ' * 4 + '+ ' + '- ' * 4 + '+'
   
def print_slash():
    print '/ '+'  ' * 4 + '/ ' + '  ' * 4 + '/ '

def print_square():
    print_boundary()
    print_slash(), print_slash(), print_slash(), print_slash() 
    print_boundary()
    print_slash(), print_slash(), print_slash(), print_slash()
    print_boundary()

def print_boundary_2():
    print '+ '+'- ' * 4 + '+ ' + '- ' * 4 + '+ ' +'- ' * 4 + '+ ' + '- ' * 4 + '+'
         
def print_slash_2():
    print '/ '+'  ' * 4 + '/ ' + '  ' * 4 + '/ ' +'  ' * 4 + '/ ' + '  ' * 4 + '/ '

def print_fourRows_fourColumns():
    print_boundary_2()
    print_slash_2(), print_slash_2(), print_slash_2(), print_slash_2()
    print_boundary_2()
    print_slash_2(), print_slash_2(), print_slash_2(), print_slash_2()
    print_boundary_2()
    print_slash_2(), print_slash_2(), print_slash_2(), print_slash_2()
    print_boundary_2()

if __name__ == "__main__":
    print_square()
    print "     "
    print_fourRows_fourColumns()


