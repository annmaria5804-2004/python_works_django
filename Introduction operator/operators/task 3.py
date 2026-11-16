#  Ask for the total price of the bill, then ask how many diners there are. Divide the total bill by the number of diners and show how much each 
# person must pay

tbill = float(input("total price of the bill:"))
dinners = int(input("how many dinners:"))
div = tbill / dinners
print("each person bill:",div)
#or
print(f"each person bill {tbill / dinners}")
