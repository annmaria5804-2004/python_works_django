name = "python" # only 1st char become captial and all others will become lower or remain as lower

print(name.capitalize()) # defined code but we need to find how this works rtather tahn defined method
# or
# so here 0th index valuse is capitalized therefore:

print(name[0].upper() + name[1:].lower()) # here p become P then 1 to end all will print using concatination as +
print(ord("h")) # 104 ord() gives the number (ASCII/Unicode value) of a character.
print(chr(104)) # chr() → Number to character
"""
ord() gives the number (ASCII/Unicode value) of a character.

print(ord("A"))  # 65
print(ord("a"))  # 97
print(ord("b"))  # 98
print(ord("0"))  # 48

ord() → Character to number

chr() → Number to character
"""