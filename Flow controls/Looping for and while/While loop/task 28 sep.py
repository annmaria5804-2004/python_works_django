""""
While Loop – Number Practice 
1. Write a program to print all numbers between 1 and 100 that are divisible by 7 using a while loop.
"""
i = 1
while i <= 100:
    if i % 7 == 0:
        print(i)
    i = i + 1

# 2. Numbers between 1 and 100 divisible by both 3 and 5
num = 1
while num <= 100:
    if num % 3 == 0 and num % 5 == 0:
        print(num)
    num = num + 1

# 3. Numbers between 1 and 50 that are not divisible by 5
num = 1
while num <= 50:
    if num % 5 != 0:
        print(num)
    num = num + 1

# 4. Numbers between 1 and 100 divisible by 3 but not divisible by 5
num = 1
while num <= 100:
    if num % 3 == 0 and num % 5 != 0:
        print(num)
    num = num + 1

# 5. Take n from the user, print numbers divisible by 7 and find their sum
n = int(input("Enter a number: "))
i = 1
total = 0
while i <= n:
    if i % 7 == 0:
        print(i)
        total = total + i
    i = i + 1

print("Sum = ", total)