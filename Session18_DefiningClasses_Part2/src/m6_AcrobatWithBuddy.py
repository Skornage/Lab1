"""
An exercise that implements the "Acrobats" role-playing exercise.
See    m3_acrobats   for details.

This is the   AcrobatWithBuddy   class in that exercise.
  -- An AcrobatWithBuddy can clap, twirl and count,
     like a BasicAcrobat, but she also has a Buddy (another Acrobat).
     When she claps or twirls, she asks her Buddy to do the same.
     When she counts, she returns her Buddy's count added to her own.
     Also, she can display the name of her Buddy.

Authors: Claude Anderson, David Mutchler, Chandan Rupakheti, Matt
         Boutell, Dave Fisher, and Noah Miller.  October 2013.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import m4_BasicAcrobat


def main():
    """ Calls the   TEST   functions in this module. """
    test_AcrobatWithBuddy()


def test_AcrobatWithBuddy():
    """ Tests the   AcrobatWithBuddy   class. """
    print()
    print('--------------------------------------------------')
    print('Testing the   AcrobatWithBuddy   class:')
    print('--------------------------------------------------')
    # TODO: With your instructor, implement some tests.
    #   You will need a Basic Acrobat (already done).
    # CONSIDER: Can an AcrobatWithBuddy have another AcrobatWithBuddy
    #           as her buddy?
    frodo = m4_BasicAcrobat.BasicAcrobat('frodo baggins')
    bilbo = AcrobatWithBuddy(frodo, 'bilbo')
    bilbo.clap(5)
    bilbo.twirl(2)
    print(bilbo.count(), frodo.count())

class AcrobatWithBuddy(m4_BasicAcrobat.BasicAcrobat):
    """
    A BasicAcrobat can clap, twirl and count.
    """
    def __init__(self, buddy, name='NoName'):
        """
        Sets this Acrobat's buddy to the given buddy (which must be
        another Acrobat).  Sets this Acrobat's name to the given name
        (or to the default 'NoName' if no name is given).
        Also initializes other fields as needed.
        """
        # TODO: With your instructor,
        #   implement the rest of this constructor.
        self.buddy = buddy
        super().__init__(name)

    def clap(self, times_told_to_clap):
        """
        Claps the given number of times,
        then passes the same instruction to her buddy.
        """
        # TODO: With your instructor, implement and test this method.
        super().clap(times_told_to_clap)
        self.buddy.clap(times_told_to_clap)

    def twirl(self, times_told_to_twirl):
        """
        Twirls the given number of times,
        then passes the same instruction to her buddy.
        """
        # TODO: With your instructor, implement and test this method.
        super().twirl(times_told_to_twirl)
        self.buddy.twirl(times_told_to_twirl)

    def count(self):
        """
        Returns the number of operations (claps, twirls, etc) that have
        been performed so far, by her AND her buddies combined.
        """
        # TODO: With your instructor, implement and test this method.
        return super().count() + self.buddy.count()

    def display_your_buddy(self):
        """ Displays the name of this Acrobat's buddy. """
        print(self.name, 'has buddy', self.buddy.name)

#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
