# ============================================================
# SECTION 5: MIXED NUMBER CHALLENGES
# ============================================================


# 30. Print all numbers between 1 and n that are both odd and prime.

n = int(input("Enter n: "))

for number in range(1, n + 1):

    count = 0

    for i in range(1, number + 1):
        if number % i == 0:
            count += 1

    if number % 2 != 0 and count == 2:
        print(number)


# ============================================================


# 31. Print all numbers between 1 and n that are perfect squares and prime.

n = int(input("Enter n: "))

for number in range(1, n + 1):

    # Check perfect square
    square = False

    for i in range(1, number + 1):
        if i * i == number:
            square = True

    # Check prime
    count = 0

    for j in range(1, number + 1):
        if number % j == 0:
            count += 1

    if square and count == 2:
        print(number)


# ============================================================


# 32. Display all numbers between 1 and n whose digit sum is a prime number.

n = int(input("Enter n: "))

for number in range(1, n + 1):

    temp = number
    digit_sum = 0

    while temp > 0:
        digit = temp % 10
        digit_sum += digit
        temp //= 10

    # Check whether digit sum is prime
    count = 0

    for i in range(1, digit_sum + 1):
        if digit_sum % i == 0:
            count += 1

    if count == 2:
        print(number)


# ============================================================


# 33. Display all numbers between 1 and n that are both Armstrong and prime.

n = int(input("Enter n: "))

for number in range(1, n + 1):

    # Armstrong check
    temp = number
    digits = 0

    while temp > 0:
        digits += 1
        temp //= 10

    temp = number
    total = 0

    while temp > 0:

        digit = temp % 10

        power = 1

        for i in range(digits):
            power *= digit

        total += power
        temp //= 10

    # Prime check
    count = 0

    for j in range(1, number + 1):
        if number % j == 0:
            count += 1

    if total == number and count == 2:
        print(number)


# ============================================================


# 34. Display all numbers between 1 and n whose digit factorial
#     sum is greater than the original number.

n = int(input("Enter n: "))

for number in range(1, n + 1):

    temp = number
    total = 0

    while temp > 0:

        digit = temp % 10

        fact = 1

        for i in range(1, digit + 1):
            fact *= i

        total += fact
        temp //= 10

    if total > number:
        print(number)


# ============================================================


# 35. Print all numbers between n and 1 that have exactly three factors.

n = int(input("Enter n: "))

for number in range(n, 0, -1):

    count = 0

    for i in range(1, number + 1):
        if number % i == 0:
            count += 1

    if count == 3:
        print(number)


# ============================================================


# 36. Display all numbers between 1 and n whose proper-factor
#     sum is greater than the number itself.

n = int(input("Enter n: "))

for number in range(1, n + 1):

    total = 0

    for i in range(1, number):
        if number % i == 0:
            total += i

    if total > number:
        print(number)


# ============================================================


# 37. For each number between 1 and n, display whether it is
#     prime, perfect, Armstrong, or strong.

n = int(input("Enter n: "))

for number in range(1, n + 1):

    print("\nNumber:", number)

    # --------------------------------------------------------
    # PRIME CHECK
    # --------------------------------------------------------

    count = 0

    for i in range(1, number + 1):
        if number % i == 0:
            count += 1

    if count == 2:
        print("Prime")


    # --------------------------------------------------------
    # PERFECT CHECK
    # --------------------------------------------------------

    perfect_sum = 0

    for i in range(1, number):
        if number % i == 0:
            perfect_sum += i

    if perfect_sum == number:
        print("Perfect")


    # --------------------------------------------------------
    # ARMSTRONG CHECK
    # --------------------------------------------------------

    temp = number
    digits = 0

    while temp > 0:
        digits += 1
        temp //= 10

    temp = number
    armstrong_sum = 0

    while temp > 0:

        digit = temp % 10

        power = 1

        for i in range(digits):
            power *= digit

        armstrong_sum += power
        temp //= 10

    if armstrong_sum == number:
        print("Armstrong")


    # --------------------------------------------------------
    # STRONG CHECK
    # --------------------------------------------------------

    temp = number
    strong_sum = 0

    while temp > 0:

        digit = temp % 10

        fact = 1

        for i in range(1, digit + 1):
            fact *= i

        strong_sum += fact
        temp //= 10

    if strong_sum == number:
        print("Strong")