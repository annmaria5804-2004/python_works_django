"""14th oct 2026
An anagram is the word or phrase formed by reaaranging all the letters of anaother word or phrase excatly once.

common examaples:

listen > silent # Both contain the same letters in say way means all comes correct way
earth > heart # Both contain the same letters
secure > rescue # Both contain the same letters

>if any words letter reapt twice and in other 1 time then not anagram
> the length of both strings should be same then only can say as same number of letters and then only we can check letters 

# 2 input from user
"""
# or chagtgpt:
word1 = "listen"
word2 = "silent"

if sorted(word1) == sorted(word2):
    print("Anagram")
else:
    print("Not an Anagram")
"""
Why use sorted()?
sorted("listen") gives ['e', 'i', 'l', 'n', 's', 't'].
sorted("silent") gives ['e', 'i', 'l', 'n', 's', 't'].
Since both lists are equal, they are anagrams. 😊
"""
# sir....

word_1 ="silent"
word_2 ="Listen"

word_1 , word_2 = word_1.lower() , word_2.lower() # Converts both words to lowercase.
if len(word_1) == len(word_2): # Checks whether both words have the same length. Both have 6 letters.
    for i in range(len(word_1)): # Repeats the loop 6 times. i takes values from 0 to 5.
        if word_1.count(word_1[i]) !=  word_2.count(word_2[i]):# Checks whether the current letter from word_1 appears the same number of times in both words. .count() counts a letter.!= means not equal.
            print("they are not anagram") # If the counts are different, prints the result and stops the loop.
            break
    else:
        print("anagram")
else:
    print("not a anagram")