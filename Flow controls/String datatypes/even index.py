# wap to return the char in the even indexes from the string by user

# or: sir...........
name = input("enter the string: ")

for i in range(len(name)):
    if i % 2 == 0:
        print(name[i])

"""
o/p:
enter the string: python
m (0 is a even number so index 0 is there)
c
i
e
e
r
i
Simple explanation
- for i in name: takes each character from the string.
- name.index(i) finds the index of that character.
- % 2 == 0 checks whether the index is even.
- print(i) prints the character if its index is even.
Important: name.index(i) returns the first occurrence of a character. If the string contains repeated characters, this method may give incorrect results.
"""

# or:
name = input("enter the string: ")
print(name[::2])