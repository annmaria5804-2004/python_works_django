# wap to get the factiorial of the num given by user using a function

def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    print(fact)

factorial(7)

# Simple explanation
# 1. def factorial(num): defines a function that accepts a number.
# 2. fact = 1 initializes the factorial result to 1.
# 3. range(1, num + 1) generates numbers from 1 to 7 when num = 7.
# 4. fact *= i multiplies fact by each number in the loop. It is equivalent to fact = fact * i.
# 5. print(fact) displays the final result.
# 6. factorial(7) calls the function with the number 7.