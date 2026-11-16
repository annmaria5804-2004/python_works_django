# Fibinacci numbers
#================================================================
# it is a series of numbers from 0 to 1 where each term is the sum of the 2 preceding numbers.
# 0 1 1 2 3 4 8 13 21 34 56.......
# Definition: Fibonacci is a series of numbers where each number is the sum of the previous two numbers.
# fromula: F(n) = F(n-1) + F(n-2)
# Remember: Fibonacci uses addition, whereas factorial uses multiplication.


# 1. Fibonacci using a normal function (without return)
def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c


num = int(input("Enter the number of terms: "))
fibonacci(num)

# a = b → Move the second number to the first position.
# b = c → Move the sum to the second position.
# c = a + b → Add the previous two numbers.

#==============2. Fibonacci using a recursive function (without return)=============================
def fibonacci(n, a=0, b=1):
    if n > 0:
        print(a, end=" ")
        fibonacci(n-1, b, a+b)


num = int(input("Enter the number of terms: "))
fibonacci(num)

#========Fibonacci Series without Function (Using for loop)==============================================
# Fibonacci series
a = 0
b = 1
n = int(input("Enter the number of terms: "))
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    
# Remember these three lines:
# - c = a + b → Add two numbers.
# - a = b → Update first number.
# - b = c → Update second number.