# return the sum of no.s 1 to 1- using lambda

# Method 1: Using Lambda
result = lambda: sum(range(1, 11))

print(result()) # 55

# Understand step by step
# - lambda: → Lambda function without parameters.
# - range(1, 11) → Generates numbers from 1 to 10.
# - sum() → Adds all the numbers.
# - result() → Calls the lambda function.

# =================================================================
# Method 2: Using a parameter
result = lambda n: sum(range(1, n+1))

print(result(10)) # 55

# or ====================================================================
result = lambda num: sum(num)

print(result(num=list(range(1,11)))) # 55

