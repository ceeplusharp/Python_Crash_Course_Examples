# Chapter 11: Try It Yourself. 11-03: Employee.


class Employee:
    """Collect employee's full name and salary details."""

    def __init__(self, first_name, last_name, annual_salary, salary_raise=0):
        """Store each required attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = int(annual_salary)
        self.salary_raise = int(salary_raise)
        self.final_salary = ''

    def give_raise(self):
        """Gives a raise to the employee."""
        if self.salary_raise == 0:
            self.final_salary = self.annual_salary + 5000
            print(f"Salary after Annual Raise: ${self.final_salary}")
            # print(f"\nEmployee: {self.first_name} {self.last_name}"
            #       f"\nAnnual Salary: ${self.annual_salary}"
            #       f"\nSalary after Annual Raise: ${self.annual_salary + 5_000}")
        else:
            self.final_salary = self.annual_salary + self.salary_raise
            print(f"Salary after Desired Raise: ${self.final_salary}")
            # print(f"\nEmployee: {self.first_name} {self.last_name}"
            #       f"\nAnnual Salary: ${self.annual_salary}"
            #       f"\nSalary after Desired Raise: ${self.annual_salary + self.salary_raise}")


employee1 = Employee('Bojack', 'Horseman', 60_000)
employee1.give_raise()

employee2 = Employee('Dianne', 'Nguyen', 50_000, 10_000)
employee2.give_raise()
