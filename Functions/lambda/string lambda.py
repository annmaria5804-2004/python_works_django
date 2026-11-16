# using a function
# input >> " python is a progrmming language"
# o/p: >> {"python" :6,"is":2, "a":1, "programming":11, "language":8}
# ===============================================================================
# You need to create a dictionary where:
# - Key = Each word in the sentence.
# - Value = Number of characters in that word.
# You can do this using a lambda function with dictionary comprehension.

# 1. Using Lambda function
#================================================================
sentence = "python is a programming language"

result = lambda text: {word: len(word) for word in text.split()}

print(result(sentence))

# Hint: Use these three concepts:
# 1. split() – separate words.
# 2. len() – count characters.
# 3. Dictionary comprehension – create key-value pairs.












# =============================================================================================
# normal function prgm:==================================================================================
def word_count(sentence):
    words = sentence.split()
    result = {}

    for word in words:
        result[word] = len(word)

    return result

print(word_count("python is a programming language"))

# Hint:
# 1. Use split().
# 2. Create an empty dictionary.
# 3. Use a for loop.
# 4. Use len() to count characters.
# 5. Return the dictionary.