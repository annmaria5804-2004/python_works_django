# wap to remove the all non prime from the list

num = [1, 3, 2, 4, 8, 7, 9, 11, 13, 15]

for i in num.copy():
    count = 0

    if i < 2:
        num.remove(i)
    else:
        for j in range(2, i):
            if i % j == 0:
                count = count + 1
                break

        if count > 0:
            num.remove(i)

print(num)

# Explanation
# - num.copy() lets you safely remove elements while looping.
# - if i < 2 removes 1, because 1 is not a prime number.
# - range(2, i) checks whether the number is divisible by any number from 2 up to i - 1.
# - if i % j == 0 means the number is divisible by another number, so it is not prime.
# - num.remove(i) removes the non-prime number from the original list.
# Remember: A prime number is greater than 1 and has exactly two factors: 1 and itself.