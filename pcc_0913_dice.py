# Chapter 9: Try it Yourself. 9-13: Dice.

from random import randint


class Dice:
    """A simple take on rolling a dice."""

    def __init__(self, sides=6):
        """To store the class attributes."""
        self.sides = sides

    def roll_die(self):
        """Prints a random number between 1 and the chosen number of sides."""
        i = 0
        while i < 10:
            print(f"The rolled number from the {self.sides}-sided die is: {randint(1,self.sides)}")
            i += 1


# 6-sided die
roll = Dice()
roll.roll_die()

# 10-sided die
roll = Dice(10)
roll.roll_die()

# 20-sided die
roll = Dice(20)
roll.roll_die()
