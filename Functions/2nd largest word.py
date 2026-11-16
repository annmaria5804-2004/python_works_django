# . Second Longest Word
# Input: Python is an amazing programming language
# Output: language

sentence = "Python is an amazing programming language"

words = sentence.split()

words.sort(key=len)

print(words[-2])

# or=====================================================
sentence = "Python is an amazing programming language"

words = sentence.split()

longest = ""

for i in words:
    if len(i) > len(longest):
        longest = i

print(longest)