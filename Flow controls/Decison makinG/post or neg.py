# post or neg
num = int(input("enter the number : "))
if num > 0:
    print(f"the number {num} is positive")
    #or-------------------
    print("the number",num, "is positive")
else:
    print(f"the number {num} is negative")
    # orrr can write as-------------
    print("the number",num, "is negaive")
    
    
# or--------------------
num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")