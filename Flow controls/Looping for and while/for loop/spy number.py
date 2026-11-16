#check a number is spy or not
# spy number:
# the sum of digits of number equal to the product of digits in a number


#What is a Spy Number?
#A number is a Spy Number if:
#Sum of its digits = Product of its digits
# 123>>> sum>> 1+2+3>>6
# 123>>> product>> 1*2*3>>6
# 123 is a spy number


number = 1124
sum = 0
product = 1

for i in str(number):

    # i = int(i)

    sum += int(i)
    product *= int(i)

if sum == product:
    print("Spy number")
else:
    print("Not a spy number")
    
    
# while loop+++++++++++++++++++++++++===============
number = 1124
sum = 0
product = 1

while number > 0:

    num = number % 10 # This gets the last digit.

    sum += num
    product *= num

    number = number // 10 # removes the last digit.

if sum == product:
    print("Spy number")
else:
    print("Not a spy number")