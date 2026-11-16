#Wap to reverse a no by user
# eg 5720 to 0275
num = int(input("Enter a number: "))
rev = 0
while num > 0:
    digit = num % 10# to get last digit
    rev = rev * 10 + digit
    num = num // 10 
print("Reverse =", rev)   # remove last digit

"""
remove last digit by num % 10  and then add to rev by eqn rev *10 + digit
then go to next last digit  repeat the same process.
% 10  → GET the last digit
// 10 → REMOVE the last digit
* 10  → MAKE space for the new digit
"""