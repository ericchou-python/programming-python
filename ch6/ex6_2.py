#!/usr/bin/env python

# 1. create empty function to print values of x and y
# 2. print values of x**2 and y**2
# 3. print values of their sum
# 4. find out that math.sqrt(x) returns the square root of x

import math

def hypotenuse(x, y):
    print math.sqrt(x**2 + y**2)

if __name__ == "__main__":
    hypotenuse(4, 4)

