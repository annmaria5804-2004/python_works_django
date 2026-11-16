# Ask the user to enter their first name. If the length 
# of their first name is under five characters, ask 
# them to enter their surname and join them 
# together (without a space) and display the name 
# in upper case. If the length of the first name is five 
# or more characters, display their first name in 
# lower case.

fname = input("enter the fname: ")

if len(fname) < 5:
    sname = input("enter the sname: ")
    name = fname+sname
    print(name.upper()) # this defined function returns the string in upper case
else:
     print(fname.lower()) 
     

"""
Simple line-by-line explanation
1. fname = input("enter the fname: ") — Gets the user's first name.
2. if len(fname) < 5: — Checks whether the first name contains fewer than 5 characters.
3. sname = input("enter the sname: ") — If the first name has fewer than 5 characters, asks for the surname.
4. name = fname + sname — Joins the first name and surname without a space.
5. print(name.upper()) — Displays the joined name in uppercase.
6. else: — Runs when the first name has 5 or more characters.
7. print(fname.lower()) — Displays the first name in lowercase.
"""