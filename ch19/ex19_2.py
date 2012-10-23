#!/usr/bin/env python

from swampy.Gui import *

def make_circle():
    canvas.circle([0,0], 100, fill='red')

g = Gui()
g.title('Gui')
canvas = g.ca(width=500, height=500)
canvas.config(bg='white')
button1 = g.bu(text="Make Circle", command=make_circle)
g.mainloop()


