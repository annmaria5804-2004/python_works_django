# wap to return word from the string enter by user
text = "python is the programming lanuage"

words = text.split()
print(words)
largest = words[0]

for word in words:
    if len(word) > len(largest):
        largest = word

print("Largest word:", largest)

# How it works:
# - split() separates the string into individual words using spaces.
# - words stores those words in a list.
# - print(words) displays the list.

# largest = words[0] — Assumes the first word is the longest.
# len(word) > len(largest) — Checks whether the current word has more characters.
# largest = word — Updates the longest word.
# print() — Displays the longest word.