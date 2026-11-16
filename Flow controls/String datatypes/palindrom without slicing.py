# check the string plaindrom without using slicing

word = input("Enter a string: ")
reverse = "" # Creates an empty string to store the reversed word.

for i in word: #  Takes each character one by one.
    reverse = i + reverse # Adds each character to the beginning of reverse.
    # if word is python then 1st = p then y+p then t+yp then h+typ then o+htyp then n+ohtyp finally string over  and in reverse there is nohtyp as reverse name
if word == reverse: #  here revere not equal to python != nohtyp
    print("Palindrome")
else:
    print("Not a palindrome") # o/p the will be this for python

"""
Simple line-by-line explanation:
Suppose the input is madam.
1. word = input(...) — Gets the string from the user.
2. reverse = "" — Creates an empty string to store the reversed word.
3. for i in word: — Takes each character one by one.
4. reverse = i + reverse — Adds each character to the beginning of reverse.
5. if word == reverse: — Checks whether the original and reversed strings are equal.
6. If equal, prints Palindrome; otherwise, prints Not a palindrome.
"""