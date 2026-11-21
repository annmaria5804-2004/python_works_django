# polymorphism
#==================================
"""
Polymorphism in Python
Definition: Polymorphism is an OOP concept that means one name, many forms. 
The same method can perform different actions depending on the object.
=============================================================================================
Concept	                        Meaning
-------------------------------------------------------------------------------------------------------
Inheritance	               Acquiring properties from a parent class
Encapsulation          	   Bundling data and methods together and controlling access
Polymorphism	           One name, many forms
Abstraction	               Hiding implementation details

----------------------------------------------------------------------------------------------------------------------------------------
Method Overloading in Python:
Definition: Method overloading means having multiple methods with the same name but different parameters in the same class.
In Python, traditional method overloading is not directly supported. We can achieve similar behaviour using default arguments or *args.

"""
# overriding=========================================================================
class GooglePay:
    def pay(self):
        print("Payment using Google Pay")

class PhonePe:
    def pay(self):
        print("Payment using PhonePe")

obj1 = GooglePay()
obj2 = PhonePe()

obj1.pay()
obj2.pay()

# 2. Explanation
# 1. GooglePay – First class.
# 2. PhonePe – Second class.
# 3. Both classes have the same method name pay().
# 4. But both methods perform different actions.
# 5. The same method behaves differently depending on the object.
# This is called Polymorphism.
#----------------------------------------------------------------------------
# 3. Real-life example
# Imagine a person who can perform different roles:
# - As a teacher – teaches students.
# - As a student – learns lessons.
# - As a developer – writes code.
# The same person behaves differently depending on the role.

#==================or===========================================================
class A:
    def method1(self):
        print("hai")

class B(A):
    def method1(self):
        print("hello")

obj1 = A()
obj2 = B()

obj1.method1()
obj2.method1()

# Explanation
# 1. A is the parent class.
# 2. B is the child class.
# 3. Both classes have the same method name method1().
# 4. Class B overrides the parent class method.
# 5. When we call the method using different objects, we get different outputs.
# This is called Method Overriding, which is a form of runtime polymorphism.

# overloading====(python not support this only *args is supported)==============================================================
class A:
    def add(self, a, b=0, c=0):
        print(a + b + c)

obj = A()

obj.add(10)
obj.add(10, 20)
obj.add(10, 20, 30)

# add() is a method.
# First call: passes 1 argument.
# Second call: passes 2 arguments.
# Third call: passes 3 arguments.
# The same method performs different operations depending on the number of arguments.

#3. Another example using *args
class A:
    def add(self, *args):
        print(sum(args))

obj = A()

obj.add(10, 20)
obj.add(10, 20, 30)
obj.add(10, 20, 30, 40)

# Overloading	                                                    Overriding
# -------------------------------------------------------------------------------------------------------------
# Same method name with different parameters	           Same method name in parent and child classes
# Usually within the same class                            Requires inheritance
# Python uses workarounds like default arguments	       Directly supported in Python