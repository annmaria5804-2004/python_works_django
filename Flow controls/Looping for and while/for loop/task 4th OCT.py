# Print all numbers from 1 to 50.
for i in range(1, 51):
    print(i)

# 2. Print Even Numbers between 1 and 100.
for i in range(1, 101):
    if i % 2 == 0:
        print("EVEN: ", i)

# 3. Print all odd numbers between 1 and 100.
for i in range(1, 101):
    if i % 2 != 0:
        print("ODD: ",i)

# 4. Sum of Numbers all numbers from 1 to 100.
sum = 0
for i in range(1, 101):
    sum += i
print("Sum =", sum)

# 5.Find the sum of all even numbers between 1 and 100.
sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum += i
print("Sum of even numbers =", sum)

# 6. Count how many even numbers are present between 1 and 100.
count = 0
for i in range(1, 101):
    if i % 2 == 0:
        count += 1
print("Count =", count)

# 7. Read a number and print its multiplication table from 1 to 10.
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n * i)

# 8. Read a number and print all its factors.
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    if n % i == 0:
        print(i)

# 9. Read a number and find the total number of factors.
n = int(input("Enter a number: "))
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count += 1
print("NO. of factors =", count)

# 10.Read a number and calculate the sum of all its factors.
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n + 1):
    if n % i == 0:
        sum += i
print("Sum of factors =", sum)

# 11. Read a number and calculate the sum of only its even factors.
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n + 1):
    if n % i == 0 and i % 2 == 0:
        sum += i
print("Sum of even factors =", sum)

# 12. Read a number and find how many even factors it has.
n = int(input("Enter a number: "))
count = 0
for i in range(1, n + 1):
    if n % i == 0 and i % 2 == 0:
        count += 1
print("NO. of even factors =", count)

# 13.Find and display the factorial of each number from 6 down to 1.
for i in range(6, 0, -1):
    fact = 1
    for j in range(1, i + 1):
        fact *= j
    print(f"the factorial of {i} is {fact}")
        
# 14. Read n and count numbers from 1 to n that are divisible by both 3 and 5.
n = int(input("Enter n: "))
count = 0
for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        count += 1
print("Count =", count)

# 15. Find the sum of all even factors for each number from 10 down to 6.
for i in range(10, 5, -1):
    sum = 0
    for j in range(1, n + 1):
        if n % j == 0 and i % j == 0:
            sum += j
    print("Sum of even factors ", sum)
