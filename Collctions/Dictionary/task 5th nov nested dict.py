
# Python Practice – Nested Collections
# Nested Lists & Nested Dictionaries
# =========================================================


# PART A – NESTED LISTS (QUESTIONS 1–5)


# 1. Row-wise and Column-wise Sum

def row_column_sum(marks):
    rows = len(marks)
    cols = len(marks[0])

    # Student totals (row-wise)
    for i in range(rows):
        total = 0
        for j in range(cols):
            total += marks[i][j]
        print(total, end=" ")
    
    print()

    # Subject totals (column-wise)
    for j in range(cols):
        total = 0
        for i in range(rows):
            total += marks[i][j]
        print(total, end=" ")


marks = [
    [80, 75, 90],
    [65, 85, 70],
    [90, 95, 85]
]

row_column_sum(marks)


# 2. Find the Largest Element in Each Row

def largest_row(numbers):
    for row in numbers:
        largest = row[0]

        for num in row:
            if num > largest:
                largest = num

        print(largest)


numbers = [
    [12, 45, 23],
    [67, 34, 89],
    [21, 90, 56]
]

largest_row(numbers)


# 3. Transpose a Matrix

def transpose(numbers):
    rows = len(numbers)
    cols = len(numbers[0])

    for j in range(cols):
        for i in range(rows):
            print(numbers[i][j], end=" ")
        print()


numbers = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

transpose(numbers)


# 4. Find the Second Largest Element in Each Row

def second_largest(numbers):
    for row in numbers:
        largest = row[0]
        second = row[1]

        if second > largest:
            largest, second = second, largest

        for num in row[2:]:
            if num > largest:
                second = largest
                largest = num
            elif num > second:
                second = num

        print(second)


numbers = [
    [10, 50, 30, 40],
    [80, 20, 60, 90],
    [15, 45, 35, 25]
]

second_largest(numbers)


# 5. Find Common Elements Between Two Nested Lists

def common_elements(list1, list2):
    result = []

    for row1 in list1:
        for num1 in row1:

            found = False

            for row2 in list2:
                for num2 in row2:
                    if num1 == num2:
                        found = True

            if found and num1 not in result:
                result.append(num1)

    print(result)


list1 = [
    [10, 20, 30],
    [40, 50, 60]
]

list2 = [
    [30, 40, 70],
    [80, 10, 90]
]

common_elements(list1, list2)


# =========================================================
# PART B – NESTED DICTIONARIES (QUESTIONS 6–10)
# =========================================================


# 6. Student Mark Analysis

def student_analysis(students):
    for student_id, details in students.items():

        name = details["name"]
        marks = details["marks"]

        total = 0
        passed = True

        for mark in marks:
            total += mark

            if mark < 40:
                passed = False

        average = total / len(marks)

        if passed:
            result = "Pass"
        else:
            result = "Fail"

        print(name, "- Total:", total,
              "Average:", format(average, ".2f"),
              result)


students = {
    101: {"name": "Arun", "marks": [80, 75, 90]},
    102: {"name": "Meera", "marks": [35, 60, 70]},
    103: {"name": "Rahul", "marks": [90, 85, 95]}
}

student_analysis(students)


# 7. Employee Salary Analysis

def salary_analysis(employees):
    departments = {}

    highest_salary = 0
    highest_employee = ""

    for emp_id, details in employees.items():

        name = details["name"]
        department = details["department"]
        salary = details["salary"]

        if department not in departments:
            departments[department] = 0

        departments[department] += salary

        if salary > highest_salary:
            highest_salary = salary
            highest_employee = name

    for department, total in departments.items():
        print(department, ":", total)

    print("Highest Salary:", highest_employee, "-", highest_salary)


employees = {
    101: {"name": "Arun", "department": "Python", "salary": 30000},
    102: {"name": "Meera", "department": "Data Science", "salary": 45000},
    103: {"name": "Rahul", "department": "Python", "salary": 35000},
    104: {"name": "Anu", "department": "Data Science", "salary": 40000}
}

salary_analysis(employees)


# 8. Product Inventory Management

def inventory_analysis(inventory):
    print("Stock Values:")

    for product_id, details in inventory.items():

        name = details["name"]
        quantity = details["quantity"]
        price = details["price"]

        stock_value = quantity * price

        print(name, ":", stock_value)

    print("Low Stock Products:")

    for product_id, details in inventory.items():

        if details["quantity"] < 10:
            print(details["name"])


inventory = {
    "P101": {"name": "Laptop", "quantity": 5, "price": 45000},
    "P102": {"name": "Mouse", "quantity": 20, "price": 500},
    "P103": {"name": "Keyboard", "quantity": 8, "price": 1200},
    "P104": {"name": "Monitor", "quantity": 12, "price": 10000}
}

inventory_analysis(inventory)


# 9. Movie Rating Analysis

def movie_analysis(movies):
    highest_rating = 0
    highest_movie = ""

    for movie, details in movies.items():

        ratings = details["ratings"]

        total = 0

        for rating in ratings:
            total += rating

        average = total / len(ratings)

        print(movie, ":", average)

        if average > highest_rating:
            highest_rating = average
            highest_movie = movie

    print("Highest Rated Movie:", highest_movie)


movies = {
    "Inception": {"ratings": [8, 9, 10, 9]},
    "Interstellar": {"ratings": [10, 9, 9, 10]},
    "Avatar": {"ratings": [7, 8, 9, 8]}
}

movie_analysis(movies)


# 10. Shopping Cart Billing System

def shopping_bill(customers):
    highest_bill = 0
    highest_customer = ""

    for customer_id, details in customers.items():

        name = details["name"]
        cart = details["cart"]

        total = 0

        for product in cart:
            quantity = product["quantity"]
            price = product["price"]

            total += quantity * price

        print(name, ":", total)

        if total > highest_bill:
            highest_bill = total
            highest_customer = name

    print("Highest Spending Customer:", highest_customer)


customers = {
    101: {
        "name": "Arun",
        "cart": [
            {"product": "Laptop", "quantity": 1, "price": 45000},
            {"product": "Mouse", "quantity": 2, "price": 500}
        ]
    },
    102: {
        "name": "Meera",
        "cart": [
            {"product": "Mobile", "quantity": 1, "price": 25000},
            {"product": "Headphone", "quantity": 2, "price": 1500}
        ]
    },
    103: {
        "name": "Rahul",
        "cart": [
            {"product": "Keyboard", "quantity": 2, "price": 1200},
            {"product": "Monitor", "quantity": 1, "price": 10000}
        ]
    }
}

shopping_bill(customers)


# Questions 4, 5, 7 and 10 carefull