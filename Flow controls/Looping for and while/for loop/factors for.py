#wap the factors of the number given
# 8: 1,2,4,8
# 6: 1,2,3,6
n = int(input("num: "))
# total = 0 for sum
for i in range(1,n+1): # 1 intial no and then n as our giving numver so to move further we bneed to do n+1  to get that n also
    #range(1,n+1) or range(1,n)
    if n % i ==0:
      print(i)
     # total +=i for sum
# print(total) # for sum