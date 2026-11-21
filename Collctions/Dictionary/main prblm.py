# dictionary[outer_key][inner_key] >> 101 102 103 all are the dict inside the dict students which is outer dict
# 5th nov 2026================================================= 

students ={
    101:{"name": "ann", "age": 22, "mark": 100},
    102:{"name": "manu", "age": 24, "mark": 97},
    103:{"name": "ram", "age": 21, "mark": 77}
}
# 1. Print age of student 102
print(students[102]["age"])

# 2. Print mark of student 103
print(students[103]["mark"])

# 3. Print name of student 102
print(students[102]["name"])

# 4. Update mark of student 101 to 95
students[101]["mark"] = 95

# 5. Add a new student 104
students[104] = {"name": "anu", "age": 23, "mark": 90}

#================1. Print student IDs (keys)========================================================
for i in students:
    print(i)
#  o/p:
# 101
# 102
# 103

# When you directly use for i in students, Python iterates through the keys of the dictionary by default.
# ====================2. Print complete student details (values)=======================================
for i in students.values():
    print(i)
    
# ============================4. Print only student names=====================================================
for i in students:
    print(students[i]["name"])
# o/p:
# ann
# manu
# ram

#========================print age and mark of all students from the dict============================
for i in students:
    print("Age:", students[i]["age"])
    print("Mark:", students[i]["mark"])
# or== print("Age:", students[i]["age"],"Mark:", students[i]["mark"])
    
# Understand the logic
# - for i in students: → Gets 101, 102, 103.
# - students[i] → Gets each student's inner dictionary.
# - students[i]["age"] → Gets the age.
# - students[i]["mark"] → Gets the mark.

#==========print the mark of student ram===========================================================================
for i in students:
    if students[i]["name"] == "rahul":
        print(students[i]["mark"])

# How it works:
# 1. for i in students: → Iterates through student IDs.
# 2. students[i]["name"] → Checks each student's name.
# 3. if ... == "rahul" → Finds Ram.
# 4. students[i]["mark"] → Prints Ram mark.

# ============================4. Print only student marks=====================================================
for i in students:
    print(students[i]["mark"])
# or== print(students[i]["mark"] for i in students)

#=============print the higehst mark====================================================
# Method 1: Using max() (easy)
marks = []
for i in students:
    marks.append(students[i]["mark"])
print(max(marks))

# Method 2: Using for loop (without max)
highest = 0
#name = ""
for i in students:
    if students[i]["mark"] > highest:
        highest = students[i]["mark"] # Highest mark: 97
        #name = students[i]["name"]
# print("Student:", name)
print("Highest mark:", highest)

# Understand the logic:
# - highest = 0 → Initially assume the highest mark is 0.
# - Compare each student's mark with highest.
# - If the mark is greater, update highest.
# - Finally, print the highest mark.


#--------------------------------------------------------------------------------------------------------
# Remember
# Method	What it returns
# students.keys()	Keys
# students.values()	Values
# students.items()	Both key and value
# for i in students	Keys by default

#-----------------------------------------------------------
# Think of it like this:
# Outer dictionary: students
# 101 → Inner dictionary

# name: ann | age: 22 | mark: 100

# 102 → Inner dictionary

# name: manu | age: 24 | mark: 97

# 103 → Inner dictionary

# name: ram | age: 21 | mark: 77

# Remember: i gets the outer dictionary's key. students[i] gets the corresponding inner dictionary.
