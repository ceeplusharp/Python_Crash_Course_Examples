# Chapter 9: Try it Yourself. 9-5: Login Attempts.

class Users:
    """Collects the user's first and last names, city and age."""

    def __init__(self, first_name, last_name, city, age):
        """To store the user's attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        """Prints the user's information."""
        print(f"\nFull Name: {self.first_name} {self.last_name}")
        print(f"City: {self.city}")
        print(f"Age: {self.age}")

    def greet_user(self):
        """Prints a personalized greeting to the user."""
        print(f"Welcome, {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        """Increments the value of login_attempts by 1."""
        self.login_attempts = self.login_attempts + 1
        print(f"Current login attempts: {self.login_attempts}")

    def reset_login_attempts(self):
        """Resets the value of login_attempts to 0."""
        self.login_attempts = 0
        print(f"Current login attempts: {self.login_attempts}")


user1 = Users('Kaycee', 'Candelaria', 'Pasig City', 27)
user1.describe_user()
user1.greet_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.reset_login_attempts()
