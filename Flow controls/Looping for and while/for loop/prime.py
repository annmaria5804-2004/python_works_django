# a prime number is a whole number greater than 1 whose only factors are 1 and itself.
# the 1st ten primes are 2,3,5,7,11,13,17,19,23,29
# 8 = 1,2,4,8
#2=1,2 and 3= 1,3 and 5=1,5 and 7 =1,7 
# this means a 1 and that number then prime other wise not prime.

num = int(input("enter the number: ")) # 7
for i in range(2,num): # i = 2,3,4,5,6
    if num % i == 0: # if 7 % 2 == 0 , 3,4,5,6
        print(f"the {num} is not a prime")
        break
else:
    print(f"the {num} is a prime")
    
# if the condition comes 1 mrsns number a s 1 then
num = int(input("enter the number: ")) # 7
if num == 1:
    print(f"please enter a num above 1")
    
for i in range(2,num): # i = 2,3,4,5,6
    if num % i == 0: # if 7 % 2 == 0 , 3,4,5,6
        print(f"the {num} is not a prime")
        break
else:  # here else for the for loop not put under the while this is a special case for prime number problem
    print(f"the {num} is a prime")
    
# using while=====
num = int(input("enter the number: ")) # 7
while(num <= 1):
    print(f"please enter a num above 1")
    num = int(input("enter the number: "))
    
for i in range(2,num): # i = 2,3,4,5,6
    if num % i == 0: # if 7 % 2 == 0 , 3,4,5,6
        print(f"the {num} is not a prime")
        break
else:
    print(f"the {num} is a prime")
    
    
# other method=========================
n = int(input("Enter the number :"))

count = 0

for i in range(1,n) :


    if n % i == 0 :

        count = count + 1

if count == 1 :

    print("Prime")

else :

    print("Not prime")