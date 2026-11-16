# wap to get the sum of three numbers enter by users a function

def sum_numbers(a, b, c):
    total = a + b + c
    print("Sum =", total)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

sum_numbers(a, b, c)

# Simple explanation
# - def sum_numbers(a, b, c): defines a function with three parameters.
# - input() gets three numbers from the user.
# - int() converts the entered values from strings into integers.
# - total = a + b + c adds the three numbers.
# - print() displays the sum.
# - sum_numbers(a, b, c) calls the function.


# here only 3 numbers can only pass so if call  a number again and pass number to much times as we like 2 3 or 4 or more can possbile using * args arguments

# WAP to get the sum of three numbers using *args(iterable)

def sum_numbers(*args):
    total = 0
    for i in args:
        total += i
    print("Sum =", total)

sum_numbers(2,5,7,13)
sum_numbers(5,5,7)
sum_numbers(2,5)

# Simple explanation
# - *args allows a function to accept any number of positional arguments.
# - total = 0 initializes the sum.
# - for i in args: loops through each number.
# - total += i adds each number to the total.
# - print() displays the final sum.
# Remember: You can also call sum_numbers(10, 20, 30, 40) to add four numbers without changing the function.