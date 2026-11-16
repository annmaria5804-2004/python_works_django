"""
count the number of digits in a strig.
sample i/p: Abc12345
"""

word = "Abc12345"
count = 0

for i in word:
    if i.isdigit(): # if i.isdigit(): — Checks whether the character is a digit (0–9).
        count = count + 1

print("Number of digits:", count)


""" next question:
wap to remove all the whitespaces in the given string
 # string is immutabel >>> cant modify a striing value.
 
Simple line-by-line explanation
1. word = "hello world python" — Stores the string.
2. result = "" — Creates an empty string to store the result.
3. for i in word: — Checks each character one by one.
4. if i != " ": — Checks whether the character is not a space.
5. result = result + i — Adds the character to result only if it is not a space.
6. print(result) — Displays the string without spaces.

"""


word = "hello world python"
result = ""

for i in word:
    if i != " ": # Checks whether the character is not a space.
        result = result + i # Adds the character to result only if it is not a space.

print(result)

"""next question:
 # remove all the digits from string
 
 Simple line-by-line explanation
1. word = "abc123de" — Stores the given string.
2. result = "" — Creates an empty string to store the result.
3. for i in word: — Checks each character one by one.
4. if not i.isdigit(): — Checks whether the character is not a digit.
5. result = result + i — Adds only non-digit characters to result.
6. print(result) — Displays the string without digits.
Remember:
- i.isdigit() → True if the character is a digit.
- not i.isdigit() → True if the character is not a digit.
"""

word = "abc123de"
result = ""

for i in word:
    if not i.isdigit():
        result = result + i

print(result)


