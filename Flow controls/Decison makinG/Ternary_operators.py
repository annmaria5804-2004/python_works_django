""" 8th october 2026
Ternary Operators
(value_if_true if condition else value_if_false)
=============================

"""
# example:
n =12 # only prblm is that we need to define the number
#if n % 2 == 0:
#  print("even")
#else:
#  print("odd")
# now making this as simple single line prgm using ternary operators:
print("even" if n % 2 == 0 else "odd")
# this prgm means print return even if n % 2 == 0 else odd 
#or
print(f"{n}even" if n % 2 == 0 else "odd")
# if neede can use f string in this
# other exmpke:
print("divisible" if n % 3 == 0 else "not didisible")

## Check whether a number is divisible by both 3 and 5
num = int(input("Enter the number: "))
print("Divisible" if n % 3 == 0 and n % 5 == 0 else "Not Divisible")