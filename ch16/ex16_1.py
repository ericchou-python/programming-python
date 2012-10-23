#!/usr/bin/env python

class Time(object):
    """Represents the time of day. 

    attributes: hour, minute, second
    """

def print_time(x):
    print("%.2d:%.2d:%.2d" % (x.hour, x.minute, x.second))

time = Time()
time.hour = 11
time.minute = 59
time.second = 30

print_time(time)

