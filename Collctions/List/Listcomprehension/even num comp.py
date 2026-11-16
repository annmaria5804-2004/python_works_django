# WAP to print the even numbers from 1 to 20
num = []
for i in range(1, 21):
    if i % 2 == 0:
       num.append(i)
       print(num)  
        
# Explanation:
# - range(1, 21) generates numbers from 1 to 20.
# - i % 2 == 0 checks whether a number is even.
# - print(i) prints each even number.

# or===========================================================

print([i for i in range(1, 21) if i % 2 == 0])