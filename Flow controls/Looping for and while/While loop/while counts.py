# wap to get count of last digit  in a no.

num = int(input("enter the no.: "))
count = 0
while(num > 0):# last condtion false ayye 0 etti ettumbo loop out akan.
    num % 10 # this is not  need to give if not give also ans will get correctly
    count += 1
    num //= 10
print(f"thr count is{count}")