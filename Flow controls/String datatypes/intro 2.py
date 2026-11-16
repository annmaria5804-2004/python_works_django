# 9/10/2026================================================
# string
# =================================
#      012345 # correct left to right
#    -6-5-4-3-2-1 # reverse right to left
name ="python"
# slicing
print(name[3]) # h
print(name[1:5:1]) # 1-4 ytho -> 1 range  means contiunes other  - name[start : stop : step]
print(name[0:5:2]) # pto -> taking char from 0,2,4  and 5 is not taken only upto 4 moreover the range is 2 and so 1 after the next char is taken
print(name[2:]) # thon -> slice the char from 2 to the last element  so simply gave : and not gave anything
print(name[-1] )# n -> here -1 onwards the char is taken
print(name[:4]) # pyth -> slice the char from 0 to 3 and 4 is not taken
print(name[::-1]) # nohtyp ->  used to reverse the string entriely >>


# Methods of the string datatypes:
#========================================================
 # stringvariable.method()
str()
int()
name ="hello" # name =str()
num = 10 # num = int()

number = 10 # interger so > number. gave its defined list of datatypes
name = "heLLoworld" # string so > name. gave its list of defined datatypes

print(name.upper()) # this defined function returns the string in upper case
print(name.lower()) # this defined function returns the string in lower case
print(name.capitalize()) # this defined function returns the strings 1st letter into upper case and all others as same
print(name.count("l")) # this defined function returns the a particular char count in string here l comes 3 times so it will be returned
# or 
print(name.count("llo")) # this defined function returns the a particular char count in string here llo comes 1 times so it will be returned
# or
print(name.count("lLo")) # this defined function returns the a particular char count in string here lLo not comes so false and gave 0 .
print(name.swapcase()) # change all the lower into uppercase and viceversa
print(name.index("l")) # here index value is 8 for smalle letter l if it was capital L then it is 2 because 1st L is at 2nd 
print(name.index("o")) # 4th postion 1st 0

name ="python is a language"

print(name.title()) # Python Is A Language tthis is the o/p make this as title form .
print(name.isupper()) # true when all char in name are upper here so it is false
print(name.islower()) # true when all char in name are lower here so it is all lower so true

name ="12344"
print(name.isdigit()) # returns True if the char in the string is a digit
name = "ann"
print(name.isalpha()) # returns true if all char are alphabets

name = "a123"
print(name.isalnum()) # returns true if it contain atleast one alphabet

