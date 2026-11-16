# ============================================================
# SECTION 3: DIFFERENT TYPES OF PRIME NUMBERS
# ============================================================


# 12. Display all prime numbers between 1 and n.

n = int(input("Enter n: "))

for number in range(2, n + 1):

    count = 0

    for i in range(1, number + 1):
        if number % i == 0:
            count += 1

    if count == 2:
        print(number)


# ============================================================


# 13. Display all prime numbers from n down to 1.

n = int(input("Enter n: "))

for number in range(n, 1, -1):

    count = 0

    for i in range(1, number + 1):
        if number % i == 0:
            count += 1

    if count == 2:
        print(number)


# ============================================================


# 14. Count how many prime numbers exist between 1 and n.

n = int(input("Enter n: "))

count_prime = 0

for number in range(2, n + 1):

    count = 0

    for i in range(1, number + 1):
        if number % i == 0:
            count += 1

    if count == 2:
        count_prime += 1

print("Number of prime numbers =", count_prime)


# ============================================================


# 15. Find the sum of all prime numbers between 1 and n.

n = int(input("Enter n: "))

sum_prime = 0

for number in range(2, n + 1):

    count = 0

    for i in range(1, number + 1):
        if number % i == 0:
            count += 1

    if count == 2:
        sum_prime += number

print("Sum of prime numbers =", sum_prime)


# ============================================================


# 16. Display pairs of prime numbers whose difference is 2.
#     These are called twin primes.

n = int(input("Enter n: "))

for number in range(2, n + 1):

    count1 = 0

    for i in range(1, number + 1):
        if number % i == 0:
            count1 += 1

    if count1 == 2:

        second = number + 2

        count2 = 0

        for j in range(1, second + 1):
            if second % j == 0:
                count2 += 1

        if count2 == 2 and second <= n:
            print(number, second)


# ============================================================


# 17. Accept a starting and ending number.
#     Display all prime numbers in that interval.

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for number in range(start, end + 1):

    count = 0

    for i in range(1, number + 1):
        if number % i == 0:
            count += 1

    if count == 2:
        print(number)


# ============================================================


# 18. Accept a number and display all its prime factors.

n = int(input("Enter number: "))

for i in range(2, n + 1):

    if n % i == 0:

        count = 0

        for j in range(1, i + 1):
            if i % j == 0:
                count += 1

        if count == 2:
            print(i)


# ============================================================


# 19. Display all numbers between 1 and n that have exactly two factors.

n = int(input("Enter n: "))

for number in range(1, n + 1):

    count = 0

    for i in range(1, number + 1):
        if number % i == 0:
            count += 1

    if count == 2:
        print(number)


# ============================================================


# 20. Display each prime number between 1 and n
#     along with its number of factors.

n = int(input("Enter n: "))

for number in range(2, n + 1):

    count = 0

    for i in range(1, number + 1):
        if number % i == 0:
            count += 1

    if count == 2:
        print(number, "-> Number of factors =", count)


# ============================================================


# 21. Display consecutive prime numbers whose difference is 2.

n = int(input("Enter n: "))

for number in range(2, n):

    count1 = 0

    for i in range(1, number + 1):
        if number % i == 0:
            count1 += 1

    next_number = number + 2
    count2 = 0

    for j in range(1, next_number + 1):
        if next_number % j == 0:
            count2 += 1

    if count1 == 2 and count2 == 2 and next_number <= n:
        print(number, next_number)