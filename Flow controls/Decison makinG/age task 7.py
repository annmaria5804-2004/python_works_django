# 24/09/2026-----------------------thursday
# Ask the user’s age. If they are 18 or over, display the message “You can vote”, if tey ae aged 17, display themessage “You can learn to drive”, if they are 16, display the message “You can buy a lottery ticket”, if they are under 16, display the message “You can go Trickor-Treating”.

age = int(input("Enter your age: "))
if age >= 18:
    print(" you are eligible to vote")
elif age == 17:
    print("eligible for driving")
elif age == 16:
    print("you can but lottery ticket")
else:
    print("you can go trick-or-treating")
