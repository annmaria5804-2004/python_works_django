# leap year================28/9/26=========
# 2000, 2008
#entury yr , non century    
#for centry yrs(2000)>>>divisible by 400
#  for non cetry yrs(2004..)>> divisible by 4 but not 100  
#⭐ Super easy rule Just memorize:
#Normally → divisible by 4 = leap year.
#But if it ends in 00 → it must be divisible by 400.
#Remember only this:
#A year is a leap year if:
#1. It is divisible by 400 → Leap year
#OR
#2. It is divisible by 4 AND NOT divisible by 100 → Leap year
# ===============================================

year = int(input("enter the yr: "))
if year % 400 == 0 or (year % 4 ==0 and year % 100 !=0):
    print(f"he {year} is leap yr")
else:
      print(f"he {year} is not a leap yr")
    

