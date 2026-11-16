# wap to check a number is prime or not.
 # need to  ask 5 inputs from the user
def prime(n1):
    for i in range(2,n1):
        if n1 % i == 0:
            print(f"{n1} is not prime")
            break
    else:
           print(f"{n1} is prime")
for i in range(5): # 0 1 2 3 4 here 5 times 5 i/p s are taken and checkj the prime or not
    num = int(input("enter the number: "))
    prime(num)
# Remember these three points:
# - A prime number has exactly two factors: 1 and itself.
# - return stops the function immediately.
# - range(5) asks for five inputs, and prime(num) checks each input separately.
# num and n1 one are diff names nio prblm it will then only work properly.,


# chrchking 1 case:
def prime(n1):
    for i in range(2,n1):
        if n1 % i == 0:
            print(f"{n1} is not prime")
            break
    else:
           print(f"{n1} is prime")
for i in range(5): # 0 1 2 3 4 here 5 times 5 i/p s are taken and checkj the prime or not
    num = int(input("enter the  number: "))
    while(num <= 1):
        num = int(input("enter the correct number: "))
    prime(num)