# # reading (r) the file sample filehandilng.py
# ===========================================================\

# Reading (r) a file
file1 = open("sample filehandilng.py", "r")

result = file1.read()

print(result)
file1.close()

# ===========================================================\

# # Reading (r) a file file name  reading file.py
# file1 = open("d:/python_works_django/Fliehandling/reading file.py", "r")

# result = file1.read()

# print(result)
# file1.close()

# next===============================================================================
while True:
    filename = input("enter the filenmae: ") # sample filehandilng.py
    try:
        file1 = open(filename,"r")
        result = file1.read()
        print(result)
        break
    except FileNotFoundError:
        print(" there is no such file") # wrong name then this
print("thanku") # last with o/p this too

# path ========================================
#  to get [ath of a file in folder go to file name area the right clickj and copy the path anfd take
#  in that we have \ but to get we need to change all to / or add in 1st area \\ then will be oke
# D:\python_works_django\Collctions\collections all .py : this is orginal we add \\ in 1st or change all / to this
# to select the \ fastly select one \ then ctrl+D then change it to / and lastly esc click

file1 = open("D:/python_works_django/Collctions/collections all .py", "r")

result = file1.read()

print(result)
file1.close()

# ======================================================================
file1 = open("writing sample", "r")
 # file read(10)   read char 
result = file1.readline() # help to read line of details seperstely in a file
 # file readline()
print(result)

#==============================================================================================
file1 = open("sample filehandilng.py", "r")

result = file1.read(10)

print(result)
file1.close() # can use if needed not imp

#  return each line as a elemnts in a list
with open("sample filehandilng.py","r") as file:
    print(file.read())
