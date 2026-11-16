"""
For loop 1/10/2026/thursday--------------------
quantity based

print()
input()
len() # return the length
type() # return the datatypes of the vaerable given

"""
name ="hello"
print(type(name)) # return the datatypes of the vaerable given
# o/p:  <class 'str'>
"""
range(start, stop,step) # this is iterabke function
range() used to generate the sequence of numbers or step
1,2,3,4,5,6   3,6,9,12,15  
10,20,30,40,50 range(start = 10,stop = 50, stop=10)
 
here we need to say the range fuction all details like start stop amd step
range(1,10,1)  here start 1 will be there 10 will be excluded
so if needed 10 add +1 or like 11 in stop area so it will be included
"""
range(1,10,1)
# if we not gave step then automatically generate as 1
# if not gave start the default as 0 
# eg: range(1,10) default 1 as step
# eg: range(10) default 1 as step and default start 0
#so o/p : 0,1,.....,8,9 
name ="helloworld"
range(len(name))# range(10) 0,1,........,9
print(range(1,10)) # range(1, 10)

"""
to print range we useb iteration method

"""

# wap to print numbers from 1 to 10
# in is a membership operator
 # 1 to 10
for i in range(1,11,1): # or range(1,11) deafault dtep as 1
    print(i)

# 6 to 0
for i in range(6,-1,-1): # range(6,-1) means to get 0 we need to add -1 then  dtep as -1 to go backward
    print(i)