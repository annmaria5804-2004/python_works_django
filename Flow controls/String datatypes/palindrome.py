# wap to check hte given string is a palindrome or not ( palindrome means malayalm when reversed it is same as 1st )

name = input("enter the name: ")
print("palindrome" if name == name[::-1] else "not a palindrome")