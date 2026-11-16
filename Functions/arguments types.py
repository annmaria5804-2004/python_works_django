# Arguments types == 22/10/26=============
#==============================================================

def greet(name,age,place="kasaragod"):
    print(f"her name is {name} and age is {age} moreover she is from {place}")
greet(place="kasaragod",age=22,name="Ann") # her name is Ann and age is 22 moreover she is from kasaragod
# this is called key word argument because here we gave the exact  key word to correctly detemine the valuses. corret ans and most better way
greet("kasaragod",22,"Ann")  # her name is kasaragod and age is 22 moreover she is from Ann 
# this is postional argument and this is a isssue here the nmes are disloacated and goes ireular way .otherwise need to gave in same order then only correctly come .
greet(name="ann", age=22)# her name is ann and age is 22 moreover she is from kasaragod
# Default argument in Python means giving a parameter a value in advance. If the user does not pass a value for that parameter during funtion call, Python uses the default value.

# eg:

def add(a, b=10):
    print(a + b)

add(5) # here default value takes a as 5 and b as 10 from above and gave 15
add(5, 20) # her 20 as b value

# or'''''

def greet(name="Ann"):
    print("Hello", name)

greet() # here default take periouvus defined ann as name.
greet("Maria") # here takes the defined correct name as maria.



