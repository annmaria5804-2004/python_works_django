# Ask how many slices of pizza the user started with and ask how many slices they have eaten. Work out how many slices they have left and display the answer in a userfriendly format.

total_slices = int(input("How many slices of pizza did you start with? "))
eaten_slices = int(input("How many slices have you eaten? "))

slices_left = total_slices - eaten_slices

print("You have", slices_left, "slices of pizza left.")