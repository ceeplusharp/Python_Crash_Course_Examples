# Chapter 9: Try it Yourself. 9-13: Dice.

from random import randint


class Dice:
    """A simple take on rolling a dice."""

    def __init__(self, sides=6):
        """To store the class attributes."""
        self.sides = sides

    def roll_die(self):
        """Prints a random number between 1 and the chosen number of sides."""
        print(f"The rolled number is: {randint(1,self.sides)}")


roll = Dice()
roll.roll_die()  # roll 1
roll.roll_die()  # roll 2
roll.roll_die()  # roll 3
roll.roll_die()  # roll 4
roll.roll_die()  # roll 5
roll.roll_die()  # roll 6
roll.roll_die()  # roll 7
roll.roll_die()  # roll 8
roll.roll_die()  # roll 9
roll.roll_die()  # roll 10
