# given a interger , perform the following conditional actions:
# if n is odd , print weired 
# if n is even and in the inclusive range 2 to 5 print not weried
# if n is even and in inclusive range 6 to 20 print wewroed
# if n is even and greazter than  20 , print weried

n = int(input("Enter a number: "))

if n % 2 != 0:
    print("Weird")

elif n >= 2 and n <= 5:
    print("Not Weird")

elif n >= 6 and n <= 20:
    print("Weird")

else:
    print(" Weird")
    
