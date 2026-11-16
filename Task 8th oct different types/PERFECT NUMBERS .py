# ============================================================
# SECTION 2: PERFECT NUMBERS
# ============================================================


# 6. A perfect number is equal to the sum of its proper factors.
#    Print all perfect numbers from 1 to n.

n = int(input("Enter n: "))

for number in range(1, n + 1):

    total = 0

    for i in range(1, number):
        if number % i == 0:
            total += i

    if total == number:
        print(number)


# ============================================================


# 7. Display all perfect numbers from n down to 1.

n = int(input("Enter n: "))

for number in range(n, 0, -1):

    total = 0

    for i in range(1, number):
        if number % i == 0:
            total += i

    if total == number:
        print(number)


# ============================================================


# 8. Count all perfect numbers between 1 and n.

n = int(input("Enter n: "))

count = 0

for number in range(1, n + 1):

    total = 0

    for i in range(1, number):
        if number % i == 0:
            total += i

    if total == number:
        count += 1

print("Number of perfect numbers =", count)


# ============================================================


# 9. Accept two limits and display every perfect number between them.

a= int(input("Enter starting number: "))
b= int(input("Enter ending number: "))

if a>b: # vimp swapping because if a > b then we need to do this to make the prgm  perfect
    a,b = b,a # here we say a b and b a are equal so swap them so a become b and b become a 
    
for number in range(a , b + 1):

    total = 0

    for i in range(1, number):
        if number % i == 0:
            total += i

    if total == number:
        print(number)


# ============================================================


# 10. Find the sum of all perfect numbers between 1 and n.

n = int(input("Enter n: "))

sum_perfect = 0

for number in range(1, n + 1):

    total = 0

    for i in range(1, number):
        if number % i == 0:
            total += i

    if total == number:
        sum_perfect += number

print("Sum of perfect numbers =", sum_perfect)


# ============================================================


# 11. Check every number from n down to 1.
#     Print each perfect number along with the sum of its proper factors.

n = int(input("Enter n: "))

for number in range(n, 0, -1):

    total = 0

    for i in range(1, number):
        if number % i == 0:
            total += i

    if total == number:
        print(number, "-> Sum of proper factors =", total)