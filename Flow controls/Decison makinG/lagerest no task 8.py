# get largest no. among 3 nos enter by user     nested if-----------------

num1 = int(input("Enter your no.1: "))
num2 = int(input("Enter your no.2: "))
num3 = int(input("Enter your no.3: "))

if num1 > num2:
    if num1 > num3:
        print(f"The largest num is {num1}")
    else:
        print(f"The largest num is {num3}")
elif num2 > num3:
        print(f"The largest num is {num2}")
else:
    print(f"The largest num is {num3}")


# or----------------------
# Get largest number among 3 numbers entered by user

num1 = int(input("Enter your no.1: "))
num2 = int(input("Enter your no.2: "))
num3 = int(input("Enter your no.3: "))

if num1 > num2:
    if num1 > num3:
        print(f"The largest num is {num1}")
    else:
        print(f"The largest num is {num3}")
else:
    if num2 > num3:
        print(f"The largest num is {num2}")
    else:
        print(f"The largest num is {num3}")
        
        
#  or------------------------logical operator------------
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print("Largest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("Largest number is:", num2)
else:
    print("Largest number is:", num3)
    
#or------------------------------
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("Largest number is:", max(a, b, c))