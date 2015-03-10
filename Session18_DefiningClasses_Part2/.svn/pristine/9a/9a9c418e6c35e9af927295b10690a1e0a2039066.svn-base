"""
An exercise that implements the "Acrobats" role-playing exercise.
See    m3_acrobats   for details.

This is the   BasicAcrobat   class in that exercise.
  -- A Basic Acrobat can clap, twirl and count.

Authors: Claude Anderson, David Mutchler, Chandan Rupakheti, Matt
         Boutell, Dave Fisher, and Noah Miller.  October 2013.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
    test_BasicAcrobat()


def test_BasicAcrobat():
    """ Tests the   BasicAcrobat   class. """
    print()
    print('--------------------------------------------------')
    print('Testing the   BasicAcrobat   class:')
    print('--------------------------------------------------')

    bilbo = BasicAcrobat('bilbo baggins')
    frodo = BasicAcrobat('frodo baggins')
    nobody = BasicAcrobat()

    bilbo.clap(3)
    frodo.twirl(2)
    bilbo.twirl(5)
    print(bilbo.count(), frodo.count(), nobody.count())

    # TODO: With your instructor, read the above and make sure you
    #   that you understand the statements and how they test this class.
    #   Then add statement(s) that test whether the default naming
    #   (per nobody, defined above) works correctly.
    nob = BasicAcrobat()
    nob.twirl(2)
    print(nob.count())

class BasicAcrobat(object):
    """
    A BasicAcrobat can clap, twirl and count.
    """
    def __init__(self, name='NoName'):
        """
        Sets this Acrobat's name to the given name
        (or to the default 'NoName' if no name is given).
        Also initializes the number of operations to 0.
        """
        # TODO: With your instructor, initialize the fields correctly
        #   (the code begins with WRONG stubs).
        self.name = name
        self.number_of_operations = 0

    def clap(self, times_told_to_clap):
        """
        Claps the given number of times.
        """

        # TODO: Read the following implementation of this method and
        #   make sure that you understand it.  ASK QUESTIONS as needed!
        for k in range(times_told_to_clap):  # @UnusedVariable
            print(self.name, 'claps.')
        self.number_of_operations += times_told_to_clap

    def twirl(self, times_told_to_twirl):
        """
        Twirls the given number of times.
        """
        for k in range(times_told_to_twirl):
            print(self.name, 'twirls')
        self.number_of_operations += times_told_to_twirl

        # TODO: With your instructor, implement and test this method.

    def count(self):
        return self.number_of_operations
        """
        Returns the number of operations (claps, twirls, etc)
        that have been performed so far.
        """
        # TODO: With your instructor, implement and test this method.

#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
