# Ask the user if it is raining. If they answer “yes”, 
#ask if it is windy. If they answer “yes” to this second question, 
#display the answer “It is too windy for an umbrella”, otherwise 
#display the message “Take an umbrella”. If they did not answer yes 
#to the first question, display the answer “Enjoy your day”.

rainy = input("is it raining: ")
if rainy == "yes":
    windy = input("is it windy: ")
    if windy == "yes":
        print("it is too windy foar an umberlla")
    else:
        print("take an umberlla")
else:
    print("enjoy your.......")
    
    



