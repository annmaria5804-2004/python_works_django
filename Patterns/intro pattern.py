""" 6th nov 2026
pattern
============================================
Code	                   Purpose

print("*")	           Prints on a new line
print("*", end=" ")	   Prints on the same line

=====================================================================
4. Important concept to remember
Pattern	            Loop	                Output

Down	         Single loop	            Vertical
Straight line	 Single loop + end=" "  	Horizontal
Square	         Nested loop	            Rows and columns

"""
# down
for i in range(1,8):
    print("*")
""" o/p:
*
*
*
*
*
*
*
"""

# straight line
for i in range(1,8):
    print("*",end=" ") # * * * * * * *  # end=" " prevents moving to the next line.
    
# square block
for i in range(3):
    for j in range(1,4):
       print("*",end=" ")
    print()
    
""" o/p:
* * *
* * *
* * *

======================================================
There are two loops:
- Outer loop (i) → Controls rows.
- Inner loop (j) → Controls columns.
"""

# butterfly------------------------
n = 5

# Upper part
for i in range(1, n + 1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)

# Lower part
for i in range(n, 0, -1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)

# Simple logic
# 1. n = 5 → Number of rows.
# 2. "*" * i → Prints stars on the left and right.
# 3. " " * (2 * (n-i)) → Prints spaces in the middle.
# 4. First loop → Prints upper wings.
# 5. Second loop → Prints lower wings.
# Main concept: We use two for loops, one increasing and one decreasing.

# 1. Equilateral Triangle Pattern====================================================
n = 5

for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
    
# 2. Rectangle Pattern=========================================================================
rows = 4
cols = 6

for i in range(rows):
    for j in range(cols):
        print("*", end=" ")
    print()
    
# Hollow Rectangle Pattern (Bonus)==================================================
rows = 4
cols = 6

for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows-1 or j == 0 or j == cols-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
    
# i controls rows.
# j controls columns.
# end=" " prints on the same line.
# print() moves to the next line.



# This is a Right-Angled Triangle Star Pattern ⭐
# *
# * * 
# * * * 
# * * * * 
# * * * * * 

for i in range(1, 6):
    for j in range(1, i+1):
        print("*", end=" ")
    print()

#     Easy explanation
# - Outer loop (i) → Controls the rows.
# - Inner loop (j) → Controls how many stars to print in each row.
# - i+1 → Increases the number of stars in every row.
# - end=" " → Prints stars on the same line.
# - print() → Moves to the next line.












