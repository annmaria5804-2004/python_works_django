""" 6th nov 2026=========================
map(), filter(), reduce()

1. map() – Perform an operation on every element
Meaning: Applies a function to every element in a collection and returns the modified values.

2. filter() – Filter elements based on a condition
Meaning: Selects only the elements that satisfy a condition.

3. reduce() – Reduce all elements to a single value
Meaning: Performs an operation cumulatively on elements and produces one final result.

reduce() is available in the functools module.

Difference between map(), filter() and reduce()
Function	Purpose	               Result
map()	   Modify every element	    Collection
filter()   Select elements	       Collection
reduce()   Combine elements	       Single value


MAP
Change every element
[1, 2, 3] → [2, 4, 6]
Multiply every number by 2.


FILTER
Select required elements
[1, 2, 3, 4] → [2, 4]
Select only even numbers.


REDUCE
Combine into one value
[1, 2, 3, 4] → 10
Calculate the total sum.


=====================sir....===================================================================
1. map(): it applies a given change to every element in a itreable (list,set,tuple renage())
syntax: map(function,itreable)

2.filter(): take after  filteration like only correct answer is taken in list and show as output
> selects elements from a itreable based on a condition.it returns the elemnts for which condition it is true
syntax: filter(function,itreable)

3. reduce(): 
syntax: reduce(function,itreable)

"""
#---------------------------------------------------------------------------------
# eg: map()

numbers = [1, 2, 3, 4, 5]
result = map(lambda x: x * 2, numbers) # lambda : 	Creates an anonymous (one-line) function
print(list(result)) # o/p: [2, 4, 6, 8, 10]

# other:====================sir======================================================================
numbers =[1,2,3,4]
print(list(map(lambda a:a ** 2,numbers))) # [1, 4, 9, 16]

# Here:
# - x represents each element.
# - x * 2 multiplies each element by 2.
# - map() applies this operation to all elements.

# ------------------------------------------------------------------------------------------------------------------------------------
#  eg : filter()

numbers = [1, 2, 3, 4, 5, 6]
result = filter(lambda x: x % 2 == 0, numbers)
print(list(result)) # o/p/: [2, 4, 6]

# or=================sir==============================================================
numbers = [1, 2, 3, 4, 5, 6,7,8]
print(list(filter(lambda a: a % 2 == 0, numbers))) # [2, 4, 6, 8]

# Here:
# - x % 2 == 0 checks whether a number is even.
# - If the condition is True, the element is included.
# - If False, it is excluded.

#-----------------------------------------------------------------------------
# eg: reduce()

from functools import reduce # we need to import reduce from  functools module
numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, numbers)
print(result) # o/p: 15

#=======================sir==============================================
from functools import reduce # we need to import reduce from  functools module
numbers = [1, 2, 3, 4]
print(reduce(lambda a, b: a + b, numbers)) # 10 (1+2+3+4=10)
print(reduce(lambda a, b: a * b, numbers))  # 24
print(reduce(lambda a, b: a / b, numbers)) # 0.041666666666666664
print(reduce(lambda a, b: a - b, numbers)) # -8

# A module is a a python file atreast contaian a variable or single line of code.

# 3 + 3 = 6
# 6 + 4 = 10
# 10 + 5 = 15
