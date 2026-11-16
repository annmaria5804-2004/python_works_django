# wap to return the unique cha from the string given

name ="machinelearning"
for i in name: # vimp step in all string prgm imp line.  takes each character one by one.
    if name.count(i) == 1: # counts how many times that character appears.
        print(i) #  prints the character if it appears only once.
        
"""
Simple explanation
- for i in name: — takes each character one by one.
- name.count(i) — counts how many times that character appears.
- == 1 — checks whether the character appears only once.
- print(i) — prints the character if it appears only once.
Note: Here, unique means characters that appear exactly once in the string.
If you want to print all characters without repeating any character, that is a different method.
o/p:
m
c
h
l
r
g

"""
# wap If you want to print all characters without repeating any character, that is a different method.

name = "machinelearning"

for i in name:
    if name.index(i) == name.find(i):
        print(i)
"""
o/p:
m
a
c
h
i
n
e
l
e
a
r
n
i
n
g

"""
# or:
name = "machinelearning"
unique = ""

for i in name:
    if i not in unique:
        unique = unique + i

print(unique)
"""
Simple explanation
- unique = "" — starts with an empty string.
- for i in name: — takes each character one by one.
- if i not in unique: — checks whether the character is already stored.
- unique = unique + i — adds the character only if it hasn't appeared before.
- print(unique) — prints the result without repeating characters.
"""