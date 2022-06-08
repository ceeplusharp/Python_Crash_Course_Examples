# Chapter 9: Classes: The Car Class.

import sys


class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"\n{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("\nYou can't roll back an odometer!")
            sys.exit()

    def increment_odometer(self, miles):
        """Add the given amount to odometer reading."""
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("\nYou can't roll back an odometer!")
            sys.exit()


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car2 = Car('toyota', 'vios', 2022)
print(my_new_car2.get_descriptive_name())
my_new_car2.odometer_reading = 23
my_new_car2.read_odometer()

my_new_car3 = Car('honda', 'city', 2021)
print(my_new_car3.get_descriptive_name())
my_new_car3.update_odometer(32)
my_new_car3.read_odometer()

my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(-100)
my_used_car.read_odometer()
