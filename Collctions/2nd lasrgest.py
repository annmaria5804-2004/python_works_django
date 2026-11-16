# wap to get  the 2nd largest no. form the list
numbers = [10, 25, 8, 45, 32]

largest = numbers[0]
second_largest = numbers[0]

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second largest number:", second_largest)

# How it works
# - largest stores the largest number found so far.
# - second_largest stores the second largest number found so far.
# - if num > largest: updates both values.
# - elif num > second_largest and num != largest: updates only the second largest.
# Note: This simple version assumes the list has at least two distinct numbers.How it works
# - largest stores the largest number found so far.
# - second_largest stores the second largest number found so far.
# - if num > largest: updates both values.
# - elif num > second_largest and num != largest: updates only the second largest.
# Note: This simple version assumes the list has at least two distinct numbers.

# sort method---------------------------
numbers = [10, 25, 8, 45, 32]

numbers.sort()

print("Second largest number:", numbers[-2])
    
# How it works
# 1. numbers.sort() — Sorts the list in ascending order (smallest to largest).
# 2. numbers[-1] — Gives the largest number.
# 3. numbers[-2] — Gives the second largest number.
# Example:

# [8, 10, 25, 32, 45]
# - Largest: 45
# - Second largest: 32
# Tip: If you want to sort from largest to smallest, use numbers.sort(reverse=True). Then the second largest number is numbers[1].