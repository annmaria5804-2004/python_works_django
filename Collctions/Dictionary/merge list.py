keys = ["name","age","place"]
values = ["ann",22,"kochi"]
elements = {}

for i in range(len(keys)):
    elements[keys[i]] = values[i]

print(elements) # {'name': 'ann', 'age': 22, 'place': 'kochi'}

# Important concepts
# - range(len(keys)) → Generates index values 0, 1, 2.
# - keys[i] → Gets the key from the first list.
# - values[i] → Gets the corresponding value from the second list.
# - elements[keys[i]] = values[i] → Adds a key-value pair to the dictionary.
# Remember: When you write elements[key] = value, Python adds that key-value pair to the dictionary. If the key already exists, its value gets updated.

# or===========================================================
# Using dictionary comprehension
elements = {keys[i]: values[i] for i in range(len(keys))}

print(elements) # {'name': 'ann', 'age': 22, 'place': 'kochi'}