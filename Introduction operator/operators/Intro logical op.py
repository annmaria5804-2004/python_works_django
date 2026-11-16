#  or------------------------logical operator------------24th sep
# True and True = True
# True and False = Flase
# False and False = False
# True or True = True
# False or True = True
# False or False = False



a = 10
b = 20 
c = 70
print((a<b) and (a<c)) # true
print((a>b) and (a<c)) # false
print((a<b) and (a>c)) # false
print((a>b) and (a>c)) # false


#or------------------------------

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print("Largest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("Largest number is:", num2)
else:
    print("Largest number is:", num3)
    
