"""
An exercise that implements the "Acrobats" role-playing exercise.
See    m3_acrobats   for details.

This is the   ProudAcrobat   class in that exercise.
  -- A ProudAcrobat extends a BasicAcrobat; it adds the 'bow' operation.

Authors: Claude Anderson, David Mutchler, Chandan Rupakheti, Matt
         Boutell, Dave Fisher, and Noah Miller.  October 2013.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import m4_BasicAcrobat


def main():
    """ Calls the   TEST   functions in this module. """
    test_ProudAcrobat()


def test_ProudAcrobat():
    """ Tests the   ProudAcrobat   class. """
    print()
    print('--------------------------------------------------')
    print('Testing the   ProudAcrobat   class:')
    print('--------------------------------------------------')

    bilbo = ProudAcrobat('bilbo baggins')
    frodo = ProudAcrobat('frodo baggins')
    nobody = ProudAcrobat()

    bilbo.clap(3)
    frodo.twirl(2)
    bilbo.twirl(5)
    print(bilbo.count(), frodo.count(), nobody.count())

    bilbo.bow()
    nobody.bow()
    nobody.clap(1)
    print(bilbo.count(), frodo.count(), nobody.count())
    # TODO: With your instructor, read the above and make sure you
    #   that you understand the statements and how they test this class.


class ProudAcrobat(m4_BasicAcrobat.BasicAcrobat):
    """
    A ProudAcrobat extends a BasicAcrobat; it adds the 'bow' operation.
    """
    def __init__(self, name='NoName'):
        """
        Sets this Acrobat's name to the given name
        (or to the default 'NoName' if no name is given).
        Also initializes other fields as needed.
        """

        # TODO: With your instructor, read the following and make sure
        #   that you understand it -- WHAT it does, the NOTATION for it,
        #   and WHY it is needed.
        super().__init__(name)

    def bow(self):
        """
        Says 'Thank you.' and then bows.
        """
        # TODO: With your instructor, read the following and make sure
        #   that you understand it -- how it AUGMENTS what a
        #   BasicAcrobat can do.
        print('Thank you.')
        print(self.name, 'bows.')

    def clap(self, times_told_to_clap):
        """
        Claps the given number of times, then bows.
        """
        # TODO: With your instructor, read the following and make sure
        #   that you understand it -- WHAT it does, the NOTATION for it,
        #   and WHY it is needed.
        super().clap(times_told_to_clap)
        self.bow()

    def twirl(self, times_told_to_twirl):
        """
        Twirls the given number of times, then bows.
        """
        super().twirl(times_told_to_twirl)
        self.bow()

        # TODO: Implement and test this method.

    # TODO: Write here (in a comment)
    #       why there is NOT a   count  method defined in this class.
    # A ProudAcrobat's count is the same as the BasicAcrobat's count.

#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
