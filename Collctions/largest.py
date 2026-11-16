# wap to get the largest no. from the list of numbers.
numbers = [10, 25, 8, 45, 32]

largest = max(numbers)

print("Largest number:", largest)
# orr----------------------
print("lowest number:", min(numbers) )
print("sum number:", sum(numbers) )

#   without build in functions============================================
numbers = [10, 25, 8, 45, 32]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number:", largest)

# How does Method 2 work?
# 1. largest = numbers[0] — Assume the first number is the largest.
# 2. for num in numbers: — Check each number in the list.
# 3. if num > largest: — If the current number is bigger, update largest.
# 4. print() — Display the final largest number.
# For your Python practice, try Method 2 first because it helps you understand loops and if conditions.

# smallest or--------------------------------------------------------
numbers = [10, 25, 8, 45, 32]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest number:", smallest)

# How it works
# 1. smallest = numbers[0] — Assume the first number is the smallest.
# 2. for num in numbers: — Check each number in the list.
# 3. if num < smallest: — If the current number is smaller, update smallest.
# 4. print() — Display the smallest number.
# Remember:
# - Largest number → num > largest
# - Smallest number → num < smallest