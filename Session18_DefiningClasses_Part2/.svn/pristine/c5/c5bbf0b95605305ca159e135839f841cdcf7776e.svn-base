"""
An exercise that implements the "Acrobats" role-playing exercise
for demonstrating various Object-Oriented Programming (OOP) and other
concepts, including:
  -- Classes (BasicAcrobat, ProudAcrobat, ...)
  -- Objects (proudAcrobat1, proudAcrobat2, ...)
       -- that is, Instances of the classes
  -- Methods (the operations clap, twirl, count, ...)
  -- Arguments:  clap(2)
  -- Returned values: from count
  -- Encapsulation in classes and in methods
  -- Fields, internal state -- each object:
       -- Has a name
       -- Keeps track of how many operations it has performed
  -- Inheritance, IS-A (e.g., ProudAcrobat is-a BasicAcrobat)
  -- Associations, HAS-A (e.g., an AcrobatWithBuddy has-a Acrobat)
  -- Implementing to an interface / duck typing
       -- Acrobats can clap, twirl and count
  -- Exceptions (which Curmudgeons might handle)
  -- UML class diagrams (that show relationships between classes)

This is the   main   file of that exercise, that constructs and uses
various acrobats.  Each class has its own file:
  -- BasicAcrobat
  -- ProudAcrobat
  -- AcrobatWithBuddy
  -- DoublingAcrobat
  -- Choreographer
  -- Curmudgeon (who does nothing other than say "I refuse!")

This exercise is adapted from Joe Bergin's page at:
   http://csis.pace.edu/~bergin/Java/RolePlay.html
that describes an idea presented by Steven K. Andrianoff
and David B. Levine at SIGCSE-2002.

Authors: Claude Anderson, David Mutchler, Chandan Rupakheti, Matt
         Boutell, Dave Fisher, and their colleagues.  October 2013.
"""

#-----------------------------------------------------------------------
# Students: Read and run this program, to see the Acrobats in action!
#-----------------------------------------------------------------------

from m4_BasicAcrobat import BasicAcrobat
from m5_ProudAcrobat import ProudAcrobat
from m6_AcrobatWithBuddy import AcrobatWithBuddy
from m7_DoublingAcrobat import DoublingAcrobat
from m8_Choreographer import Choreographer
from m9_Curmudgeon import Curmudgeon


def main():
    """ Demonstrates acrobats of various types (classes). """
    # Construct Acrobats.
    carla = BasicAcrobat('Carla Wallenda')
    herman = BasicAcrobat('Herman Wallenda')
    joseph = BasicAcrobat('Joseph Geiger')

    helen = ProudAcrobat('Helen Kreis')
    cathy = ProudAcrobat('Cathy Rigby')

    bellos_full_name = 'Demetrius Alexandro Claudio Amadeus Bello Nock'
    bello = AcrobatWithBuddy(cathy, bellos_full_name)
    nik = AcrobatWithBuddy(bello, 'Nik Wallenda')

    rietta = DoublingAcrobat('Rietta Wallenda')

    karl = Choreographer('Karl Wallenda')
    raymond = Choreographer('Raymond Chitty')

    oscar = Curmudgeon('Oscar the Grouch')

    acrobats = [carla, herman, joseph, helen, cathy, bello, nik,
                rietta, karl, raymond]  # All but oscar
    karl.add_acrobats(acrobats)
    raymond.add_acrobats(acrobats)

    # Ask Acrobats to do things.
    # Basic Acrobats:
    carla.clap(2)
    herman.twirl(1)
    carla.twirl(2)
    x = carla.count()
    print(carla.name, 'has done', x,
          'operations (count, twirl, ...) so far')
    x = joseph.count()
    print(joseph.name, 'has done', x,
          'operations (count, twirl, ...) so far')

    # Proud Acrobats:
    helen.clap(3)
    cathy.twirl(1)
    helen.bow()

    # Curmudgeon:
    oscar.twirl(3)
    oscar.clap(3)

    # Acrobats with Buddies:
    bello.clap(4)
    bello.clap(2)
    bello.twirl(1)
    bello.display_your_buddy()

    nik.display_your_buddy()
    nik.clap(3)
    x = nik.count()
    print(nik.name, 'has done', x,
          'operations (count, twirl, ...) so far')

    bello.twirl(1)
    bello.display_your_buddy()
    nik.display_your_buddy()

    # Doubling Acrobat:
    rietta.clap(3)
    x = rietta.count()
    print(rietta.name, 'has done', x,
          'operations (count, twirl, ...) so far')
#     rietta.twirl(100)  # just kidding!

    # Choreographers:
    karl.clap(3)
    karl.clap(3)
    raymond.clap(2)
    x = karl.count()
    print(karl.name, 'has done', x,
          'operations (count, twirl, ...) so far')

    # Basic Acrobat again (to show that she has not forgotten her state)
    x = carla.count()
    print(carla.name, 'has done', x,
          'operations (count, twirl, ...) so far')
    # CONSIDER:  What goes wrong if you execute the commented-out
    #               b.clap(1)    below?
    a = AcrobatWithBuddy(None, 'Acrobat 1')
    b = AcrobatWithBuddy(a, 'Acrobat 2')
    a.buddy = b  # Bad on many levels!
#     b.clap(1)

#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
