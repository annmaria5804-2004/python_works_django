# wap to get avg of 3 no.s using function

def avg_num():
    n1 = int(input("enter the n1: "))
    
    n2 = int(input("enter the n2: "))

    n3 = int(input("enter the n3: "))
    total = n1+ n2+ n3
    avg = total/3
    print(avg)
avg_num()
# this can be used in any where means  if i call this function anywhere then i can use this without wroting thec ent0ire code.

# or set variable not like this means n1 n2 n3 other way


def avg_num(n1,n2,n3): # parameters

    total = n1+ n2+ n3
    avg = total/3
    print(avg)
avg_num(10,20,30) # define the values here for n1 n2 n3 then easyily will occur. this values will be passed to the that values.