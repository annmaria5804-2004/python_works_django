students = {
    "Ann":[97,100,95],
    "Manu":[87,90,92] ,
    "Ram":[85,90,97]
}
# print all marks of ann ==================================================
print(students["Ann"])

# print all marks of ann for loop====================================
for i in students["Ann"]:
    print(i)

# print all marks of ann  condition=======================================
for i in students:
    if i == "Ann":
      print(students[i])
      
# return the total marks of each strudents in onter lisr sum  with name of each===========

for i in students:
    total = sum(students[i])
    print(i, ":", total)
# Ann : 292
# Manu : 269
# Ram : 272

# Without using sum() (manual method)=====================
for i in students:
    total = 0
    for j in students[i]:
        total = total + j
    print(i, total)
# Here:
# - i represents the student name.
# - j represents each mark.
# - total stores the sum of marks.
# Important: Practise the second method too. It helps you understand nested for loops, which are important in Python.
    
# or >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
print([sum(students[i]) for i in students]) # [292, 269, 272]

# add a new mark 70 to mark list ram==============================================
students["Ram"].append(70)
print(students) # {'Ann': [97, 100, 95], 'Manu': [87, 90, 92], 'Ram': [85, 90, 97, 70]}
print(students["Ram"]) # [85, 90, 97, 70]
# Remember: append() adds one new element to an existing list.

# return the  max mark of each students=============================================== 
# Method 1: Using max()
for i in students:
    print(i, ":", max(students[i])) # max(students[i]) → Finds the highest mark in that list.
    
# Method 2: Without using max() (using nested loops)
for i in students:
    highest = 0
    for j in students[i]:
        if j > highest:
            highest = j
    print(i, ":", highest)
#------------------------------------------------------------------------   
# Ann : 100
# Manu : 92
# Ram : 97

# .......................................======================
# Remember:
# - sum() → Total marks.
# - max() → Highest mark.
# - min() → Lowest mark.
# - len() → Number of marks.
# Try Method 2 to practise nested for loops and if conditions.