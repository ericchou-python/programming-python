#!/usr/bin/env python

def is_between(x, y, z):
    if x <= y <= z:
        return True
    else:
        return False

if __name__ == "__main__":
    print is_between(3, 2, 3)


