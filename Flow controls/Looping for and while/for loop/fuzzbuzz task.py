# print the num from 1 to 50
# if any no. divi by 3 replace the num and print "fizz"
# if any no. divi by 5 replace the num and print "buzz"
# if any no. divi by both replace the num and print "fizzbuzz"


for i in range(1, 51):

    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")

    elif i % 3 == 0:
        print("fizz")

    elif i % 5 == 0:
        print("buzz")

    else:
        print(i)
        
#================while==================
i = 1

while i <= 50:

    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")

    elif i % 3 == 0:
        print("fizz")

    elif i % 5 == 0:
        print("buzz")

    else:
        print(i)

    i += 1