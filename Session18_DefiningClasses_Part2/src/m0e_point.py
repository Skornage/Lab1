"""
A simple Point class.  It illustrates:
  -- Constructor __init__
  -- Fields
  -- Methods
  -- How to reference fields and methods:
       -- of constructed objects
       -- from within methods

Authors: Claude Anderson, David Mutchler, Matt Boutell, Dave Fisher,
         Chandan Rupakheti, their colleagues and others.  October 2013.
"""

import math


def main():
    """ Tests the Point class. """
    p1 = Point(1, 2)
    p2 = Point(-2, 6)
    print(p1, p2)

    d1 = p1.distance_from(p2)
    d2 = p2.distance_from(p1)
    d3 = p1.distance_from(p1)
    print("Distance between points {} and {} is {}".format(p1, p2, d1))
    print("Distance between points {} and {} is {}".format(p2, p1, d2))
    print("Distance between points {} and {} is {}".format(p1, p1, d3))

    p2.move_by(10, -6)
    d4 = p1.distance_from(p2)
    print("Distance between points {} and {} is {}".format(p1, p2, d4))

    p3 = Point(5, 5)
    p4 = Point(6, 3)
    points = (p1, p2, p3, p4)
    format_string = '{:14} {:14} Distance = {:5.2f}'
    for j in range(len(points)):
        for k in range(len(points)):
            distance = points[j].distance_from(points[k])
            print(format_string.format(points[j], points[k], distance))

    for point in points:
        farthest = point.farthest_point(points)
        print('Farthest point from', point, 'is', farthest)


class Point(object):
    """
    Represents a point in 2-dimensions with very simple properties
    and functionality (and no graphics).
    """

    def __init__(self, x, y):
        """ Constructs a Point at the given coordinates. """
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point(' + str(self.x) + ', ' + str(self.y) + ')'

    def move_by(self, dx, dy):
        """ Moves this point by the given amounts. """
        self.x = self.x + dx
        self.y = self.y + dy

    def distance_from(self, other):
        return math.sqrt(((self.x - other.x) ** 2) +
                         ((self.y - other.y) ** 2))

    def farthest_point(self, points):
        """
        Given a non-empty list of Points, returns the Point in the list
        that is farthest from this Point.
        """
        farthest = points[0]
        for point in points:
            if self.distance_from(point) > self.distance_from(farthest):
                farthest = point

        return farthest

#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
