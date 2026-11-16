# wap  to find the numbers from a list of sequence of numbers 
# The missing numbers between 1 and 11 are 4 and 8.

num = [7, 3, 1, 2, 6, 9, 11, 10, 5]

for i in range(1, 12):
    if i not in num:
        print(i)
        
# Explanation
# - range(1, 12) generates numbers from 1 to 11.
# - if i not in nunm checks whether each number is missing from the list.
# - print(i) displays the missing numbers.
# If you meant something else by “find the numbers from a list of sequence of numbers,” tell me what output you need, and I'll show you the correct program.

nunm = [7, 3, 1, 2, 6, 9, 11, 10, 5]

for i in range(min(nunm), max(nunm) + 1):
    if i not in nunm:
        print(i)
        
# Explanation
# - min(nunm) returns the smallest number, which is 1.
# - max(nunm) returns the largest number, which is 11.
# - range(min(nunm), max(nunm) + 1) checks all numbers from 1 to 11.
# - if i not in nunm checks whether a number is missing.
# Why max(nunm) + 1? Because the ending value of range() is excluded. Adding 1 ensures that 11 is checked too.