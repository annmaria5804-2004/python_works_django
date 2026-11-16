# wap all zeros in a list to the end without changing the order of the other elements (o/p: [1, 2, 3, 4, 5, 6, 0, 0, 0])

num = [1, 0, 2, 3, 0, 4, 0, 5, 6]

for i in num.copy():
    if i == 0:
        num.remove(i)
        num.append(i)

print(num)


# Explanation
# - num.copy() lets you iterate over a copy while modifying the original list.
# - if i == 0: checks whether the element is zero.
# - num.remove(i) removes the zero from the list.
# - num.append(i) adds that zero to the end.
# This keeps the non-zero elements in their original order and moves all zeros to the end.