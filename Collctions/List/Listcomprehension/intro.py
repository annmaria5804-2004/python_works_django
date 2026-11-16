"""
List comprehension==========================================
-------------------------------------------------------------
> To create a new list  from any exstig itreable can be written in a sungle line



""" 
# WAP to get the numbers from 1 to 10 in a list using list comprehension

print([i for i in range(1, 11)])

# Explanation:
# - range(1, 11) generates numbers from 1 to 10.
# - for i in range(1, 11) takes each number one by one.
# - [i for i in range(1, 11)] creates a new list containing all those numbers.

# or----------------------------------------------
# WAP to get the numbers from 1 to 10 in a list using for loop

num = []

for i in range(1, 11):
    num.append(i)

print(num)

# Explanation:
# 1. num = [] creates an empty list.
# 2. range(1, 11) generates numbers from 1 to 10.
# 3. num.append(i) adds each number to the list.
# 4. print(num) displays the final list.

