# Chapter 11: Try It Yourself. 11-03: Employee.


import unittest
from pcc_1103_employee_class import Employee


class TestEmployeeRaise(unittest.TestCase):
    """Tests for the class Employee."""

    def setUp(self):
        """Creates the employee profile."""
        self.employee1 = Employee('Bojack', 'Horseman', 60_000)
        self.employee2 = Employee('Diane', 'Nguyen', 50_000, 10_000)

    def test_give_default_raise(self):
        """Test the given default raise."""
        self.assertEqual(self.employee1.give_raise(), 65_000)

    def test_give_custom_raise(self):
        """Test the given default raise."""
        self.assertEqual(self.employee2.give_raise(), 60_000)


if __name__ == '__main__':
    unittest.main()
