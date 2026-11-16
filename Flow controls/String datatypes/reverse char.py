"""Write a Python program to reverse all characters in a given string that appear before the first occurrence of a "p". 
  The "p" should not be reversed. If the character is not found, the entire string should be reversed.

  eg:  "hellopython"

  o/p : "ollehpython"
  """
  
# sir:
word ="hellopython"
for i in word:  # i = h
    if i == "p":  # i == p
       print("the word is",word[0:word.index(i)][::-1] + word[word.index(i)::]) # word[0:5][::-1] "olleh"
       break
else:
    print(word[::-1])


"""
Simple explanation
1. for i in word: — checks each character in the string.
2. if i == "p": — checks whether the character is p.
3. word[0:word.index(i)][::-1] — takes hello and reverses it to olleh.
4. word[word.index(i)::] — takes python without changing it.
5. print(...) — joins both parts and prints ollehpython.
6. break — stops the loop when p is found.
7. else — belongs to the for loop. It executes only if the loop finishes without a break, so if p is absent, it prints the entire reversed string.
Important: break must be inside the if block. If you put it outside, the loop stops after checking only the first character.
"""

#or:
  
name = input("Enter the string: ")

if "p" in name:
   pos = name.index("p")
   result = name[:pos][::-1] + name[pos:]
else:
   result = name[::-1]

print(result)
