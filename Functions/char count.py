# wap to get the total count of vowels fro the string enter by user using function.

def count_vowels(s):
    count = 0
    for i in s:
        if i.lower() in "aeiou":
            count += 1
    print(count)

s = input("Enter a string: ")
count_vowels(s)
# Enter a string: AnnMaria = 4

# or...................................

# WAP to get the total count of vowels from a string using a function

def count_vowels(s):
    count = 0
    for i in s:
        if i in "aeiouAEIOU":
            count += 1
    return count

s = input("Enter a string: ")
result = count_vowels(s)
print("Total number of vowels:", result)

# RETURN is a statement inside a function to send a specific o/p or result
# or value back to the function caller line
