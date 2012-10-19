#!/usr/bin/env python

from swampy.TurtleWorld import *

def square(t, length):
    # t is a turtle object
    for i in range(4):
        fd(t, length)
        lt(t)

def polygon(t, length, n):
    # x is a tutle object
    for i in range(n):
        fd(t, length)
        lt(t, 360/n)

def circle(t, r):
    polygon(t, r, 360)

# arc doesnt work
def arc(t, r, angle):
    polygon(t, r, angle)

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

#fd and bk for forward and backward
#lt and rt for left and right turns. 
#each Turtle is holding a pen, either down or up; if the pen is down, 
#the Turtle leaves a trail when it moves. 
#The functions pu and pd stand for pen up and pen down.

# Execution of different functions

square(bob, 20)
polygon(bob, 100, 5)
circle(bob, 2)
#arc(bob, 2, 5)

wait_for_user()

