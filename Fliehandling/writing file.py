file2 = open("sample filehandilng.py", "w")

result = file2.write(" an ann and a good girl")

print(result)

# here the exsiting data in file is deleted and write this to the file
 #0/p:  an ann and a good girl >> runing of sample filehamdilin.[py file]
 
#========================================================================================
num = [1,2,3,4,5,6,7]
file2.write(str(num))
print(result)
# o/p:  an ann and a good girl[1, 2, 3, 4, 5, 6, 7]
# here the exsiting data in file is deleted and write this to the file

# if there is no file when i am giving nbame the create its own file and write it to that\
file2 = open("writing sample.py", "w")

result = file2.write("# name = an ann and a good girl")

print(result)

# here the exsiting data in file is deleted and write this to the file

