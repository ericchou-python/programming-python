#!/usr/bin/env python

from swampy.Gui import *

def make_circle():
    circle = canvas.circle([0,0], 100, fill='red')
    entry = g.en(text='Enter Color')
    button2 = g.bu(text='Enter', command=change_color)
    global circle, entry

# handle the exception of changing color on a circle not created by 
# the order of operations, i.e. does not get to the color change until circle is created. 
def change_color():
    color = entry.get()
    colorList = ['white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta']
    if color not in colorList:
        print "The color you specified is not valid. Available colors are: "
        for i in colorList:
            print i
    else:
        circle.config(fill=color)

g = Gui()
g.title('Gui')
canvas = g.ca(width=500, height=500)
canvas.config(bg='white')
button1 = g.bu(text="Make Circle", command=make_circle)
g.mainloop()


