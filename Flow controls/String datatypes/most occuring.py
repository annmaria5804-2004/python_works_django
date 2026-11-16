# return the char which is most occuring in the given string.


name = input("Enter the string: ") # aabbaaba

max_count = 0 # stores the highest count found so far.
char = "" #  stores the character with the highest count.

for i in name:
    count = name.count(i) # a=5 and b=3 counts how many times that each character appears.
    if count > max_count: # a=5 so 5> 0  checks whether its count is greater than the previous maximum.
        max_count = count #  max count as = 5 updates the highest count.
        char = i # stores that character.

print("Most occurring character:", char)
print("Count:", max_count)


"""
Simple explanation
- max_count = 0 → stores the highest count found so far.
- char = "" → stores the character with the highest count.
- for i in name: → checks each character one by one.
- count = name.count(i) → counts how many times that character appears.
- if count > max_count: → checks whether its count is greater than the previous maximum.
- max_count = count → updates the highest count.
- char = i → stores that character.
Note: If multiple characters have the same highest count, this code returns the first one it encounters. For aaabbcddd, both a and d occur 3 times, so it returns a.

o/p:
Enter the string: aabbaaba
Most occurring character: a
Count: 5
"""