# wap to get the sum o digits in a number

num = int(input("enter the no.: "))
total = 0
while(num > 0):# this is not  need to give if not give also ans will get correctly
    last_digit = num % 10   # get last digit
    total += last_digit
    num //= 10   # remove last digit
print(f"the total sum is{total}")

# 1st 1234 take 4 by num% 10 and remove by num // 10 
# then 123 then take 3 then 12 take 2 lastly 1 and end.