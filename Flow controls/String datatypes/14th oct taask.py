# 1. Replace Vowels with *

word = "education"
result = ""

for i in word:
    if i in "aeiou":
        result += "*"
    else:
        result += i

print(result)
# o/p: *d*c*t**n

# Simple explanation:
# - result = "" creates an empty string.
# - for i in word checks each character.
# - if i in "aeiou" checks whether the character is a vowel.
# - If it is a vowel, add *; otherwise, add the original character.
# - Finally, print the result.

# 2. Find the First Non-Repeating Character

word = "aabbcddee"

for i in word:
    if word.count(i) == 1:
        print(i)
        break
# o/p: c

# Simple explanation:
# - word.count(i) counts how many times a character occurs.
# - == 1 means the character appears only once.
# - print(i) displays the first character that occurs once.
# - break stops the loop immediately.

# 3. Check Whether Two Strings Are Rotations

word1 = "abcd"
word2 = "cdab"
# or print("rotational" if len(word1) == len(word2) and word1 in word1+word1 else "not rotational")
if len(word1) == len(word2) and word2 in word1 + word1:
    print("Rotation")
else:
    print("Not a Rotation")
# o/p:Rotation

# Simple explanation:
# - len(word1) == len(word2) checks whether both strings have the same length.
# - word1 + word1 gives "abcdabcd".
# - "cdab" is present inside "abcdabcd".
# - Therefore, the strings are rotations of each other.

# 4. Compress a String

word = "aaabbccccdaa"
result = ""
count = 1

for i in range(1, len(word)):
    if word[i] == word[i - 1]:
        count += 1
    else:
        result += word[i - 1] + str(count)
        count = 1

result += word[-1] + str(count)
print(result)
#o/p: a3b2c4d1a2

# Simple explanation:
# - count = 1 starts counting each character.
# - word[i] == word[i - 1] checks whether the current character equals the previous character.
# - If they match, increase count.
# - Otherwise, add the previous character and its count to result.
# - str(count) converts the number into a string.
# - The final line adds the last character and its count.

# 5. Expand an Encoded String

word = "a3b2c4"
result = ""

for i in range(0, len(word), 2):
    char = word[i]
    count = int(word[i + 1])
    result += char * count

print(result)
# 0o/p:aaabbcccc

# Simple explanation:
# - range(0, len(word), 2) moves through the string two positions at a time.
# - word[i] gets the character, such as a.
# - word[i + 1] gets its count, such as 3.
# - int() converts the count into an integer.
# - char * count repeats the character the required number of times.

# or..........
word = "a3b2c4"
result = ""

for i in range(len(word)):
    if word[i].isdigit():
        result += word[i - 1] * int(word[i])

print(result)

# Simple line-by-line explanation
# - word[i].isdigit() checks whether the current character is a digit.
# - word[i - 1] gets the character before the digit.
# - int(word[i]) converts the digit from a string to an integer.
# - word[i - 1] * int(word[i]) repeats the character that many times.
# - result += adds the repeated characters to the result.
# Example: When i points to '3', word[i - 1] is 'a', so 'a' * 3 gives 'aaa'.

# 6. Find the Second Most Frequent Character

word = "aaabbccccdd"
result = ""

for i in word:
    if i not in result:
        result += i
result = sorted(result, key=word.count, reverse=True)
print(result[1])

#o/p: b

# Simple explanation:
# - result = "" creates an empty string to store unique characters.
# - if i not in result prevents adding the same character more than once.
# - sorted() arranges characters by their frequency.
# - key=word.count uses each character's count.
# - reverse=True sorts from highest frequency to lowest.
# - result[1] prints the second character in the sorted list.
# For the sample, the frequencies are c = 4, a = 3, b = 2, and d = 2. The output is b because it appears before d in the original string when their frequencies are tied.


# 7. Remove Characters at Odd Index Positions

word = "python"
result = ""

for i in range(len(word)):
    if i % 2 == 0:
        result += word[i]

print(result)
# o/p: pto

# Simple explanation:
# - range(len(word)) gives the index positions: 0, 1, 2, 3, 4, 5.
# - i % 2 == 0 checks whether the index is even.
# - word[i] gets the character at that index.
# - The characters at indices 0, 2, and 4 are p, t, and o.
# Remember: Python indexing starts from 0, so even index positions are 0, 2, 4, ....

# 8. Check Neon Number

num = 9
square = num * num
total = 0

for i in str(square):
    total += int(i)

if total == num:
    print("Neon Number")
else:
    print("Not a Neon Number")
# o/p: Neon Number

# Simple explanation:
# - square = num * num calculates \(9 \times 9 = 81\).
# - str(square) converts 81 into "81".
# - The loop adds its digits: \(8 + 1 = 9\).
# - If the digit sum equals the original number, it is a Neon Number.
# Try num = 12. Its square is 144, and \(1 + 4 + 4 = 9\), so the output is Not a Neon Number.

# 9. Check Duck Number

num = 1023

if "0" in str(num):
    print("Duck Number")
else:
    print("Not a Duck Number")
# o/p: Duck Number


# Simple explanation:
# - str(num) converts the number into a string.
# - "0" in str(num) checks whether the number contains a zero.
# - If it contains a zero, print Duck Number.
# - Otherwise, print Not a Duck Number.
# For example, 1023 is a Duck Number, but 1234 is not.
# Important: A Duck Number contains zero in its digits, but a leading zero does not count. For example, 0123 written as a number becomes 123, which is not a Duck Number.


# or....................

# 6. Find the Second Most Frequent Character
# Sample Input: "aaabbccccdd"
# Sample Output: "b"


str1 = input("Enter the string: ")
mostcount = 1
secondmostcount = 1
secondcountchar = ""

for i in str1:
  if str1.count(i) > mostcount:
    mostcount = str1.count(i)

for i in str1:
  if str1.count(i)<mostcount and secondmostcount <str1.count(i):
    secondmostcount = str1.count(i)
    secondcountchar = i

print(f"Second frequent char is {secondcountchar}")

# =======================================================================

str1 = input("Enter the string: ")
mostcount = 1
scount = 1
scountchar = ""

for i in str1:
  if str1.count(i)>mostcount and str1.count(i)>scount:
    scount = mostcount
    mostcount = str1.count(i)

  elif str1.count(i)<mostcount and str1.count(i)>scount:
    scount = str1.count(i)
    scountchar = i

  else:
    pass

print(f"Second frequent char is {scountchar}")



"""
Simple explanation of each line
1. str1 = input(...) — Gets a string from the user.
2. mostcount = 1 — Stores the highest frequency found so far.
3. secondmostcount = 1 — Stores the second-highest frequency.
4. secondcountchar = "" — Stores the second most frequent character.
5. for i in str1: — Checks each character in the string.
6. str1.count(i) — Counts how many times the character appears.
7. if str1.count(i) > mostcount: — Checks whether its count is greater than the current highest count.
8. mostcount = str1.count(i) — Updates the highest count.
9. The second for loop checks each character again.
10. str1.count(i) < mostcount — Checks that the character is not the most frequent.
11. str1.count(i) > secondmostcount — Checks whether its count is greater than the current second-highest count.
12. secondmostcount = str1.count(i) — Updates the second-highest count.
13. secondcountchar = i — Stores that character.
14. print(...) — Displays the answer.
How it works: The first loop finds the highest count. The second loop finds the highest count that is smaller than the highest count.


==================================================================================================================================================
Simple explanation of each line
1. str1 = input(...) — Gets a string from the user.
2. mostcount = 1 — Stores the highest frequency.
3. scount = 1 — Stores the second-highest frequency.
4. scountchar = "" — Stores the second most frequent character.
5. for i in str1: — Checks each character in the string.
6. str1.count(i) — Counts the occurrences of the current character.
7. if str1.count(i) > mostcount and str1.count(i) > scount: — Checks whether the current count is greater than both stored counts.
8. scount = mostcount — Moves the old highest count into the second-highest position.
9. mostcount = str1.count(i) — Updates the highest count.
10. elif str1.count(i) < mostcount and str1.count(i) > scount: — Checks whether the current count is between the highest and second-highest counts.
11. scount = str1.count(i) — Updates the second-highest count.
12. scountchar = i — Stores the character.
13. else: pass — Does nothing if neither condition is true.
14. print(...) — Displays the result.
Important: Your second method has a small issue: when a new highest count is found, it updates scount but does not update scountchar to the character that previously had the second-highest count. So it may print an incorrect result.
Also, both methods can fail to return the right answer when different characters share the same frequency. For beginner practice, Method 1 is easier to understand, but it should be adjusted if you want to handle ties correctly.
"""

#6. or=====================================
# 6. Find the Second Most Frequent Character
# Sample Input: "aaabbccccdd"
# Sample Output: "b"

# name = "aaababbcddcdae"
name=input("Enter string: ")
max = 0
second_max = 0
max_char=""
for i in name:
    count = name.count(i)
    if count > max:
        second_max = max
        second_char = max_char
        max = count
        max_char = i
    elif count > second_max and i != max_char:
        second_max = count
        second_char = i

print(f"{second_char} has second max occurrence {second_max}")

# Explanation of each line
# 1. name = input("Enter string: ")
#    Gets a string from the user.
# 2. max = 0
#    Stores the highest occurrence count.
# 3. second_max = 0
#    Stores the second-highest occurrence count.
# 4. max_char = ""
#    Stores the character that occurs the most.
# 5. for i in name:
#    Checks each character in the string one by one.
# 6. count = name.count(i)
#    Counts how many times the current character appears.
# 7. if count > max:
#    Checks whether the current character's count is greater than the highest count.
# 8. second_max = max
#    Moves the old highest count to the second-highest position.
# 9. second_char = max_char
#    Stores the previous most frequent character as the second character.
# 10. max = count
#     Updates the highest count.
# 11. max_char = i
#     Stores the current character as the most frequent character.
# 12. elif count > second_max and i != max_char:
#     If the first condition is false, checks whether the count is greater than the second-highest count and the character is not the most frequent character.
# 13. second_max = count
#     Updates the second-highest count.
# 14. second_char = i
#     Stores the second most frequent character.
# 15. print(...)
#     Displays the second most frequent character and its count.
# Example
# Input:
# aaabbccccdd


# Character	Occurrences
# a	3
# b	2
# c	4
# d	2
# Output:
# a has second max occurrence 3


# Remember:
# - max → highest count.
# - second_max → second-highest count.
# - max_char → most frequent character.
# - second_char → second most frequent character.
# Note: This code finds the character with the second-highest distinct frequency. If two characters tie, the result depends on the order in which the characters are processed.