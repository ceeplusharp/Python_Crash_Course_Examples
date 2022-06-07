# Chapter 9: Try it Yourself. 9-6: Ice Cream Stand.

class Restaurant:
    """A simple restaurant with its offered cuisine."""

    def __init__(self, restaurant_name, cuisine_type):
        """To store the restaurant name and cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Displays the restaurant name and offered cuisine."""
        print(f"\nThe restaurant {self.restaurant_name} offers {self.cuisine_type}.")

    def open_restaurant(self):
        """Displays that the restaurant is open."""
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self):
        """Sets the number of customers that have been served."""
        print(f"\n{self.number_served} customers have been served.")

    def increment_number_served(self, num_served):
        """Increments the number of customers who have been served."""
        self.number_served += num_served
        print(f"\n{self.number_served} customers have been served for today.")


class IceCreamStand(Restaurant):
    """A specific kind of restaurant for selling Ice Creams."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes of the parent class.
        Then initialize attributes specific to Electric Cars."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors_list = []

    def icecream_flavors(self, flavors):
        """Store and print ice cream flavors."""
        self.flavors_list.append(flavors)
        print(f"\nThese are the served ice cream flavors: {self.flavors_list}")


icecream_stand1 = IceCreamStand('Cold Stone', 'Ice Cream')

icecream_stand1.describe_restaurant()
icecream_stand1.open_restaurant()

icecream_stand1.icecream_flavors('Strawberry')
icecream_stand1.icecream_flavors('Choco Mint')
icecream_stand1.icecream_flavors('Avocado')