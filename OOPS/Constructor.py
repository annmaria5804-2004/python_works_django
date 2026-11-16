# # constructor 10th nov 2026=====================
# =======================================================================================
"""
Let's continue your Python learning notes for Constructors (__init__).
Constructor in Python
A constructor is a special method that is automatically called when an object of a class is created.
- It is used to initialize object attributes.
- It is called automatically when creating an object.
- In Python, the constructor method is __init__().
- It does not need to be called manually.
-----------------------------------------------------------------------------------------------------------------------
# syntax:
class ClassName:
    def __init__(self):
        # initialization statements
obj = ClassName()
-----------------------------------------------------------------------------------------------------------------------------------------
Types of Constructors
1. Default constructor: A constructor that does not accept any arguments other than self (when provided by the programmer).
2. Parameterized constructor: A constructor that accepts parameters to initialize object attributes.
-------------------------------------------------------------------------------------------------------------------------------------------------
Difference between normal method and constructor:
Constructor              	                               Normal method
-------------------------------------------------  |    ---------------------------------------
__init__()	                                       |     User-defined method name
Called automatically during object creation	       |      Called manually
Initializes object attributes	                   |     Performs specific operations
Usually called once during object initialization   |     Can be called multiple times

"""
# Example 1 – Constructor without parameters
class Student:
    def __init__(self):
        print("Constructor called")
        print("Student object created")

obj = Student()
# o/p:
# Constructor called
# Student object created

# Example 2 – Constructor with parameters
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

obj = Student("Ann", 22)
obj.display()
# o/p:
#Name: Ann
# Age: 22

# Example 3 – Multiple objects
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(self.name, self.salary)

emp1 = Employee("Anu", 25000)
emp2 = Employee("Miya", 30000)

emp1.display()
emp2.display()
# o/p:
# Anu 25000
# Miya 30000