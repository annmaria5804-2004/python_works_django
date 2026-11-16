# numbers printing pattern======================================================================
# 1. Increasing numbers
# 1
# 12
# 123
# 1234
# 12345

for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

# 2. Same number in each row
# 1
# 22
# 333
# 4444
# 55555

for i in range(1, 6):
    for j in range(1, i+1):
        print(i, end=" ")
    print()

# 3. Decreasing numbers
# 12345
# 1234
# 123
# 12
# 1

for i in range(5, 0, -1):
    for j in range(1, i+1):
        print(j, end="")
    print()
    
# 4. Reverse numbers
# 54321
# 5432
# 543
# 54
# 5

for i in range(5, 0, -1):
    for j in range(5, i-1, -1):
        print(j, end="")
    print()
    
# 1. Number Square Pattern in Python
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

for i in range(1, 6):
    for j in range(1, 6):
        print(j, end=" ")
    print()
    
# Explanation:
# - Outer loop (i) → Controls rows (5 rows).
# - Inner loop (j) → Controls columns (5 columns).
# - print(j, end=" ") → Prints numbers in the same line.
# - print() → Moves to the next row.

# 2. Same Number Square
for i in range(1, 6):
    for j in range(1, 6):
        print(i, end=" ")
    print()

# 3. Continuous Number Square
# 1  2  3  4  5
# 6  7  8  9  10
# 11 12 13 14 15
# 16 17 18 19 20
# 21 22 23 24 25

num = 1
for i in range(1, 6):
    for j in range(1, 6):
        print(num, end=" ")
        num = num + 1
    print()