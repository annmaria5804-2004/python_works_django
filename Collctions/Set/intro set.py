# # set====================================================
# -------------------------------------------------------------------
# it is defined as set()
#  duplicates are not alloweded
#  order of elements cannot be preserved
# no index postion in set
# it is heterogeneous
# it is itreable

elements = {"1",1,True,"hello",2,"python","hello",7.5}
for i in range(3):
    print(elements)
# Explanation:
# - A set does not allow duplicate elements, so "hello" appears only once.
# - 1 and True are considered equal in Python sets, so only one of them is kept.
# - The order of elements is not guaranteed.
# - The loop prints the same set three times.

elements = {"1", 1, True, "hello", 2, "python", "hello", 7.5}

elements.add("ann")
print(elements)

elements.remove("1")
print(elements)

elements.pop()
print(elements)
elements.discard("ann")


set1={1,2,3,4,5,6,7}
set2={5,6,7,8,9,10}
print(set1.union(set2)) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Explanation
# - union() combines the elements of both sets.
# - Duplicate elements (5, 6, 7) appear only once.
# - The original sets remain unchanged.

# or==================================
print(set1 | set2) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# Both set1.union(set2) and set1 | set2 produce the same result.

set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {5, 6, 7, 8, 9, 10}

print(set1.intersection(set2)) # {5, 6, 7}

# Explanation:
# - intersection() returns only the elements that exist in both sets.
# - The common elements are 5, 6, 7.
# or==============================================
print(set1 & set2) # {5, 6, 7}
# Remember:
# - union() → All unique elements from both sets.
# - intersection() → Only common elements from both sets.

set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {5, 6, 7, 8, 9, 10}

print(set1.difference(set2)) # {1, 2, 3, 4}
print(set2.difference(set1))  # {8, 9, 10}
# set1.difference(set2) → Elements in set1 but not in set2.
# set2.difference(set1) → Elements in set2 but not in set1.

print(set1 - set2) # {1, 2, 3, 4}
print(set2 - set1) # {8, 9, 10}

# Important: Difference is directional. set1 - set2 and set2 - set1 give different results.