# Write a Python program to create a simple ATM system.
#The user starts with an initial balance of ₹10,000.
#Display the following menu:
#===== ATM MENU =====
#1. Check Balance
#2. Deposit
##4. Exit
##Use if-elif-else to perform the following operations:
#Check Balance
##Deposit
#Ask the user to enter the deposit amount.
##Add the amount to the balance.
#Display the updated balance.
#Withdraw
#Ask the user to enter the withdrawal amount.
#Check whether the withdrawal amount is less than or equal to the available balance.
#If sufficient balance is available, deduct the amount and display the remaining balance.
#Otherwise, display "Insufficient Balance".
#Exit
#Display "Thank you for using the ATM".
#If the user enters any other choice:
#Display "Invalid Choice".


bal = 10000

print(f"============ATM MENU==========")
print(f"1.check balance \n2.deposit \n3.withdraw \n4.exit")
choice = input("user choice: ")
if choice == "1":
    print(f"hi,ur available balance is{bal}")
elif choice == "2":
    deposit_amount = int(input("enter the deposit amount:"))
    bal = bal + deposit_amount
    print(f"hii,your updated balace is {bal}")
elif choice == "3":
    withdraw =  int(input("enter the withdraw amount:"))
    if withdraw <= bal:
        bal = bal - withdraw
        print(f"thankyou and your balance is {bal}")
    else:
        print("sorry insufficent balance")
elif choice == "4":
    print("thank you visit again....")
else:
    print("invalid choice")

