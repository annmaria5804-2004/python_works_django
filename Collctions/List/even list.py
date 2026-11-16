# wap to print the even numbers from 1 to 50 in list

numbers = []
for i in range(1, 51):
    if i % 2 == 0:
        numbers.append(i)
print(numbers)
# o/p: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]

"""
 Explanation
- range(1, 51) generates numbers from 1 to 50.
- i % 2 == 0 checks whether a number is even.
- numbers.append(i) adds each even number to the list.
- print(numbers) displays the list.
""" 