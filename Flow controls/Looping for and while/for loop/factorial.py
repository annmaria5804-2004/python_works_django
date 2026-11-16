#wap to get the factorial of no.s from 3 to 5
# 1,2,3,4,5   # 1,2 # 1,2,3

for i in range(3,6): # i = 3,i = 4,i = 5
    #3!,4!,5!
    fact = 1
    for j in range(1,i+1): #(1,4) 1,2,3 Start from 1 and go up to i.
        fact *= j
    print(f"the factorial of {i} is {fact}")

"""
fact = 1
fact = 1 × 1 = 1
fact = 1 × 2 = 2
fact = 2 × 3 = 6
= 3! = 6

eg: Then i = 4
The outer loop moves to:
i = 4
Again:
fact = 1
The inner loop gives:
1, 2, 3, 4
Calculation:
1 × 1 = 1
1 × 2 = 2
2 × 3 = 6
6 × 4 = 24
Therefore:
4! = 24

Outer loop (i) = numbers 3, 4, 5
Inner loop (j) = numbers to multiply
fact = stores the multiplication result
"""
