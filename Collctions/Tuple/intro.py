# Tuple================================================================
#------------------------------------------------------------
# it is defined as () , tuple()
# it is heterogeneous
# order of elements are preserved
# duplicate elements allowed'
# index postion are there
# it is itreable
# we cant modify the tuple have only 2 methods as index and count only nothing more

name ="1234567"
# int (name) # 1234567
# list(name) # ["1","2",.................."7"]
# list(range(1,10))

print(tuple(name))  # 0/p: ('1', '2', '3', '4', '5', '6', '7')

# or-----------------------------------------------------------------------
elements = (1,2,True,1,"Hello",7.5,2)
print(elements.count(1)) # 0/p:3 becuse true is 1 in machine code so it will consider that.
# return total number of occurances of a specific element
print(elements.index(2)) # here for 2 it is o/p: as 1 because 2 index have true and as as 1

num = (1,2,3,4,5)
nums = list(num)
nums.append(6)
print(tuple(nums))