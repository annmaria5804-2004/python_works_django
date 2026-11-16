# enter the no and check both divisible by 3 and 5 and else if it eithe divi 3 or 5 and else it is not bt both 3 and 5

num = int(input("number :"))
if num % 3 == 0 and num % 5 ==0:
   print("both divi by 3 and 5")
elif num % 3 == 0 or num % 5 ==0:
    print("either  divi by 3 or 5")
else:
    print("not div by both 3 and 5")