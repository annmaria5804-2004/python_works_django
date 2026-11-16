# wap to get the sum of numbers from 1 to n

n = int(input("num: "))
total = 0
for i in range(1,n+1): # 1 intial no and then n as our giving numver so to move further we bneed to do n+1  to get that n also
    #range(1,n+1) or range(1,n)
    total += i
    print(i)
print(total)