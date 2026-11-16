# wap  to return the factorial  of the given no.

num = int(input("Enter a number: "))
fact = 1
i = 1
while i <= num:
    fact = fact * i # fact eqn.. the get 5! = 5 × 4 × 3 × 2 × 1 = 120
    i += 1
print("Factorial =", fact)

# or===============================
num = int(input("Enter a number: "))
fact = 1
while num > 0 :
    fact *= num # fact eqn.. the get 5! = 5 × 4 × 3 × 2 × 1 = 120
    num -= 1
print("Factorial =", fact)