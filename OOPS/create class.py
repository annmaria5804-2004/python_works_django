# create a class by user sample and define a single method
class sample(): # blue print or class named sample
    def greet(self): # method inside class means func are called as method inside a class and when method comesm inside a class we must use self 
       print("hello ann") 

# creat a object
obj1 = sample()
obj1.greet() # Calling the method using the object

# Code	Explanation
# class sample():	Creates a user-defined class
# def greet(self):	Defines an instance method
# self	Refers to the current object
# print("hello ann")	Statement inside the method
# obj1 = sample()	Creates an object
# obj1.greet()	Calls the method

#or 2 object==============================================================================================\
class Sample:
    def greet(self):
        print("Hello Ann")

obj1 = Sample()
obj2 = Sample()

obj1.greet()
obj2.greet()
#o/p:
# Hello Ann
# Hello Ann

# ==============chatgpt====================================================================================
class Student:

    # Creating a method
    def display(self):
        print("Hello, Welcome to Python OOPS")

# Creating an object
s1 = Student()
# Calling the method
s1.display() # Hello, Welcome to Python OOPS

# Explanation
# 1. class Student: – Creates a user-defined class.
# 2. def display(self): – Defines a method inside the class.
# 3. self – Refers to the current object.
# 4. s1 = Student() – Creates an object of the Student class.
# 5. s1.display() – Calls the method using the object.