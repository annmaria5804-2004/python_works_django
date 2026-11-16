# ceeate a class atm
# method1 = details(blance = 1000, name)
#  method2 = deposit()
# method3 = withdrawal()
# method4 = check balance

class Atm:

    # Method 1: Details
    def details(self, balance, name): # Stores account holder name and initial balance
        self.balance = balance
        self.name = name
        print(f"Hi {self.name}, welcome to my bank!")

    # Method 2: Deposit
    def deposit(self): # Adds money to the account
        amount = int(input("Enter deposit amount: ")) # or avoid this and and add on last obj calling area
        self.balance += amount
        print("Amount deposited successfully")

    # Method 3: Withdrawal
    def withdrawal(self): # Removes money from the account
        amount = int(input("Enter withdrawal amount: ")) # or avoid this and and add on last obj calling area

        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully")
        else:
            print("Insufficient balance")

    # Method 4: Check balance
    def check_balance(self): # 	Displays the current balance
        print("Your current balance is:", self.balance)


# Creating an object
obj1 = Atm()

# Calling methods
obj1.details(1000, "Ann")
obj1.deposit()
obj1.withdrawal()
obj1.check_balance()

"""
self. balance and self.name for calling the method variabales or  methods in anaother method in a class.
balance is a local parameter received by the method.
self.balance stores the balance as an instance attribute.
Other methods can access and modify self.balance.

Important: Understand the difference
Variable	            Meaning

balance         	Parameter/local variable
self.balance	    Instance variable
name	            Parameter
self.name	        Instance variable
obj1	            Object


"""