#Palindrome List
# Input: ['madam','apple','level','python','radar']
# Output: ['madam','level','radar']

# Input
words = ['madam', 'apple', 'level', 'python', 'radar']

items = []

for i in words:
    if i == i[::-1]:
        items.append(i)

print(items)

# Explanation:
# - for i in words → Iterates through each word.
# - i[::-1] → Reverses the word.
# - i == i[::-1] → Checks whether the word is a palindrome.
# - append(i) → Adds the palindrome word to the new list.
