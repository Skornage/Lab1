"""
An exercise that implements the "Acrobats" role-playing exercise.
See    m3_acrobats   for details.

This is the   Choreographer   class in that exercise.
  -- When a Choreographer is asked to clap or twirl, she chooses two
     Acrobats at random, and asks THEM to clap or twirl the requested
     number of times.  If she is asked to count, she picks two Acrobats
     at random, asks them to count, and returns the sum of the values
     that they return.
     Her random choices can be any Acrobats, including herself.

Authors: Claude Anderson, David Mutchler, Chandan Rupakheti, Matt
         Boutell, Dave Fisher, and Noah Miller.  October 2013.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import m4_BasicAcrobat
import m5_ProudAcrobat
import m6_AcrobatWithBuddy
import m7_DoublingAcrobat

import random


def main():
    """ Calls the   TEST   functions in this module. """
    test_Choreographer()


def test_Choreographer():
    """ Tests the   Choreographer   class. """
    print()
    print('--------------------------------------------------')
    print('Testing the   Choreographer   class:')
    print('--------------------------------------------------')

    frodo = m5_ProudAcrobat.ProudAcrobat('frodo baggins')
    bilbo = m4_BasicAcrobat.BasicAcrobat('bilbo baggins')
    gandalf = Choreographer('gandalf', [frodo, bilbo])

    for _ in range(5):
        print('\nGandalf, clap twice:')
        gandalf.clap(2)

        print('\nGandalf, twirl 3 times:')
        gandalf.twirl(3)

    print(gandalf.count(), bilbo.count(), frodo.count())

    # TODO: Read the above and make sure you
    #   that you understand the statements and how they test this class.


class Choreographer(m4_BasicAcrobat.BasicAcrobat):
    """
    When a Choreographer is asked to clap or twirl, she chooses two
    Acrobats at random, and asks THEM to clap or twirl the requested
    number of times.  If she is asked to count, she picks two Acrobats
    at random, asks them to count, and returns the sum of the values
    that they return.
    When she is constructed, she is given a list of Acrobats, plus she
    has methods by which to add or remove Acrobats from her list.  Her
    random choices can be any Acrobats on that list, including herself.
    """
    def __init__(self, name='NoName', acrobats=[]):
        """
        Sets this Acrobat's list of Acrobats to the given list of
        Acrobats -- that list is the list from which she will choose
        random Acrobats to choreograph.  Adds herself to that list.
        Sets this Acrobat's name to the given name
        (or to the default 'NoName' if no name is given).
        Also initializes other fields as needed.
        """
        # TODO: Read this DONE constructor, make sure you understand it.
        self.acrobats = acrobats
        self.acrobats.append(self)
        super().__init__(name)

    def clap(self, times_told_to_clap):
        """
        Chooses two Acrobats from her list of Acrobats
        and asks each of them to clap the given number of times.
        """
        # TODO: Implement and test this method.
        self.random_acrobat().clap(times_told_to_clap)
        self.random_acrobat().clap(times_told_to_clap)

    def twirl(self, times_told_to_twirl):
        """
        Chooses two Acrobats from her list of Acrobats
        and asks each of them to twirl the given number of times.
        """
        # TODO: Implement and test this method.
        self.random_acrobat().twirl(times_told_to_twirl)
        self.random_acrobat().twirl(times_told_to_twirl)

    def count(self):
        """
        Chooses two Acrobats from her list of Acrobats
        and returns the sum of the numbers that they return to her.
        """
        # TODO: Implement and test this method.
        return self.random_acrobat().count() + self.random_acrobat().count()

    def random_acrobat(self):
        """ Returns a random Acrobat from her list of Acrobats. """
        r = random.randrange(len(self.acrobats))
        return self.acrobats[r]

    def add_acrobats(self, acrobats):
        """ Adds the Acrobats to her list of Acrobats. """
        for acrobat in acrobats:
            if not acrobat in self.acrobats:
                self.acrobats.append(acrobat)

    def remove_acrobats(self, acrobats):
        """ Removes the Acrobats from her list of Acrobats. """
        for acrobat in acrobats:
            if acrobat in self.acrobats:
                self.acrobats.remove(acrobat)

#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
