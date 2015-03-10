"""
A moving-smiley exercise that illustrates the implementation of a class.

A Smiley can move on the screen, recogize a collision with another
Smiley, start and stop moving, and toggle between frowing and smiling.

Authors: Developed by Claude Anderson and revised many times by various
         people including Matt Boutell, Steve Chenoweth, David Mutchler,
         and now Noah Miller.  October 2013.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import math
import zellegraphics as zg
import time
import m1t_test_Smiley


def main():
    """ Calls the   TEST   functions in this module. """
    test_Smiley()


def test_Smiley():
    """ Tests the   Smiley   class. """
    print()
    print('--------------------------------------------------')
    print('Testing the   Smiley   class:')
    print('--------------------------------------------------')

    window = zg.GraphWin('Test the  Smiley  class', 400, 300)

    # TODO: 2. With your instructor:
    #   -- Construct a default Smiley.
    #   -- Write a test for the   draw   method.
    #   -- Implement and test the remainder of the Smiley constructor
    #      and the   draw   method.
    red = Smiley(window)
    red.start()
    red.draw()

    # TODO: 3. With your instructor:
    #   -- Test the non-default Smiley construction.
    green = Smiley(window, 100, 200, 8, -2, 80, 'green', False)
    green.draw()

    # TODO: 4. With your instructor:
    #   -- Write tests for the methods:  move  start  stop.
    #        Include m1_test_Smiley.scene1() as a test.
    #   -- Implement and test those methods.
    for k in range(20):
        red.move()
        time.sleep(1 / 24)

    # DONE: 5. With your instructor:
    #   -- Write tests for the methods:  frown  smile.
    #   -- Implement and test those methods.

#     green = Smiley(window, color='green')
#     green.draw()
#     for k in range(6):
#         green.frown()
#         time.sleep(0.5)
#         green.smile()
#         time.sleep(0.5)

    # DONE: 6. With your instructor:
    #   -- Write tests for the   collides_with   method.
    #        Include m1_test_Smiley.scene2() .. scene4() as tests.
    #        Note that that file has its own TODO's.
    #   -- Implement and test the   collides_with   method.
#     print(red.collides_with(blue),
#           red.collides_with(green),
#           blue.collides_with(red),
#           blue.collides_with(green),
#           green.collides_with(red),
#           green.collides_with(blue))
    print('The above should be:  False True False False True False')

    m1t_test_Smiley.scene2()
    m1t_test_Smiley.scene3()
    m1t_test_Smiley.scene4()

    # TODO: 7. [OPTIONAL] There is LOTS of other fun things you can do
    #   with this Smiley class. For example: color the eyes, blink the
    #   eyes, implemented a Samantha (from Bewitched) nose,
    #   add lipstick, add eyebrows, and more!
    window.closeOnMouseClick()


class Smiley(object):
    """
    A Smiley is a smiley-face object that can move, detect collisions
    with other Smileys, start and stop moving, and frown/smile.
    Its FIELDS (a.k.a. instance variables) include:
      -- window:        the window in which this Smiley lives
      -- center_point:  center of this smiley
      -- dx, dy:        amount this smiley moves at each step
      -- size:          radius of this smiley
      -- is_smiling:    True if this Smiley is smiling
                          (otherwise this Smiley is frowning)
      -- is_moving:     True if this Smiley is moving, else False
      -- parts:         a list of all the drawable parts of this Smiley
      -- Other fields:  the individual drawable parts of this Smiley:
           head, nose, left_eye, right_eye, mouth_bottom_side,
           mouth_left_side, mouth_right_side
    """
    def __init__(self, window, init_x=None, init_y=None, dx=1, dy=1,
                  size=40, color='red', is_smiling=True):
        # Store the given information in relevant fields:
        # STUDENTS: Make sure you understand each of the following.
        self.window = window
        self.dx = dx
        self.dy = dy
        self.size = size
        self.color = color
        self.is_smiling = is_smiling
        self.is_moving = False

        # Initialize the drawable components:
        if init_x == None:
            init_x = window.getWidth() // 2
        if init_y == None:
            init_y = window.getHeight() // 2

        center = zg.Point(init_x, init_y)

        # Nose:
        self.nose = translated_point(center, 0, 0)

        # Head:
        self.head = zg.Circle(center, size)
        self.head.setFill(color)
        self.head.setWidth(3)

        # Eyes:
        left_center = translated_point(center, -size / 4, -size / 3)
        right_center = translated_point(center, size / 4, -size / 3)
        self.left_eye = zg.Circle(left_center, size / 8)
        self.right_eye = zg.Circle(right_center, size / 8)

        # Mouth, in the smile position:
        bottom_left = translated_point(center, -size / 4, size / 2)
        bottom_right = translated_point(center, size / 4, size / 2)
        top_left = translated_point(center, -size / 4, size / 4)
        top_right = translated_point(center, size / 4, size / 4)

        self.mouth_bottom_side = zg.Line(bottom_left, bottom_right)
        self.mouth_left_side = zg.Line(bottom_left, top_left)
        self.mouth_right_side = zg.Line(bottom_right, top_right)

        # or in the frown position:
        if not is_smiling:
            self.mouth_left_side.move(0, self.size / 4)
            self.mouth_right_side.move(0, self.size / 4)

        # TODO: Collect all drawable parts into a sequence.
        # STUDENTS: Would a list or tuple be better here?
        #           What would be better still?
        self.parts = [self.head, self.nose, self.left_eye, self.right_eye, self.mouth_bottom_side, self.mouth_left_side, self.mouth_right_side]

    # TODO: Implement the unimplemented methods below.  The   scene1
    #   test works with just the constructor, draw and move implemented.
    def draw(self):
        """ Draws this Smiley in its window. """
        for part in self.parts:
            part.draw(self.window)

    def move(self):
        """
        Moves this Smiley (one "step") if it is in the "moving" state.
        It knows how far to move.
        """
        if self.is_moving:
            for part in self.parts:
                part.move(self.dx, self.dy)

    def collides_with(self, other):
        """ Returns: has this Smiley collided with that other one? """

    def start(self):
        """
        Lets this Smiley start moving (so hereafter it moves one "step"
        each time the   move   method is called).
        """
        self.is_moving = True

    def stop(self):
        """
        Stops this Smiley from moving (so hereafter it does NOT move
        even when the   move  method is called).
        """
        self.is_moving = False

    def frown(self):
        """ Changes this Smiley's "facial expression" to a frown. """

    def smile(self):
        """ Changes this Smiley's "facial expression" to a smile. """

    def frown_and_stop(self):
        """
        Makes this Smiley frown and stop.
        Returns 1 if this Smiley had been moving, else returns 0.
        """
        self.frown()
        if self.is_moving:
            self.stop()
            return 1
        else:
            return 0


#-----------------------------------------------------------------------
# Two useful functions (these are NOT Smiley methods).
#-----------------------------------------------------------------------
def translated_point(point, dx, dy):
    """
    Returns a new zg.Point that is a clone of the given zg.Point,
    but translated by the given deltas dx and dy.
    """
    new_point = point.clone()
    new_point.move(dx, dy)
    return new_point


def distance(point1, point2):
    """ Returns the distance between the given point1 and point2. """
    return math.sqrt((point1.getX() - point2.getX()) ** 2 +
                     (point1.getY() - point2.getY()) ** 2)

#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
