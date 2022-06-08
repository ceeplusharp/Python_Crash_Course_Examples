# Chapter 9: Try it Yourself. 9-12: Multiple Modules.

from pcc_0912_module_users import Users


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
