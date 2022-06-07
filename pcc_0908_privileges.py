# Chapter 9: Try it Yourself. 9-8: Privileges.

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


class Privileges1:
    """Stores the list of privileges."""

    def __init__(self, privileged1=''):
        """Initialize the class attributes."""
        self.privileged1 = privileged1
        self.privileges_list = []

    def show_privileges1(self, privileged1):
        """Store and print admin user privileges."""
        self.privileges_list.append(privileged1)
        print(f"These are the Admin User's Privileges: {self.privileges_list}")


class Admin(Users):
    """Specific for Admin Users only."""

    def __init__(self, first_name, last_name, city, age):
        """Initialize attributes of the parent class.
        Then initialize attributes specific to Admin Users."""
        super().__init__(first_name, last_name, city, age)
        self.privileges = []
        self.privileges1 = Privileges1()

    def show_privileges(self, privilege):
        """Store and print admin user privileges."""
        self.privileges.append(privilege)
        print(f"These are the Admin User's Privileges: {self.privileges}")


# Output using Child Class Admin
admin1 = Admin('Princess', 'Carolyn', 'Hollywoo', 26)

admin1.describe_user()
admin1.greet_user()

admin1.show_privileges('can add post')
admin1.show_privileges('can delete post')
admin1.show_privileges('can ban user')

# Output using Child Class Admin and New Class Privileges1
admin2 = Admin('Dianne', 'Nguyen', 'Boston', 32)

admin2.describe_user()
admin2.greet_user()

admin2.privileges1.show_privileges1('can add post')
admin2.privileges1.show_privileges1('can delete post')
admin2.privileges1.show_privileges1('can ban user')
