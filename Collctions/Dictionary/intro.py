# Dictionar  29/10/2026
# ======================================================
"""   
> Eelements should be in {key:value} pair
> it is defined as {} , dict()
> keys should be in str, or tuple. immutable
> keys cannot be duplicated later values overwrite earlier ones.
>it is iterable(loop form)
> order of elemnts are maintained
> Insertion order is maintained.
> Remember: a dictionary stores data as key:value pairs, and you normally access each value using its key.
> dict[key] return the values of the key given



"""
elements_dict = {"name":"ann","age":22,"place":"kasaragod"}
for i in range(10):
    print(elements_dict)
    
# or==========================================
print(elements_dict["name"])   # ann
print(elements_dict["age"])    # 22

# or===========================================
for i in elements_dict:
    print(i) # name age place 
    
# or==============================================
elements_dict["course"] = "Python"  # Add
elements_dict["age"] = 23           # Update

print(elements_dict) # {'name': 'ann', 'age': 23, 'place': 'kasaragod', 'course': 'Python'}

# or========access the elements sepaetrtely===============================
elemnets = ["a","b",1]
print(elemnets [1]) # b
print(elemnets [2]) # 1
print(elemnets [0]) # a

# or===============================================
# my = [("name":"ann"),("age":22,),("place":"kasaragod")]
items = []

for i in elements_dict:
    items.append((i, elements_dict[i])) # [('name', 'ann'), ('age', 23), ('place', 'kasaragod'), ('course', 'Python')]

print(items)


print(elements_dict.get("name")) # ann
# to return the values from the key given > dictionary.get(key) → Returns the value or None if the key doesn't exist.
# elements["name"] # key error > dictionary[key] → Returns the value or raises KeyError.


print(elements_dict.keys())  # dict_keys(['name', 'age', 'place', 'course'])  > Returns all keys
print(elements_dict.values()) # dict_values(['ann', 23, 'kasaragod', 'Python']) > 	Returns all values

print(elements_dict.items())  # items()	Returns key-value pairs >o/p: dict_items([('name', 'ann'), ('age', 23), ('place', 'kasaragod'), ('course', 'Python')])


# Convert keys and values into list
print(list(elements_dict.keys()))
print(list(elements_dict.values()))
# o/p: ['name', 'age', 'place', 'course']
 # o/p:['ann', 23, 'kasaragod', 'Python']
 
 
# print(elements_dict.pop()) # pop common way inside pop enter any key then it will pop
print(elements_dict.pop("name")) # ann
print(elements_dict) # {'age': 23, 'place': 'kasaragod', 'course': 'Python'}

print(elements_dict.popitem()) # pop and gaves last elemets in the dict >> o/p: ('course', 'Python') 

#============diff of tuple set dict==============================================================================
"""
1. Tuple ()
A tuple is an ordered and immutable collection(unchanged).
- Ordered – maintains insertion order.
- Immutable – cannot add, remove, or change elements after creation.
- Allows duplicate values.
- Supports indexing.

eg:
a = (10, 20, 30, 20)

print(a)
print(a[0])
print(a[2])

o/p:
(10, 20, 30, 20)
10
30
========================================================================================================
2. Set {}
A set is an unordered collection of unique elements.
- Unordered - does not support indexing.
- Mutable - can add or remove elements.
- Does not allow duplicate values.
- Does not support indexing.

eg:
a = {10, 20, 30, 20, 40}
print(a)

o/p:
{10, 20, 30, 40}
==================================================================================================================

3. Dictionary {key: value}
A dictionary stores data in key-value pairs.
- Ordered - maintains insertion order.
- Mutable - can add, remove, and update values.
- Keys must be unique.
- Values can have duplicates.
- Access values using keys, not indexes.

eg:
student = {
    "name": "Ann",
    "age": 22,
    "place": "Kerala"
}

print(student["name"])
print(student["age"])

o/p:
Ann
22

======================================================================================
pop in all 3 :
Easy way to remember:
- Tuple → No pop.
- Set → pop() removes an arbitrary element.
- Dictionary → pop("key") removes a key-value pair.
- List → pop(index) removes an element by index.


"""