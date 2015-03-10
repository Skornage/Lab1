"""
An exercise that implements the "Acrobats" role-playing exercise.
See    m3_acrobats   for details.

This is the   Curmudgeon   class in that exercise.
  -- A Curmudgeon always says 'I refuse' (in response to ANY request).

Authors: Claude Anderson, David Mutchler, Chandan Rupakheti, Matt
         Boutell, Dave Fisher, and Noah Miller.  October 2013.
"""  # DONE.  Nothing to do in here.


def main():
    """ Calls the   TEST   functions in this module. """
    test_Curmudgeon()


def test_Curmudgeon():
    """ Tests the   Curmudgeon   class. """
    print()
    print('--------------------------------------------------')
    print('Testing the   Curmudgeon   class:')
    print('--------------------------------------------------')

    bilbo = Curmudgeon('bilbo baggins')
    frodo = Curmudgeon('frodo baggins')

    bilbo.clap(3)
    frodo.twirl(2)
    bilbo.twirl(5)
    print(bilbo.count(), frodo.count())
    frodo.twirl(4)
    print(bilbo.count(), frodo.count())


class Curmudgeon(object):
    """
    A Curmudgeon always says 'I refuse!'
    """
    def __init__(self, name='NoName'):
        """
        Sets this Acrobat's name to the given name
        (or to the default 'NoName' if no name is given).
        """
        self.name = name

    def clap(self, times_told_to_clap):
        """ Refuses to clap. """
        self.refuse()

    def twirl(self, times_told_to_twirl):
        """ Refuses to twirl. """
        self.refuse()

    def count(self):
        """ Refuses to count. """
        self.refuse()

    def refuse(self):
        """ Indicates that she refuses! """
        print('I refuse!')

#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()