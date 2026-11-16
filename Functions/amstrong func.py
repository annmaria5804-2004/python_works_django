# wap to check the given number is amstrong or not using function.

def amstrong(n):
  temp = n# Because later we are going to change num using num = num // 10 Eventually num becomes 0.So we keep the original 153 safely in another variable.
  count = len(str(num)) # very imp eqn len(number like 257 anything ) returns its lengthb as 3 or 4 or 2 here 3 if 32456 means 5 as lenth n 
  sum = 0
  while n > 0:
     digit = n % 10 # 153 % 10 = 3 to get last digit
     sum = sum + digit ** count # sum = 0 digit = 3 count = 3
     n = n // 10 # 153 // 10 = 15   so num = 15  We removed the last digit 3
    
  if sum == temp:
     print("Armstrong number")
  else:
     print("Not an Armstrong number")
num = int(input("enter the number: "))
amstrong(num)