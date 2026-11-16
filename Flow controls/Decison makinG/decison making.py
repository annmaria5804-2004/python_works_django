# decision making-------------23/09/24-------------

# the process of controlling the flow of the prgm based on specific conditions called as decison making.

#syntax=======
# if condition:
     # statement
# else:
     # statement
     
num = int(input("enter the number : "))
if num % 2 == 0:
    print(f"the number {num} is even")
    #or-------------------
    print("the number",num, "is even")
else:
    print(f"the number {num} is odd")
    # orrr can write as-------------
    print("the number",num, "is odd")