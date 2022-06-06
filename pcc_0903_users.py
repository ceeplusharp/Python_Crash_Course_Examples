# Chapter 9: Try it Yourself. 9-3: Users.

class Users:
    """Collects the user's first and last names, city and age."""

    def __init__(self, first_name, last_name, city, age):
        """To store the user's attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.age = age

    def describe_user(self):
        """Prints the user's information."""
        print(f"\nFull Name: {self.first_name} {self.last_name}")
        print(f"City: {self.city}")
        print(f"Age: {self.age}")

    def greet_user(self):
        """Prints a personalized greeting to the user."""
        print(f"Welcome, {self.first_name} {self.last_name}!")


user1 = Users('Juan', 'Dela Cruz', 'Metro Manila', 31)
user1.describe_user()
user1.greet_user()

user2 = Users('Juana', 'Dela Cruz', 'Antipolo City', 26)
user2.describe_user()
user2.greet_user()

user3 = Users('Maria', 'Dela Cruz', 'Marikina City', 28)
user3.describe_user()
user3.greet_user()
