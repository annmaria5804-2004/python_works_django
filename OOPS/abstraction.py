"""
What is Abstraction in Python?
Abstraction is an OOP (Object-Oriented Programming) concept that hides the internal implementation details and shows only the essential features to the user.
In simple words, we show what an object does, not how it does it.

Real-life example:
When you use an ATM:
- You enter your PIN.
- You select an amount.
- You withdraw money.
You don't need to know how the ATM internally processes the transaction. This is abstraction.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Important points for interviews
1. Abstraction hides implementation details.
2. It shows only essential information.
3. Python supports abstraction using the abc module.
4. Abstract classes cannot be instantiated directly.
5. Abstract methods must be implemented by child classes.
Short interview answer
"Abstraction is an OOP concept that hides the internal implementation details and displays only the necessary information to the user. In Python, we achieve abstraction using abstract classes and abstract methods from the ABC module."

Remember the difference:
- Abstraction: Hiding implementation details.
- Encapsulation: Hiding and protecting data using classes and access control.

"""
# Python Example
# Python uses the abc module to achieve abstraction.
from abc import ABC, abstractmethod # ABC – Used to create an abstract class.abstractmethod – Used to define an abstract method.

class Animal(ABC):
    @abstractmethod # @abstractmethod makes sound() an abstract method.
    def sound(self):
        pass # pass means the method has no implementation here.

class Dog(Animal): # Dog inherits from Animal.
    def sound(self):
        print("Dog barks")
obj = Dog()
obj.sound()

# Example: In your code:
# - Animal is the abstract class.
# - sound() is the abstract method.
# - Dog inherits the Animal class.
# - Dog implements the sound() method.

#==========next=====================================================================================

from abc import ABC, abstractmethod

class Payment(ABC):
    def payment_details(self, amount):
        print("Payment started")
        print("The amount is:", amount)
        
    @abstractmethod
    def pay(self, amount):
        pass

class GooglePay(Payment):
    def pay(self, amount):
        self.payment_details(amount) # calls the normal method from the parent class.
        print("Payment successful using Google Pay")

class phonepe(Payment):
    def pay(self,amount):
        print("paid using phonepe pay")
        
obj1 = GooglePay()
obj1.pay(2000)

obj2 = phonepe()
obj2.pay(3000)

# Simple explanation
# 1. Payment – Abstract parent class.
# 2. payment_details() – Normal method.
# 3. pay() – Abstract method.
# 4. GooglePay – Child class.
# 5. pay() – Implements the abstract 

#---------------------------------------------
# You are creating two objects, but assigning both to the same variable obj.
# - First, obj = phonepe() creates a PhonePe object.
# - Next, obj = GooglePay() replaces that reference with a GooglePay object.
# - Finally, obj.pay(2000) calls the GooglePay method.
# Important: Both GooglePay and PhonePe must implement the abstract pay() method. 
# Otherwise, Python will not allow you to create their objects.