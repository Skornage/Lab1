"""
Tests the Smiley class by creating and running some "scenes"
that involve moving (and colliding) Smileys.

Authors: Developed by Claude Anderson and revised many times by various
         people including Matt Boutell, Steve Chenoweth, David Mutchler,
         and now Noah Miller.  October 2013.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import m1_Smiley
import zellegraphics as zg
import time


def main():
    """
    Tests the Smiley class by using "scenes"  that involve moving
    (and for scenes 2, 3 and 4, colliding) Smileys.
    """
    # STUDENTS: Can you make sense of the following nifty code?
    scenes = [scene1, scene2, scene3, scene4]
    for scene in scenes:
        scene()


def scene1():
    """ Draws and moves some Smileys.  No collisions yet. """
    window = zg.GraphWin('Scene 1 - Move three smileys 70 steps',
                         400, 400)

    s0 = m1_Smiley.Smiley(window)
    s1 = m1_Smiley.Smiley(window, 50, 50, 2, 2, color='cyan')
    s2 = m1_Smiley.Smiley(window, 330, 130, -5, 2, 60, 'green', False)
    smileys = [s0, s1, s2]

    for smiley in smileys:
        smiley.draw()

    # s0 will not move
    s1.start()
    s2.start()

    times_to_move = 70
    for i in range(times_to_move):  # Animation loop. @UnusedVariable
        for smiley in smileys:  # Loop over all the Smileys.
            smiley.move()
        time.sleep(0.05)

    window.closeOnMouseClick()


def run_collision_scene(window, smileys, steps):
    """
    Moves the Smileys in the given sequence until all have collided.
    When Smileys collide, they stop and frown!
    """
    # This text message gets displayed if all of the Smileys crash.
    message_area = zg.Text(zg.Point(200, 40), "PileUp!!")
    message_area.setSize(30)  # set font size
    message_area.setFace('arial')
    message_area.setStyle('bold')
    message_area.setFill('blue3')

    # TODO: Draw and start 'em all.

    # TODO: Implement the following.
    #   Loop for the given number of steps.
    #   Each time through the loop:
    #     1. Loop through all of the Smileys.  For each Smiley:
    #          a. If it is NOT moving, continue to the next Smiley.
    #          b. Otherwise:
    #               b1. Move the Smiley.
    #               b2. [Do this sub-step by CALLING stop_colliders]
    #                   Loop through all of the OTHER Smileys (SKIPPING
    #                   over the just-moved Smiley).  For each OTHER
    #                   SMILEY, see if the just-moved Smiley and the
    #                   other Smiley have collided.  If so, make both
    #                   of them frown and stop moving.
    #     2. If none of the Smileys are still moving,
    #        BREAK out of the loop.
    #     3. Sleep for a short time (say, 1/24 of a second).
    smileys_moving = len(smileys)

    # Print a closing message.
    if smileys_moving <= 0:  # all smileys have crashed!.
        message_area.draw(window)
    window.closeOnMouseClick()


def stop_colliders(smiley, smileys):
    """
    For each Smiley in the given list of Smileys (argument 2),
    checks whether the given Smiley (argument 1) has collided with it.
    If so, stops and frowns both colliding Smileys.
    Returns the number of newly-stopped Smileys.
    """
    # TODO: Implement this method.


def scene2():
    window = zg.GraphWin('Scene 2 with collisions', 800, 700)
    smileys = (m1_Smiley.Smiley(window, 50, 50, 2, 2),
               m1_Smiley.Smiley(window, 130, 200, 4, 3, 60, 'green'),
               m1_Smiley.Smiley(window, 300, 70, -1, 4, 25, 'orange'),
               m1_Smiley.Smiley(window, 70, 350, 3, 0, 40, 'cyan'),
               )
    run_collision_scene(window, smileys, 150)


def scene3():
    window = zg.GraphWin('Scene 3 with collisions', 800, 700)
    smileys = (m1_Smiley.Smiley(window, 50, 50, 2, 2),
               m1_Smiley.Smiley(window, 130, 200, 4, 3, 60, 'green'),
               m1_Smiley.Smiley(window, 300, 70, -2, 4, 25, 'orange'),
               m1_Smiley.Smiley(window, 70, 350, 3, 0, 40, 'cyan'),
               )
    run_collision_scene(window, smileys, 200)


def scene4():
    window = zg.GraphWin('Scene 4 with collisions', 800, 700)
    smileys = (m1_Smiley.Smiley(window, 50, 50, 2, 2),
               m1_Smiley.Smiley(window, 130, 200, 4, 3, 60, 'green'),
               m1_Smiley.Smiley(window, 300, 70, -1, 5, 25, 'orange'),
               m1_Smiley.Smiley(window, 70, 350, 3, 0, 40, 'cyan'),
               )
    run_collision_scene(window, smileys, 200)

#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
