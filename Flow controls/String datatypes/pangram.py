# a pangram is a snetence , pharse , or word thar uses every letter of a given alaphabet at least once (A pangram contains every letter of the English alphabet (a to z) at least once.)

sentence = "The quick brown fox jumps over the lazy dog"

count = 0
alphabets ="abcdefghijklmnopqrstuvwxyz"

for i in alphabets : # or "abcdefghijklmnopqrstuvwxyz":
    # or  if i not in sentence.lower():
      #     print("pangram")
       #    break
    if i in sentence.lower():
      count += 1

if count == 26:
   print("Pangram") # o/p: Pangram
else:
   print("Not a pangram") 

"""
Simple explanation
1. count = 0 — starts the count at zero.
2. for i in "abcdefghijklmnopqrstuvwxyz": — checks all 26 English letters one by one.
3. sentence.lower() — converts the sentence to lowercase.
4. if i in sentence.lower(): — checks whether each letter is present in the sentence.
5. count += 1 — increases the count when the letter is found.
6. if count == 26: — if all 26 letters are present, it is a pangram.
Remember: "The quick brown fox jumps over the lazy dog" is a pangram because it contains every letter from a to z at least once.
"""