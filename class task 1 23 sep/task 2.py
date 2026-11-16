# SESSION 2 — Simple Decision Making

# 1. Positive or Negative
num = int(input("Enter a number: "))
if num > 0:
       print(f"the number {num} is positive")
elif num < 0:
       print(f"the number {num} is negative")
else:
    print("Zero")


# 2. Even or Odd
num = int(input("enter the number : "))
if num % 2 == 0:
    print(f"the number {num} is even")
else:
    print(f"the number {num} is odd")


# 3. Pass or Fail
mark = int(input("Enter your mark: "))
if mark >= 70:
    print("Pass")
else:
    print("Fail")

# 4. Voting Eligibility
age = int(input("Enter your age: "))
if age >= 18:
    print(" you are eligible to vote")
else:
    print("not eligible to vote")


# 5. Greater Number
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
if num1 > num2:
    print("Greater number:", num1)
else:
    print("Greater number:", num2)


# 6. Temperature Category
temperature = float(input("Enter temperature: "))
if temperature > 27:
    print("Hot")
elif temperature < 12:
    print("Cold")
else:
    print("Normal")
    
# 7. Discount Calculator
amount = float(input("Enter total amount: "))
if amount >= 5000:
    discount = amount * 20 / 100
elif amount >= 2000:
    discount = amount * 10 / 100
else:
    discount = 0
final_amount = amount - discount
print("Discount:", discount)
print("Final Amount:", final_amount)

# 8. Grade Calculator
mark = int(input("Enter your mark: "))
if mark >= 90:
    print("Grade A")
elif mark >= 80:
    print("Grade B")
elif mark >= 75:
    print("Grade C")
elif mark >= 50:
    print("Grade D")
else:
    print("Fail")