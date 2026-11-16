# wap to get the no.s divisible  by 3 and 5 from 1 to 70

print([i for i in range(1, 71) if i % 3 == 0 and i % 5 == 0])

# or=========================================================
# WAP to get the numbers divisible by 3 and 5 from 1 to 70
num= []
for i in range(1, 71):
    if i % 3 == 0 and i % 5 == 0:
        num.append(i)
print(num)