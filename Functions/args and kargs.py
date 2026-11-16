# collections===============================================================================
# You are now learning **kwargs in Python. It is similar to *args, but there is one important difference.
# - *args → Accepts multiple positional arguments.
# - **kwargs → Accepts multiple keyword arguments (key-value pairs).====================================================================================

# *args
def addition(*numbers): # numbers =(1,2,3,4)
    return sum(numbers)
addition(1,2,3,4) # variable number of postional arguments
addition(3,4,5)
addition(3,4,5,6,7,8,9) # Output: (10, 20, 30) Data type: Tuple

# Here:
# - *numbers accepts multiple positional arguments.
# - Python collects all the arguments into a tuple.
# - sum(numbers) adds all the values.
# - return sends the answer back.
# Important: args is not a keyword. You can use any variable name, such as *numbers, *values, or *args.
# Because *args collects multiple positional arguments into a tup

# ==========================================================================================================================
# **kwargs  vimp===================================================================
def details(**kwargs):
    pass
details(name ="ann",place ="kochi")
details(name ="ann",place ="kochi",age =22) # o/p:Output: {'name': 'ann', 'age': 22} Data type: Dictionary

# Here:
# - **kwargs accepts any number of keyword arguments.
# - Python collects them into a dictionary.
# - pass means do nothing (it is used as a placeholder).
# Since kwargs is a dictionary, you can access values using keys.

#===========================================================================================================================================
# 1. Using *args
# *args accepts multiple positional arguments and stores them in a tuple.

def addition(*numbers):
    return sum(numbers)

print(addition(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# ===================================================================================================================

# 2. Using **kwargs
# **kwargs accepts multiple keyword arguments and stores them in a dictionary.
def addition(**numbers):
    return sum(numbers.values())

print(addition(a=1, b=2, c=3, d=4, e=5,
               f=6, g=7, h=8, i=9, j=10))

# Explanation:
# - **numbers collects the arguments into a dictionary.
# - numbers.values() gets only the values.
# - sum() adds all the values.
# Important: *args and **kwargs are ways of accepting arguments in a function. Lambda is a way of creating a function. They can be used together, but they are not the same concept.