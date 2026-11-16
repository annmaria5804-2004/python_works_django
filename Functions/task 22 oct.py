# 1. Number Transformation
# Replace even digits with 0 and odd digits with 1
def transform_number(n):
    result = 0
    place = 1
    while n > 0:
        digit = n % 10

        if digit % 2 == 0:
            digit = 0
        else:
            digit = 1
        result = digit * place + result
        place = place * 10
        n = n // 10
    return result
print(transform_number(583246))
print(transform_number(12345))

# 2. Digit Frequency Analyzer
# Count how many times a digit appears in a number
def digit_frequency(n, d):
    count = 0
    while n > 0:
        digit = n % 10
        if digit == d:
            count = count + 1
        n = n // 10
    return count
print(digit_frequency(1223122, 2))
print(digit_frequency(55525, 5))

# 3. Unique Digit Counter
# Count the number of distinct digits
def unique_digit_count(n):
    count = 0
    for digit in range(10):
        temp = n
        while temp > 0:
            if temp % 10 == digit:
                count = count + 1
                break
            temp = temp // 10
    return count
print(unique_digit_count(12234521))
print(unique_digit_count(7777))

# 4. Number Reordering
# Arrange digits in ascending order
def reorder_number(n):
    result = 0
    place = 1
    for digit in range(10):
        temp = n
        while temp > 0:
            if temp % 10 == digit:
                result = result + digit * place
                place = place * 10
            temp = temp // 10
    return result
print(reorder_number(583214))
print(reorder_number(42132))

# 5. Electricity Bill Calculator
# First 100 units: Rs. 2 per unit
# Next 100 units: Rs. 3 per unit
# Above 200 units: Rs. 5 per unit
def electricity_bill(units):
    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = 100 * 2 + (units - 100) * 3
    else:
        bill = 100 * 2 + 100 * 3 + (units - 200) * 5
    return bill
print(electricity_bill(80))
print(electricity_bill(250))

# 6. Password Strength Checker
# Weak: fewer than 8 characters
# Medium: 8 or more characters but missing uppercase or digit
# Strong: 8 or more characters with uppercase and digit
def check_password(password):
    if len(password) < 8:
        return "Weak"
    has_upper = False
    has_digit = False
    for ch in password:
        if ch >= 'A' and ch <= 'Z':
            has_upper = True
        if ch >= '0' and ch <= '9':
            has_digit = True
    if has_upper and has_digit:
        return "Strong"
    else:
        return "Medium"
print(check_password("hello12"))
print(check_password("Hello123"))

# 7. Palindrome Number Checker
# Check whether a number reads the same forward and backward
def is_palindrome(n):
    original = n
    reverse = 0
    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10
    if original == reverse:
        return True
    else:
        return False
print(is_palindrome(12321))
print(is_palindrome(12345))

# 8. Armstrong Number Range
# Check whether a number is an Armstrong number
# Display all Armstrong numbers from 1 to the given limit
def is_armstrong(n):
    original = n
    temp = n
    digits = 0
    total = 0
    while temp > 0:
        digits = digits + 1
        temp = temp // 10
    temp = n
    while temp > 0:
        digit = temp % 10
        power = 1
        for i in range(digits):
            power = power * digit
        total = total + power
        temp = temp // 10
    return total == original

def display_armstrong(limit):
    for n in range(1, limit + 1):
        if is_armstrong(n):
            print(n, end=" ")
    print()
print(is_armstrong(153))
print(is_armstrong(123))
display_armstrong(500)
display_armstrong(1000)

# 9. Shopping Discount Calculator
# Below Rs. 1000: no discount
# Rs. 1000 to Rs. 4999: 5% discount
# Rs. 5000 and above: 10% discount
def shopping_discount(amount):
    if amount < 1000:
        discount = 0
    elif amount < 5000:
        discount = amount * 0.05
    else:
        discount = amount * 0.10
    return amount - discount
print(shopping_discount(800))
print(shopping_discount(6000))

# 10. Time Converter
# Convert seconds into hours, minutes and remaining seconds
def convert_time(seconds):
    hours = seconds // 3600
    seconds = seconds % 3600
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    return hours, minutes, remaining_seconds
print(convert_time(3725))
print(convert_time(5000))