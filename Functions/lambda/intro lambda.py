# # Lambda==== 4th nov===========================================================
# =============================================================================================
"""
Important: Lambda functions automatically return the result of their expression. You don't need to write return.
>>> syntax: lambda arguments : expression
>>> eg:  result = lambda a, b: a + b
===================sir=====================================================================================================
A anonymous function(without a name) which contains a single expression and multiple arguments.
syntax: lambda arguments : expression
"""

# > normal fumction without lambda:
def add(n1,n2):
    result = n1 + n2
    print(result)
add(3,4) # 7

# Explanation:
# - def is used to create a normal function.
# - add is the function name.
# - n1, n2 are parameters.
# - return is not used here; instead, print() displays the result.

# ======================================================================================================

# > usimg lambda :
result = lambda a, b: a + b
print(result(3, 4))

# You are printing result, which displays the function object, not the answer.

# 4. Difference between all three
# Method	Accepts	Data type
# *args	Multiple positional arguments	Tuple
# **kwargs	Multiple keyword arguments	Dictionary
# lambda	A short function expression	Function