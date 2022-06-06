# Chapter 9: Try it Yourself. 9-4: Number Served.

class Restaurant:
    """A simple restaurant with its offered cuisine."""

    def __init__(self, restaurant_name, cuisine_type):
        """To store the restaurant name and cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Displays the restaurant name and offered cuisine."""
        print(f"\nThe restaurant {self.restaurant_name} offers {self.cuisine_type} cuisines.")

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


restaurant = Restaurant('Yabu', 'Japanese')

restaurant.describe_restaurant()
restaurant.open_restaurant()

print(restaurant.number_served)
restaurant.number_served = 5
print(restaurant.number_served)

restaurant.number_served = 7
restaurant.set_number_served()

restaurant.increment_number_served(50)