#!/usr/bin/env python

from swampy.Gui import *

def make_label():
    g.la(text='Good Job!')

def make_button():
    g.bu(text='Next', command=make_label)

g = Gui()
g.title('Gui')
button1 = g.bu(text="Press Me", command=make_button)
g.mainloop()


