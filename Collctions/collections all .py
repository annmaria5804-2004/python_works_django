"""
In Python collections, List, Set, and Dictionary are mutable, whereas Tuple is immutable.
Mutable vs Immutable
Collection	Mutable / Immutable	Meaning
List []	Mutable	Can change elements
Tuple ()	Immutable	Cannot change elements
Set {}	Mutable	Can add or remove elements
Dictionary {key:value}	Mutable	Can add, update or delete key-value pairs

1. List – Mutable
num = [10, 20, 30]num[0] = 100print(num)



Output:
[100, 20, 30]



2. Tuple – Immutable
num = (10, 20, 30)num[0] = 100



Output:
TypeError



Because tuple elements cannot be modified.
3. Set – Mutable
num = {10, 20, 30}num.add(40)print(num)



Output:
{10, 20, 30, 40}



4. Dictionary – Mutable
student = {"name": "Ann", "age": 22}student["age"] = 23print(student)



Output:
{'name': 'Ann', 'age': 23}



Easy way to remember
Mutable
 List, Set, Dictionary

Immutable
 Tuple

Interview question: Which Python collection is immutable?

Answer: Tuple is immutable.

Remember: Mutable means we can modify the original collection after creating it.
and diff of all


Here is the easy-to-understand difference between all four Python collections: List, Tuple, Set and Dictionary.
1. Difference between List, Tuple, Set and Dictionary
Feature	List	Tuple	Set	Dictionary
Syntax	[]	()	{}	{key:value}
Mutable	Yes	No	Yes	Yes
Ordered	Yes	Yes	No	Yes (insertion order)
Duplicates	Allowed	Allowed	Not allowed	Keys: No, Values: Yes
Indexing	Yes	Yes	No	Access using keys
Slicing	Yes	Yes	No	No
Elements	Any data type	Any data type	Any hashable type	Key-value pairs

2. Examples of each
1. List
- Uses square brackets [].
- Allows duplicate values.
- Maintains insertion order.
- Supports indexing and slicing.
- Mutable.
a = [10, 20, 30, 20]print(a[0])       # 10a.append(40)print(a)



Output: [10, 20, 30, 20, 40]

2. Tuple
- Uses parentheses ().
- Allows duplicate values.
- Maintains insertion order.
- Supports indexing and slicing.
- Immutable.
a = (10, 20, 30, 20)print(a[0])       # 10



3. Set
- Uses curly brackets {}.
- Does not allow duplicate values.
- Does not maintain insertion order.
- Does not support indexing or slicing.
- Mutable.
a = {10, 20, 30, 20}print(a)a.add(40)print(a)



Output (order may vary):
{10, 20, 30}{10, 20, 30, 40}



4. Dictionary
- Uses curly brackets {key: value}.
- Stores data in key-value pairs.
- Keys must be unique.
- Values can be duplicated.
- Maintains insertion order.
- Mutable.
student = {    "name": "Ann",    "age": 22,    "place": "Kerala"}print(student["name"])  # Annstudent["age"] = 23



3. Important methods
List	Tuple	Set	Dictionary
append()	count()	add()	keys()
extend()	index()	update()	values()
insert()		remove()	items()
remove()		discard()	get()
pop()		union()	pop()
sort()		intersection()	update()
reverse()		difference()	

4. Easy memory tricks
- List: Ordered, duplicates allowed, mutable.
- Tuple: Ordered, duplicates allowed, immutable.
- Set: Unique elements, no indexing, mutable.
- Dictionary: Key-value pairs, unique keys, mutable.
"""