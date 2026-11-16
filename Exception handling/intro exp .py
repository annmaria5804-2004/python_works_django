# Exception handling======================================2/11/2026==========================
#---------------------------------------------------------------------------------------------------------------
"""
1. What is Exception Handling?
An exception is an error that occurs while a program is running.


For example:
- Dividing a number by zero.
- Entering text instead of a number.
- Accessing an index that doesn't exist.
- Using an undefined variable.

Explanation:
Keyword	Meaning
try >	Contains code that may cause an error.
except >	Handles the error if it occurs.
else > Executes if no exception occurs.
finally > 	Executes whether an exception occurs or not.


3. Different types of exceptions
Exception >	When does it occur?
ZeroDivisionError >	Dividing by zero
ValueError >	Invalid value conversion
TypeError >	Performing an operation on incompatible data types
IndexError >	Accessing an invalid list index
KeyError >	Accessing a dictionary key that doesn't exist
NameError >	Using an undefined variable
FileNotFoundError >	Opening a file that doesn't exist


basic structure syntax:
================================================
try:
    # Risky code

except ExceptionType:
    # Error handling

else:
    # Executes if no error

finally:
    # Always executes

sir=======================================================
= techincques used to handle the runtime errors intsed of crashing the execution
= for 1 try we can use more than one expect means countlesss expect...










"""
num1= int(input("enter the num1: ")) # if 1
num2= int(input("enter the num2: ")) # if 0
result = num1/num2 # not defined as 1/0 is  as not defined form
print(result) # o/p: ZeroDivisionError: division by zero
print("thank you") # this also not execute because above there is error so there it will end

# so---------------------------------------------------------new way ------------------------------------
# 2. How to handle this error using try and except
# We use try and except to handle errors without stopping the entire program unexpectedly.
num1 = int(input("Enter the num1: "))
num2 = int(input("Enter the num2: "))

try:
    result = num1 / num2
    print(result)

except ZeroDivisionError:
    print("Cannot divide by zero")

print("Thank you") # o/p: Cannot divide by zero | Thank you

# 4. Example using multiple except blocks
try:
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))

    result = num1 / num2
    print(result)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Please enter numbers only")

print("Thank you")

# Here:
# - If you enter 10 and 0 → ZeroDivisionError.
# - If you enter hello → ValueError.
# - If no error occurs → Result will be printed.

# 5. Using else and finally
try:
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))

    result = num1 / num2

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input")

else:
    print("Result:", result)

finally:
    print("Thank you")
    
# Remember:
# - try → Try the code.
# - except → Handle the error.
# - else → Run if there is no error.
# - finally → Always execute.

# ============================================================================
# raise------------------------------------------------------------------------------------
# used to manually gernate the expection(error) when a specific condtion is met in a prgm
age = int(input("enter the age : "))
if age <=17:
    raise ValueError("something went wrrong") #    raise ValueError("something went wrrong")
#or
    raise Exception("something went wrrong")
else:
    print("you are eligible")