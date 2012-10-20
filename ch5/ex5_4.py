#!/usr/bin/env python

def is_triangle(a, b, c):
    if ((a > (b + c)) or (b > (a+c)) or (c > (a+b))):
        return "No"
    else:
        return "Yes"

def prompt():
    a = raw_input("Enter the length of the first side: \n")
    b = raw_input("Enter the length of the second side: \n")
    c = raw_input("Enter the length of the third side: \n")
    answer = is_triangle(int(a), int(b), int(c))
    print answer

if __name__ == "__main__":
    prompt()

    
