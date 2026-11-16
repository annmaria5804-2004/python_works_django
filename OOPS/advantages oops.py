# Advantages of oops =============12th nov=======================================================
#---------------------------------------------------------------------------------------------------------------
"""
> Four Main Pillars of OOPS
1. Encapsulation
==================
Wrapping data and methods together inside a single class.
Example: A bank account keeps balance and related operations together.
--------sir-----------------------------------------------------------------------

2. Inheritance
=================
One class can acquire the properties and methods of another class.
Example: A child class inherits features from a parent class.
-----------------------------sir-----------------------------------------------------------------
the one class accquire(can reuse) the method and properties from another class without rewritting it.

3. Polymorphism
===================
One method or operation can behave in different ways.
Example: The same speak() method can produce different sounds for different animals.
---------------sir----------------------------------------------------------------------------------------------
4. Abstraction
=================
Hiding internal implementation details and showing only essential features.
Example: We drive a car using the steering wheel without knowing its internal engine mechanism.
------------------sir-------------------------------------------------------------------------------------------------








==================================================================================================================================================================================================================================================================================================
self is used to accsess the parameter inside a method(function) if to acces that varibale in other method or any where then we need to use self for that
eg: def ann(self,a,b)
here to acces the a,b we need to call the using self
or like instead of a,b if it was balance and name then it will be like self.balance = balance and self.name = name this way only we can access balance from this method to other or anywhere.

"""
# this prgm can change using above pillars and make it more simple.
class A:
    def method1(self):
        print("Hello")

    def method2(self):
        print("Hello")


class B:
    def method3(self):
        print("Hello Python")


# Object creation
obj1 = A()
obj2 = B()

# Method calling
obj1.method1()
obj1.method2()
obj2.method3()


"""
               object(class)
        |             |           |
      ------        -------     -------
    |  class    |   | list() |  | tuple() |
    |str(object)|   |        |  |         |


name = "hello"

"""