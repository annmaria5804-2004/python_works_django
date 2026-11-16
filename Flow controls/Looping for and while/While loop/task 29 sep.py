# 1. Find and display all factors
num = int(input("Enter a number: "))
i = 1
while i <= num:
    if num % i == 0:
        print(i)
    i += 1
    
#2. Sum of even factors
num = int(input("Enter a number: "))
i = 1
sum = 0
while i <= num:
    if num % i == 0 and i % 2 == 0:
        sum += i
    i += 1
print("Sum of even factors:", sum)
 
# 3. Sum of odd factors
num = int(input("Enter a number: "))
i = 1
sum = 0
while i <= num:
    if num % i == 0 and i % 2 != 0:
        sum += i
    i += 1
print("Sum of odd factors:", sum)

# 4. Count the factors
num = int(input("Enter a number: "))
i = 1
count = 0
while i <= num:
    if num % i == 0:
        count += 1
    i += 1
print("Number of factors:", count)

# 5. Sum of all factors
num = int(input("Enter a number: "))
i = 1
sum = 0
while i <= num:
    if num % i == 0:
        sum += i
    i += 1
print("Sum of factors:", sum)

# 6. Count of even factors
num = int(input("Enter a number: "))
i = 1
count = 0
while i <= num:
    if num % i == 0 and i % 2 == 0:
        count += 1
    i += 1
print("Count of even factors:", count)

# 7. Product of odd factors
num = int(input("Enter a number: "))
i = 1
product = 1
while i <= num:
    if num % i == 0 and i % 2 != 0:
        product *= i
    i += 1
print("Product of odd factors:", product)