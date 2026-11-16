"""
An automorphic number is a integer whose square ends in the exact same digits as the number itself.
for ex: 5 >> 5^2 = 25  which ends in 5
        76 >> 76^2 = 5776 which ends in 76
        25 >> 25^2 = 625 which ends in 25
        
"""
num = 250
length = len(str(num)) # 3 string "250" then its length as 3
square = num ** 2 # 62500 #length = 3  means 10³ = 1000
if square % 10 ** length == num:
    print(" it is automorphic")
else:
    print("not ")
    
"""
length = 3
10³ = 1000
62500 % 1000 = 500

>>>62500 ÷ 1000
  1000 × 62 = 62000
  62500 - 62000 = 500
so 500 == 250 not
"""