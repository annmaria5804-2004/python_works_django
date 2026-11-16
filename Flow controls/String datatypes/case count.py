# ask the user to enter the string'
# wap to return the total number of lowercase char and upper case char

name = input("Enter the string: ")

up = 0
lc = 0

for i in name:
    if i.isupper():
        up += 1
    elif i.islower():
        lc += 1

print("Uppercase:", up)
print("Lowercase:", lc)

"""
Simple explanation
- up = 0 → starts the uppercase count at zero.
- lc = 0 → starts the lowercase count at zero.
- for i in name: → checks each character one by one.
- i.isupper() → checks whether the character is uppercase (A, B, C…).
- up += 1 → increases the uppercase count by one.
- i.islower() → checks whether the character is lowercase (a, b, c…).
- lc += 1 → increases the lowercase count by one.

Enter the string: haiann
Uppercase: 0
Lowercase: 6
PS D:\python_works_d
"""