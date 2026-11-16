
# WAP to get the total number of characters in a string

# usig function:
name = input("Enter a string: ")

print("Total number of characters:", len(name))


# without using len function:
name = input("Enter a string: ")

count = 0

for i in name:
    count += 1

print("Total number of characters:", count)




