""" 24/10/2026===========================================================================================
Collections:
----------------------------------------------------------------------------------
Assigning more than one values to a single variable.

# Types: list, tuples, set, dictionary

1. List name = [] or list()
---------------------------------------------------
>list  can be defined a variable by either [] or list()
>duplicate elements are there for each elements
>index postions are there for each elements
>zero based indexing
>slicing are allowed
>list is heterogenous
>list is mutable means we can modify the exsting list(append(), insert(), pop())
(felexible and good type in collection than other types)
"""
# LIST============================================
name = 10 # int
name = "hello" # str
name = [] # list
         # 0 1   2     3    4     5      6 
elements =[1,2,"hello",True,4.5,"python",2] 
for i in range(5):
    print(elements)
#            0 1   2      3    4     5      6 7> here white space take as one index if space plus any data come in one are the same index if white space alone the it is added as a index.
# elements =[1,2,"hello", True,4.5,"python", ,2]
 
elements =[1,2,"hello",True,4.5,"python",2] 

elements.append("kochi") # add a new objects to the end of the list (only on last)
print(elements) #  elements =[1,2,"hello",True,4.5,"python",2,"kochi"]

elements.insert(2,False) # here in 2nd index false will be inserted and all other process goes to nextpostion and moves to next and last 7 index become 8 (nothing get deleted only insertion)
# elements =[1,2,False,"hello",True,4.5,"python",2,"kochi"] 
print(elements) 

elements.insert(-1,"django") # not possible to do this list have no such option so it uses append to make anything on last (this is  not a working code) 

elements =[1,2,"hello",True,4.5,"python",2] 
print(elements.count(2)) # return the total no. of occurances of a value given
print(len(elements)) # 7 >> return total no. of values in a list

print(elements.pop()) # 2 >> remove the last element from the list and return the reomved element
print(elements.pop(2)) # hello >> remove the 2nd element from the list and return the reomved element

print(elements.index("python")) # find 1st occurance of the given strings index postion

elements.remove("python") # remove the elemts from the list where it is 1st occured 
print(elements) 