"""
amstrong no that equals the sum of its own digits, 
where each digits is raised to the power of the total
number of digits 
3-digits eg: 153 >> 1^3 +5^3 + 3^3 = 1 + 125 + 127 = 153
4-digits eg: 1532 >> 1^4 +5^4 + 3^4 + 2^4 = ....

"""

num = int(input("Enter a number: "))
original = num # Because later we are going to change num using num = num // 10 Eventually num becomes 0.So we keep the original 153 safely in another variable.
count = len(str(num)) # very imp eqn len(number like 257 anything ) returns its lengthb as 3 or 4 or 2 here 3 if 32456 means 5 as lenth n 
sum = 0
while num > 0:
    digit = num % 10 # 153 % 10 = 3 to get last digit
    sum = sum + digit ** count # sum = 0 digit = 3 count = 3
    num = num // 10 # 153 // 10 = 15   so num = 15  We removed the last digit 3
    
if sum == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
    
    
    
    
"""
1. Get the number
num = int(input("Enter a number: "))

Suppose you enter:

153

Then:

num = 153

input() gives a string, so int() converts it to an integer.

2. Save the original number
original = num

So:

original = 153
num      = 153

Why do we need original?

Because later we are going to change num using:

num = num // 10

Eventually num becomes 0.

So we keep the original 153 safely in another variable.

3. Count the number of digits
count = len(str(num))

This looks complicated, but break it into 2 steps.

str(num)
str(153)

becomes:

"153"

It's now a string.

len()
len("153")

gives:

3

Therefore:

count = 3

So count tells us how many digits the number has.

For example:

len(str(153))     # 3
len(str(1532))    # 4
len(str(25))      # 2
len(str(12345))   # 5

This is important because Armstrong numbers use the number of digits as the power.

4. Start the sum at 0
sum = 0

We need a variable to store the total.

Initially:

sum = 0

Then we'll keep adding:

1³
5³
3³
Now the important part: while loop
while num > 0:

This means:

Keep repeating as long as num is greater than 0.

Initially:

num = 153

So the loop starts.

First iteration
Get the last digit
digit = num % 10

% means remainder.

153 % 10 = 3

So:

digit = 3

The % 10 trick is used to get the last digit.

Examples:

153 % 10 = 3
5722 % 10 = 2
45 % 10 = 5
9 % 10 = 9
Add the digit raised to the power
sum = sum + digit ** count

We have:

sum = 0
digit = 3
count = 3

Therefore:

sum = 0 + 3³
sum = 0 + 27

So:

sum = 27
Remove the last digit
num = num // 10

// means integer/floor division.

153 // 10 = 15

So now:

num = 15

We removed the last digit 3.

Second iteration

Now:

num = 15
Get last digit
digit = num % 10
15 % 10 = 5

So:

digit = 5
Add its cube
sum = sum + digit ** count
sum = 27 + 5³
sum = 27 + 125
sum = 152
Remove last digit
num = num // 10
15 // 10 = 1

Now:

num = 1
Third iteration

Now:

num = 1
Get last digit
digit = num % 10
1 % 10 = 1

So:

digit = 1
Add its cube
sum = sum + digit ** count
sum = 152 + 1³
sum = 153
Remove last digit
num = num // 10
1 // 10 = 0

Now:

num = 0
Loop stops

The condition was:

while num > 0:

But now:

num = 0

So:

0 > 0

is False.

The loop ends.

Finally, compare
if sum == original:

We have:

sum      = 153
original = 153

Therefore:

153 == 153

is True.

So:

print("Armstrong number")

Output:

Armstrong number
The whole process visually

For 153:

Step	num	digit = num % 10	digit ** count	sum	num // 10
Start	153			0	
1	153	3	3³ = 27	27	15
2	15	5	5³ = 125	152	1
3	1	1	1³ = 1	153	0

Then:

sum = 153
original = 153

153 == 153

✅ Armstrong number

Remember these 4 important tricks

These are the most important parts of this program:

1. Count digits
count = len(str(num))

Example:

153 → 3 digits
1532 → 4 digits
2. Get last digit
digit = num % 10

Example:

153 % 10 → 3
15 % 10 → 5
1 % 10 → 1
3. Remove last digit
num = num // 10

Example:

153 // 10 → 15
15 // 10 → 1
1 // 10 → 0
4. Raise digit to number of digits
digit ** count

For 153:

3 ** 3
5 ** 3
1 ** 3

So the basic logic is:

Take last digit → raise it to digit count → add to sum → remove last digit → repeat.

"""