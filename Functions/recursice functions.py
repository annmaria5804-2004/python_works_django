# return the factorial of the number enter by user
def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i #(fact *= i)
    return fact

num = int(input("Enter a number: "))
print("Factorial =", factorial(num))

# Easy explanation
# 1. def factorial(n) – Creates a function.
# 2. fact = 1 – Initializes factorial value as 1.
# 3. for i in range(1, n + 1) – Loops from 1 to the entered number.
# 4. fact = fact * i – Multiplies each number.
# 5. return fact – Returns the final factorial.
# 6. print() – Displays the result.

# How factorial works:
# 5! = 1 \times 2 \times 3 \times 4 \times 5 = 120

# Remember: Factorial of 0 is also 1.

#==========recursive function===================================================================
# Factorial using Recursive Function in Python
# A recursive function is a function that calls itself again and again until a stopping condition is reached.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


num = int(input("Enter a number: "))
print("Factorial =", factorial(num))

# example: factorial(5)
# = 5 * factorial(4)
# = 5 * 4 * factorial(3)
# = 5 * 4 * 3 * factorial(2)
# = 5 * 4 * 3 * 2 * factorial(1)
# = 5 * 4 * 3 * 2 * 1
# = 120

# Code	                                Meaning
#---------------------------------------------------------------------------
# def factorial(n)	               Defines a function
# if n == 0 or n == 1	           Stopping condition (base case)
# return 1	                       Stops recursion
# factorial(n-1)	               Function calls itself
# return n * factorial(n-1)    	   Multiplies the numbers

# Remember:
# - Base condition → Stops the function.
# - Recursive call → Function calls itself.
# Without a base condition, recursion will continue until Python raises a recursion error.


# return n * factorial(n-1) means multiply the current number by the factorial of the previous number.
# Here:
# - n = Current number.
# - n-1 = Previous number.
# - factorial(n-1) = Calls the same function again with the previous number.
# - return = Sends back the calculated result.

#=========without return=========================================================================================
def factorial(n, fact=1):
    if n == 0 or n == 1:
        print("Factorial =", fact)
    else:
        fact = fact * n
        factorial(n - 1, fact)


num = int(input("Enter a number: "))
factorial(num)

#--------------------------------------------------------------------------------------------------
def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    print("Factorial =", fact)


num = int(input("Enter a number: "))
factorial(num)


# Difference between both:
# Normal function           	Recursive function
#-----------------------------------------------------------------------------
# Uses for loop              Function calls itself
# Multiplies using loop  	 Multiplies before each recursive call
# No return needed	         No return needed
# Stops when loop ends	     Stops at base condition