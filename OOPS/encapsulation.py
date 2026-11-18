# encapsulation============================
#---------------------------------------------------------
"""
Encapsulation in Python
Definition: Encapsulation is an OOP concept that combines data (variables) and methods (functions) into a single unit (class) and restricts direct access to some data.

In simple words: Wrapping data and methods together and protecting the data from direct access.
====================================================================================================================

3. Types of access modifiers in Python
Type	Syntax	Meaning
Public	name	Accessible from anywhere
Protected	_name	Intended for internal use and subclasses
Private	__name	Name-mangled to discourage direct access

4. Interview questions
Q1. What is encapsulation?

Encapsulation is wrapping data and methods into a single unit and restricting direct access to data.

Q2. How do you achieve encapsulation in Python?

Using classes and access conventions such as public, protected and private attributes.

Q3. What is a private variable?

A variable declared using double underscores (__) that undergoes name mangling in Python.
Short interview answer
"Encapsulation is an OOP concept that combines variables and methods inside a class and protects data from direct access. In Python, we can use private variables with double underscores."

Remember all four OOP concepts:
- Inheritance – Acquiring properties from a parent class.
- Polymorphism – One name, many forms.
- Abstraction – Hiding implementation details.
- Encapsulation – Wrapping data and methods together and controlling access.




"""
class Bank:
    def __init__(self):
        self.__balance = 5000

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited:", amount)

    def display(self):
        print("Balance:", self.__balance)


obj = Bank()
obj.deposit(1000)
obj.display()