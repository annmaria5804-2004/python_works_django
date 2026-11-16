# create a class named employe and 
# method1 : baasic with values name,slary
# method2 : display name, basic salary , hra

class Employee:

    def basic(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        hra = self.salary * 0.20

        print("Employee Name:", self.name)
        print("Basic Salary:", self.salary)
        print("HRA:", hra)


# Object creation
obj = Employee()

# Method calling
obj.basic("Ann", 25000)
obj.display()

# Employee Name: Ann
# Basic Salary: 25000
# HRA: 5000.0

# Easy explanation
# Method 1: basic()
# - Accepts employee name and salary.
# - self.name stores the employee name.
# - self.salary stores the basic salary.
# Method 2: display()
# - Displays employee name.
# - Displays basic salary.
# - Calculates and displays HRA.
# HRA calculation
# Here, we assume HRA is 20% of basic salary.
# HRA = Basic\ Salary \times \frac{20}{100}
# For example:
# 25000 × 20 / 100 = 5000

# Remember:
# - self is used to access object variables.
# - self.name and self.salary store values.
# - obj.basic() calls the first method.
# - obj.display() calls the second method.