# create a class calculator and define two methodss addition and substraction of 2 numbers

# Creating a class
class Calculator:

    # Addition method
    def addition(self, a, b):
        print("Addition:", a + b)
        # or..........................
        # result = a+b
        # return result

    # Subtraction method
    def subtraction(self, a, b):
        print("Subtraction:", a - b)
        # or..............................
        # result = a-b
        # return result
        

# Creating an object
obj1 = Calculator()

# Calling the methods
obj1.addition(10, 5) # or print(obj1.addition(10, 5))
obj1.subtraction(10, 5) # or or print(obj1.subtraction(10, 5))


#========Calculator using user input==========================================
# Getting input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Creating a class
class Calculator:

    # Addition method
    def addition(self, a, b):
        print("Addition:", a + b)

    # Subtraction method
    def subtraction(self, a, b):
        print("Subtraction:", a - b)

# Creating an object
obj1 = Calculator()

# Calling methods
obj1.addition(num1, num2)
obj1.subtraction(num1, num2)