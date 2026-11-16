# rotation the list by 3 times
numbers = [1,2,3,4,5,6,7,8]
# o/p: [6,7,8,1,2,3,4,5]
#[8,1,2,3,4,5,6,7] >> [7,8,1,2,3,4,5,6] >> [6,7,8,1,2,3,4,5]

for i in range(3):
    elements = numbers.pop()
    numbers.insert(0,elements)
print(numbers)

"""
How it works
- numbers.pop() removes the last element.
- numbers.insert(0, elements) inserts that element at index 0 (the beginning).
- range(3) repeats these steps 3 times.
Step-by-step rotation:
1. [8, 1, 2, 3, 4, 5, 6, 7]
2. [7, 8, 1, 2, 3, 4, 5, 6]
3. [6, 7, 8, 1, 2, 3, 4, 5]
"""

