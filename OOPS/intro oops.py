# OOPS(OBJECT ORINETED PROGRAMMING)===9TH NOV 2026========================
#=======================================================================================
"""
1. What is OOPS?
OOPS (Object-Oriented Programming System) is a programming approach in which we write programs using classes and objects.

It helps us to organize code, reuse code, and make programs easier to understand and maintain.
--------------------------------------------------------------------------------------------------------------------------------------------

Simple definition:
OOPS is a way of writing programs by grouping data (variables) and functions (methods) together using classes and objects.
2. Real-life example of OOPS

Think about a car.
A car has:
- Properties: Colour, brand, model, speed.
- Behaviours: Start, stop, accelerate, brake.
In Python:
- Properties are represented by variables.
- Behaviours are represented by methods (functions inside a class).
------------------------------------------------------------------------------------------------------------------
3. What is a Class?
A class is a blueprint or template used to create objects.
Example: A car design is a class. It describes what properties and behaviours a car should have.
----------------------------------------------------------------------------------------------------------------------------
4. What is an Object?
An object is an instance of a class.
In simple words:
- Class = Blueprint.
- Object = Real thing created using that blueprint.

----------------------------------------------------------------------------------------------------------------------------------------
5. Four Main Pillars of OOPS
1. Encapsulation
==================
Wrapping data and methods together inside a single class.
Example: A bank account keeps balance and related operations together.

2. Inheritance
=================
One class can acquire the properties and methods of another class.
Example: A child class inherits features from a parent class.

3. Polymorphism
===================
One method or operation can behave in different ways.
Example: The same speak() method can produce different sounds for different animals.

4. Abstraction
=================
Hiding internal implementation details and showing only essential features.
Example: We drive a car using the steering wheel without knowing its internal engine mechanism.

----------------------------------------------------------------------------------------------------------------
6. Why do we use OOPS?
1. Code reusability.
2. Easy to maintain.
3. Better code organization.
4. Reduces code duplication.
5. Makes large projects easier to manage.

------------------------------------------------------------------------------------------------------------------------
7. Important OOPS Terminology                                |
Term         	Meaning                                      |
-------------------------------------------------------------|
Class	      Blueprint of an object                         |
Object	      Instance of a class                            |
Attribute	  Variable inside a class/object                 |
Method	      Function inside a class                        |
Constructor	  Special method used during object creation     |
Inheritance	  Acquiring features from another class          |
self	      Refers to the current object                   |
                                                             |
===============sir.......................==========================================================
> it is a programming concept.
> class: it is a blueprint used to create objects
> object: it is  said to be a instance of the class
# methods: A Method is a function defined inside a class. It is used to perform a particular action or operation on an object.// Simple definition: A method is a function that belongs to a class.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
= it is a programming approach.(concept)
= by using this approach(concept) we organize the code using class and object

# class:
class is a blueprint used to create objects.it has the methods which can exues in the object created

# object:
instance of  a class. it has the data and reperesnt the methods defined in its class

# str(),int(),float(),bool(),list(),tuple(),set(),dict() >> python define this as a class.
name = str("hello")
str → Class
"hello" → String object (instance of str)
name → Variable referencing that object.
----------------------------------------------------------------------------------------------
"hello": can said to be a object of str() >> string object
name : variable refer to the string objcts so it can also said to be string objects
name.<method_name> : methods defined in str() class can executed by its own object.
-------------------------------------------------------------------------------------------------------
Class	str
Object	"hello"
Variable	name

eg: when we add new account in insta tere we are the new object in that and insta as the calss and we as the objects.

==========================================================================================================================================================
CLASS: str = Built-in Python class
||
Methods : upper() · lower() · split() · replace() · strip() · find()
||
Creates an instance = OBJECT: "hello" = Instance of str
||
VARIABLE: name = name = "hello" = References the string object
===============================================================================================================================

int = Class
22 = Object
age = Variable
-------------------------------------------------------------------------------------------------------------------------------------------
self is used to accsess the parameter inside a method(function) if to acces that varibale in other method or any where then we need to use self for that
eg: def ann(self,a,b)
here to acces the a,b we need to call the using self
or like instead of a,b if it was balance and name then it will be like self.balance = balance and self.name = name this way only we can access balance from this method to other or anywhere.


"""

class Student:
    pass
s1 = Student()
# Student → Class
# s1 → Object
# s1 refers to an instance of Student.
#-------------------------------------------------
name = "hello"
age = 22
print(type(age))
print(type(name))
#o/p:
# <class 'int'>
# <class 'str'>