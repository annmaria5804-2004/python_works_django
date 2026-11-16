# wap to remove the even numbers from the given list
num = [3,5,1,2,4,7,6,11,10,13,20]
num = [3, 5, 1, 2, 4, 7, 6, 11, 10, 13, 20]

new_list = []

for i in num:
    if i % 2 != 0:
        new_list.append(i)

print(new_list)



# num = [3, 5, 1, 2, 4, 7, 6, 11, 10, 13, 20]new_list = []for i in num:    if i % 2 != 0:        new_list.append(i)print(new_list)
# Output
# [3, 5, 1, 7, 11, 13]

# Explanation
# - for i in num: — takes each number from the list.
# - i % 2 != 0 — checks whether the number is odd.
# - new_list.append(i) — adds only odd numbers to the new list.
# - print(new_list) — displays the list without even numbers.
# Remember: % 2 == 0 checks for even numbers, while % 2 != 0 checks for odd numbers.

# corect..................................................................................................
num = [3, 5, 1, 2, 4, 7, 6, 11, 10, 13, 20]

for i in num.copy():
    if i % 2 == 0:
        num.remove(i)

print(num)
# \
#     How does num.copy() work?
# - num.copy() creates a copy of the original list.
# - for i in num.copy(): iterates through the copied list.
# - if i % 2 == 0: checks whether the number is even.
# - num.remove(i) removes that even number from the original list.
# Why use num.copy()?

# When you remove elements from a list while iterating over that same list, some elements may be skipped. Using num.copy() avoids this problem because you iterate over the copy while modifying the original list.