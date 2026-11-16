"""
# get the perfect number from the range 1 to 500
A perfect number is a positive integer that equals the sum of its proper divisors, excluding the number itself.
Examples of Perfect Numbers
6: Proper divisors are 1, 2, and 3. Their sum (1+2+3) equals 6.
28: Proper divisors are 1, 2, 4, 7, and 14. Their sum equals 28.

"""

# get the perfect number from the range 1 to 500

for num in range(1, 501):

    sum = 0

    for i in range(1, num):

        if num % i == 0:
            sum += i

    if sum == num:
        print(f"{num} is a perfect number")