""" 8th oct 2026---------------------------
string datatypes
=============================================================================================================================
>>>string means for python a collection of characters and sting si iterable.
>>> iteration >> iterating variable i strarts from position 0 and assign values from each postion during for loop


>>>exm: name ="hello.]&%12 " here this is collection of char 
>here h,e,l,l,o,.,],&,%,1,2,_(whitespace) all are char and togerther string beacuse comes inside double quotes("").
>therefore here lengthnof char or string is 12.

>>>so anything inside the "....." this is a string for python.
>># number, alphabets,dots,commas,whitespace,each pf thgem are consider to be character.


>>>>> INDEX POSITIONING means it is a postion values for rach character in aq string.

"""
#====================================================================================================================================
name = "hello"
for i in range(5):  # range(5) = repeat 5 times.
    print(name) # here printing hello 5 times
# Here, i is the loop variable. We are not using its value, but it still controls how many times the loop runs.

#======================================================================================================================================

# string postional values means index postioning and it is zero based index
#zero based index and order of char can be maintaned properly.
name = "hello" # 0 1 2 3 4 
# and duplicate cahrs are allowed in a string which means here hello have 2 ll and is duplocate or repetative that is allowded.
#         0123456789
for i in "helloworld": # here 0 is h so assign i as h then 1 assign as e and etc....
    print(i)
 
#===========================================================================================================================================================   
    
# postion finding : slicing::::
name ="python"
print("5th postion char sliced is ",name[2])# slice the char t as 5th postion char 
# [] is used to slice the char important dont chage this.
# ( ) used in functions.

#==============================================================================================================================

#print(num[2])
#     print(num[2])
# TypeError: 'int' object is not subscriptable
# thisd means integer dont have index postionaing so dont get the value only string have index postioning. 
# if neede number then gave then in "5227"
# then we will get the value correctly because it is a string

#=============================================================================================================================

name = "hello world"
print(name[5]) # here output is blank because 5 is white space and print as white space simply nothing just space

#=====================================================================================================================================

# to slice more than 1 char in single porgm
name = "hello world"
print(name[5])
print(name[2:7]) 
# llo_w slice the substring from postion 2 to 7
# here 2 as start and collen : to seoarate them and then end as 7 but 7th char not incuded only upto 6
#so we get charaters from 2 to 6 means 7 is not included
print(name[100]) # gaves o/p as out of index range means there is no such index in your name
#o/p as : here is no such index in your name | IndexError: string index out of range
