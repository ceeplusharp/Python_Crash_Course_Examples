# Chapter 9: Try it Yourself. 9-10: Imported Restaurant.

"""A class for describing restaurants and offered cuisines."""


class Restaurant:
    """A simple restaurant with its offered cuisine."""

    def __init__(self, restaurant_name, cuisine_type):
        """To store the restaurant name and cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Displays the restaurant name and offered cuisine."""
        print(f"\nThe restaurant {self.restaurant_name} offers {self.cuisine_type} cuisines.")

    def open_restaurant(self):
        """Displays that the restaurant is open."""
        print(f"{self.restaurant_name} is now open!")
