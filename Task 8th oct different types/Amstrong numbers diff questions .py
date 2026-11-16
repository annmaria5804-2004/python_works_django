# ============================================================
# 1. Print all Armstrong numbers between 1 and n
# ============================================================

n = int(input("Enter n: "))

for number in range(1, n + 1):

    temp = number
    count = 0

    # count the digits
    while temp > 0:
        count += 1
        temp //= 10

    temp = number
    total = 0

    # find Armstrong sum
    while temp > 0:
        digit = temp % 10

        power = 1
        for i in range(count):
            power *= digit

        total += power
        temp //= 10

    if total == number:
        print(number)


# ============================================================
# 2. Display all Armstrong numbers from n down to 1
# ============================================================

n = int(input("Enter n: "))

for number in range(n, 0, -1):

    temp = number
    count = 0

    # count the digits
    while temp > 0:
        count += 1
        temp //= 10

    temp = number
    total = 0

    # find Armstrong sum
    while temp > 0:
        digit = temp % 10

        power = 1
        for i in range(count):
            power *= digit

        total += power
        temp //= 10

    if total == number:
        print(number)


# ============================================================
# 3. Count how many Armstrong numbers exist between 1 and n
# ============================================================

n = int(input("Enter n: "))

count_armstrong = 0

for number in range(1, n + 1):

    temp = number
    count = 0

    # count the digits
    while temp > 0:
        count += 1
        temp //= 10

    temp = number
    total = 0

    # find Armstrong sum
    while temp > 0:
        digit = temp % 10

        power = 1
        for i in range(count):
            power *= digit

        total += power
        temp //= 10

    if total == number:
        count_armstrong += 1

print("Number of Armstrong numbers =", count_armstrong)


# ============================================================
# 4. Display Armstrong numbers between starting and ending number
# ============================================================

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for number in range(start, end + 1):

    temp = number
    count = 0

    # count the digits
    while temp > 0:
        count += 1
        temp //= 10

    temp = number
    total = 0

    # find Armstrong sum
    while temp > 0:
        digit = temp % 10

        power = 1
        for i in range(count):
            power *= digit

        total += power
        temp //= 10

    if total == number:
        print(number)


# ============================================================
# 5. Display all three-digit Armstrong numbers
# ============================================================

for number in range(100, 1000):

    temp = number
    total = 0

    while temp > 0:

        digit = temp % 10

        power = 1

        for i in range(3):
            power *= digit

        total += power
        temp //= 10

    if total == number:
        print(number)

