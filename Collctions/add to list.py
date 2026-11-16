# create a list and ask the user to enter the value and ass it to list until the user enter the number 40

numbers = []

while True:
    num = int(input("Enter a number: "))

    if num == 40:
        break

    numbers.append(num)

print(numbers) # Enter a number: 20
# Enter a number: 30
# Enter a number: 40
# [10, 20, 30]

# How it works
# 1. numbers = [] — Creates an empty list.
# 2. while True: — Repeats the loop continuously.
# 3. input() — Asks the user to enter a number.
# 4. if num == 40: — Checks whether the user entered 40.
# 5. break — Stops the loop if the number is 40.
# 6. numbers.append(num) — Adds the number to the list if it is not 40.
# Note: In this program, 40 is only the stopping value, so it is not added to the list.