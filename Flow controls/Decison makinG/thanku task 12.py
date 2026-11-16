"""
ask the user to enter 1,2,or 3 .if they enter a 1,display the message thanku, if they enter a2 display well donen, if they enter a3, display correct, if they enter anything display erroe message

 """
 
num = int(input("Enter 1, 2, or 3: "))

if num == 1:
    print("Thank you")
elif num == 2:
    print("Well done")
elif num == 3:
    print("Correct")
else:
    print("Error: Please enter only 1, 2, or 3")