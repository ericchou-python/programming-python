#!/usr/bin/env python

from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
print bob

#fd and bk for forward and backward
#lt and rt for left and right turns. 
#each Turtle is holding a pen, either down or up; if the pen is down, 
#the Turtle leaves a trail when it moves. 
#The functions pu and pd stand for pen up and pen down.

# Draws a square 
#fd(bob, 100)
#lt(bob)
#fd(bob, 100)
#lt(bob)
#fd(bob, 100)
#lt(bob)
#fd(bob, 100)

# A better way to draw a square
for i in range(4):
    fd(bob, 100)
    lt(bob)

wait_for_user()

