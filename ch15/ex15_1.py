#!/usr/bin/env python

class Point(object):
    """Represents a point in 2-D space."""

    def distance_between_points(self, x, y):
        d = x - y
        return d

z = Point()
z.x = 10
z.y = 8

distance = z.distance_between_points(z.x, z.y)
print distance

