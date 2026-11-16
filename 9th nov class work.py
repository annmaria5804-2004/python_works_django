# Question 1 – String: Character Frequency
# Logic:
# 1. Get a string from the user.
# 2. Convert it into lowercase.
# 3. Check each character.
# 4. Ignore spaces.
# 5. Count how many times each character appears.

def character_frequency(s):
    s = s.lower()

    for i in s:
        if i != " ": # If the character is not a space, continue.
            count = 0 # If it is a space, skip it.

            for j in s:
                if i == j:
                    count = count + 1

            # Check whether character was already counted
            already = False

            for k in s[:s.index(i)]: #s[:s.index(i)] checks the characters before its first occurrence.
                if k == i:
                    already = True # If the same character is found, already becomes True.

            if already == False:
                print(i, ":", count) # If the character has not appeared previously, print its frequency.


s = input("Enter a string: ")
character_frequency(s)

#or================================================================================
def character_frequency(s):
    s = s.lower()

    for i in range(len(s)): # len(s) finds the length of the string.
        if s[i] != " ": # Checks whether the current character is not a space.
            count = 0

            for j in range(len(s)): # Checks the current character against every character in the string and counts the matching characters.
                if s[i] == s[j]:
                    count = count + 1

            # Check previous characters
            duplicate = False # Checks whether the character already appeared at an earlier index.

            for k in range(i):
                if s[i] == s[k]:
                    duplicate = True

            if duplicate == False:
                print(s[i], ":", count)


s = input("Enter a string: ")
character_frequency(s)

#------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
# Question 2 – Nested List: Student Marks Analysis
# Logic:
# 1. Take each student's details.
# 2. First element is the name.
# 3. Remaining elements are marks.
# 4. Calculate total using a loop.
# 5. Calculate average using total / 3.
# 6. Compare totals to find the highest student.

students = [
    ["Arun", 85, 90, 78],
    ["Meera", 92, 88, 95],
    ["Rahul", 70, 80, 75],
    ["Anu", 80, 85, 90]
]


def student_analysis(students):

    highest = 0
    highest_name = ""

    for i in students:

        name = i[0] # i[0] means the first value in the inner list.
        total = 0

        for j in range(1, 4): # It skips index 0 because index 0 contains the student's name.
            total = total + i[j]

        average = total / 3

        print("Student:", name)
        print("Total Marks:", total)
        print("Average:", round(average, 2))
        print()

        if total > highest:
            highest = total
            highest_name = name

    print("Highest Scoring Student:", highest_name)
    print("Highest Total Marks:", highest)


student_analysis(students)

#----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
# Question 3 – Nested Dictionary: Employee Management
# Logic:
# 1. Use employees.items() to access employee ID and details.
# 2. Access name using details["name"].
# 3. Access department using details["department"].
# 4. Check salary using an if condition.
# 5. Compare salaries to find the highest.
# 6. Calculate average salary.

employees = {
    101: {"name": "Arun", "department": "Python", "salary": 45000},
    102: {"name": "Meera", "department": "Data Science", "salary": 60000},
    103: {"name": "Rahul", "department": "Testing", "salary": 40000},
    104: {"name": "Anu", "department": "Web Development", "salary": 55000}
}


def employee_analysis(employees):

    total_salary = 0
    count = 0

    highest_salary = 0
    highest_name = ""

    print("Employee Details:")

    for emp_id, details in employees.items():

        name = details["name"]
        department = details["department"]
        salary = details["salary"]

        print(emp_id, "-", name, "-", department)

        # Salary greater than 50000
        if salary > 50000:
            print("Salary above 50000:", name)

        # Calculate total salary
        total_salary = total_salary + salary
        count = count + 1

        # Find highest salary
        if salary > highest_salary:
            highest_salary = salary
            highest_name = name

    average = total_salary / count

    print()
    print("Highest Salary Employee:", highest_name)
    print("Highest Salary:", highest_salary)

    print("Average Salary:", average)


employee_analysis(employees)

#----------------------------------------------------------------------------------

# Important Python concepts to understand
# These are the main concepts used in all three questions.
# Concept	                   Meaning

# def	                   Create a function
# for i in students	       Access each student
# range(1, 4)	           Generate 1, 2, 3
# count = count + 1	       Increase count
# total = total + i[j]	   Add marks
# if salary > 50000	       Check a condition
# items()	               Access dictionary key and value
# details["name"]	       Access dictionary value