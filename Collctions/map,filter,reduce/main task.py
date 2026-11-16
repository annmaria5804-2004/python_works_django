# map,filter,reduce===========================
# ============================================================================
#  wap to reduce even numbers from list of num from 1 to 20
# return the list  of square of num from even list above
# from the final saquared list retuen the sum

from functools import reduce # need for reduce only
numbers = list(range(1, 21))

# Step 1: Filter even numbers
even = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even)

# Step 2: Find square of even numbers
square = list(map(lambda x: x ** 2, even))
print("Square numbers:", square)

# Step 3: Find sum of squared numbers
total = reduce(lambda x, y: x + y, square)
print("Sum:", total)

# o/p:
# Even numbers: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# Square numbers: [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
# Sum: 1540

#=================================================================================
# Original list
# 1 to 20
# FILTER
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# MAP
# [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
# REDUCE
# 1540
# Final sum

#============================================================================================
# # FILTER
# lambda x: x % 2 == 0

# # MAP
# lambda x: x ** 2

# # REDUCE
# lambda x, y: x + y

#============================================================================
# Easy trick for your exam:
# - Even / Odd / Greater than → filter()
# - Square / Cube / Multiply each → map()
# - Sum / Product / Combine → reduce()
