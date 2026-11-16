students = {
    "student1":{
        "name": "ANN",
        "marks":[97,100,95]
    },
     "student2":{
            "name": "MANU",
            "marks":[87,90,92]
        },
         "student3":{
                "name": "ELSI",
                "marks":[85,90,97]
            }
            
}

# 1. Return all keys
for i in students:
    print(i)

# 2. Return all values
for i in students:
    print(students[i])

# 3. Return both keys and values
for i in students:
    print(i, students[i])

# 4. Return student names
for i in students:
    print(students[i]["name"])

# 5. Return all marks
for i in students:
    print(students[i]["marks"])

# 6. Return student name and marks
for i in students:
    print(i, students[i]["name"], students[i]["marks"])

# 7. Return student names having marks above 90
for i in students:
    for j in students[i]["marks"]:
        if j > 90:
            print(students[i]["name"], j)

# 8. Return students whose all marks are above 90
for i in students:
    if all(j > 90 for j in students[i]["marks"]):
        print(students[i]["name"])

# 9. Return total marks of each student
for i in students:
    print(students[i]["name"], sum(students[i]["marks"]))

# 10. Return average marks of each student
for i in students:
    avg = sum(students[i]["marks"]) / len(students[i]["marks"])
    print(students[i]["name"], avg)

# 11. Return highest mark of each student
for i in students:
    print(students[i]["name"], max(students[i]["marks"]))

# 12. Return lowest mark of each student
for i in students:
    print(students[i]["name"], min(students[i]["marks"]))

# 13. Return students having total marks above 280
for i in students:
    if sum(students[i]["marks"]) > 280:
        print(students[i]["name"], sum(students[i]["marks"]))

# 14. Return students having average marks above 90
for i in students:
    avg = sum(students[i]["marks"]) / len(students[i]["marks"])
    if avg > 90:
        print(students[i]["name"], avg)

# 15. Return students having a mark of 100
for i in students:
    if 100 in students[i]["marks"]:
        print(students[i]["name"])

# 16. Return students having all marks above 85
for i in students:
    if all(j > 85 for j in students[i]["marks"]):
        print(students[i]["name"])

# 17. Return students having at least one mark below 90
for i in students:
    if any(j < 90 for j in students[i]["marks"]):
        print(students[i]["name"])

# 18. Return student name with highest total marks
highest = max(students, key=lambda i: sum(students[i]["marks"]))
print(students[highest]["name"])

# 19. Return student name with lowest total marks
lowest = min(students, key=lambda i: sum(students[i]["marks"]))
print(students[lowest]["name"])

# 20. Return all student names in uppercase
for i in students:
    print(students[i]["name"].upper())


# Function	Purpose
# keys()	Returns keys
# values()	Returns values
# items()	Returns keys and values
# sum()	Calculates total
# len()	Counts elements
# max()	Finds highest
# min()	Finds lowest
# all()	Checks whether all conditions are true
# any()	Checks whether at least one condition is true



# add 96 to the marks of ANN
for i in students:
    if students[i]["name"] == "ANN":
        students[i]["marks"].append(96)

print(students)
# or=========================
print(students["student1"])

# Explanation:
# - for i in students: → Iterates through students.
# - students[i]["name"] == "ANN" → Finds ANN.
# - append(96) → Adds 96 to the marks list.
# Remember: append() adds a new element to the end of a list.

print(students["student1"]) # print the student 1 name marks only 
print(students["student1"]["name"]) # print student1 name
print(students["student1"]["marks"]) # print student1 marks

# add ta new student the the students dict with name as jack and marks as 80,77,75
students["student4"] = { # Creates a new student.
    "name": "JACK",
    "marks": [80, 77, 75]
}

print(students) 
# or===============================
print(students["student4"]) # {'name': 'JACK', 'marks': [80, 77, 75]}

# find the max marks of 
for i in students:
    if students[i]["name"] == "ANN":
        print(max(students[i]["marks"])) # - max() → Returns the highest mark.