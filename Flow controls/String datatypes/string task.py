name = "aaabbcddd"
new= ""
for i in name: # i = a counts how many times the character appears in the original string.
    if i not in new: #  avoids repeating characters.
      count = name.count(i) # counts the character in the original string.
      new += i + str(count) # a3 b2    stores the character and its count.
print(new) # o/p: a3b2c1d3

"""
Simple explanation
- name.count(i) counts how many times the character appears in the original string.
- str(count) converts the count into a string.
- new += i + str(count) adds the character and its count to new.
Remember these three important lines:
- if i not in new: → avoids repeating characters.
- name.count(i) → counts the character in the original string.
- new += i + str(count) → stores the character and its count.
"""