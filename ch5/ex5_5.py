#!/usr/bin/env python

from swampy.TurtleWorld import *

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    fd(t, length*n)
    lt(t, angle)
    draw(t, length, n-1)
    rt(t, 2*angle)
    draw(t, length, n-1)
    lt(t, angle)
    bk(t, length*n)

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

#fd and bk for forward and backward
#lt and rt for left and right turns. 
#each Turtle is holding a pen, either down or up; if the pen is down, 
#the Turtle leaves a trail when it moves. 
#The functions pu and pd stand for pen up and pen down.

# Execution of different functions

draw(bob, 2, 5)

wait_for_user()

