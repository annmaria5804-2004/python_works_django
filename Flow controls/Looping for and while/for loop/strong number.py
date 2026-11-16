""" 5th october 2026
A strong number  is a positive number where  the sum of the factorial of its individual digits eqauls the number itself.
for eaxmple, 145 is a strong number because:
eg: 1! + 4! + 5! = 1 + 24 + 120 = 145
int data type is not iterable in python
range() is iterable
string is iterable
"""

number = 645
total = 0
for num in str(number): # for i in 645
    # num = 6 # "6"
    fact = 1
    for j in range(1,int(num) +1): # for j in range(1,2,3,4,5,6)
        fact *= j
    total += fact
    
if total == number:
    print("strong num")
else:
    print("not a strong number")
    
    
#===============while=================
number = 645

total = 0
num = number

while num > 0:

    digit = num % 10

    fact = 1
    j = 1

    while j <= digit:
        fact *= j
        j += 1

    total += fact

    num = num // 10

if total == number:
    print("strong num")
else:
    print("not a strong number")