# 7th october 2026================
# wap to get numbers from 10 to 200 prime number

for num in range(10, 201):       # 10 to 200

    for i in range(2, num):      # check factors

        if num % i == 0:
            print(f"the {num} is not prime")
            break                # not prime
          
    else:                        # no break = prime
        print(f"the {num} is prime")
        

#================================================
# check the prime numbers from  1 to n

# check the prime numbers from 100 to 10

# get the  first 10 prime numbers from 1 to n

# get the prime factors of the number enter by user
#====================================================
# wap to find prime numbers from 1 to n
n = int(input("Enter the number: "))

if n == 1:
    print("Please enter a number above 1")

else:
    for num in range(2, n + 1):

        for i in range(2, num):

            if num % i == 0:
                break

        else:
            print(f"the {num} is a prime")

# check the prime numbers from 100 to 10

for num in range(100, 9, -1):

    for i in range(2, num):

        if num % i == 0:
            break

    else:
        print(num)

# get the first 10 prime numbers from 1 to n

n = int(input("Enter the number: "))

count = 0

for num in range(2, n + 1):

    for i in range(2, num):

        if num % i == 0:
            break

    else:
        print(num)
        count += 1

        if count == 10:
            break
# get the prime factors of the number entered by user

n = int(input("Enter the number: "))
if n == 1:
    print(f"please enter a num above 1")
    
for i in range(2, n + 1):

    while n % i == 0:

        print(i,"is a prime factor")

        n = n // i