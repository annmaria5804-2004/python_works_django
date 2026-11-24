
# ==========================================
# CAMPUS LOST & FOUND TRACKER
# A simple terminal-based Python project
# ==========================================


# Create an empty list to store all items
items = []


# ------------------------------------------
# 1. FUNCTION TO ADD A LOST OR FOUND ITEM
# ------------------------------------------

# Create a function named add_item
# item type receives either "Lost" or "Found"
def add_item(item_type):

    # Get the item name from the user
    name = input("Enter item name: ")

    # Get the location where the item was lost or found
    location = input("Enter location: ")

    # Get the name of the person reporting the item
    person = input("Enter your name: ")

    # Get the contact information
    contact = input("Enter contact number: ")

    # Create a dictionary to store the item details
    item = {
        "id": len(items) + 1,       # Generate an item ID.+ 1 generates the next ID.len(items) counts the number of records in the list.
        "type": item_type,          # Store Lost or Found
        "name": name,               # Store item name
        "location": location,       # Store item location
        "person": person,           # Store reporter name
        "contact": contact,         # Store contact number
        "status": "Open"             # Initially item status is Open
    }

    # Add the dictionary new thing to the items named list
    items.append(item)

    # Display a success message
    print("\nItem added successfully!")

    # Display the generated item ID.item["id"] accesses the value associated with the "id" key in the dictionary.
    print("Your Item ID is:", item["id"])


# ------------------------------------------
# 2. FUNCTION TO VIEW ALL REPORTED ITEMS
# ------------------------------------------

# Create a function to display all reported items.
def view_items():

    # Check whether the list is empty
    if len(items) == 0:

        # Display message if no items are available
        print("\nNo items reported yet.")

    else:

        # Display the heading
        print("\n===== ALL REPORTED ITEMS =====")

        # Loop through each item in the list
        for item in items:

            # Display the item details
            print("\nItem ID:", item["id"])
            print("Type:", item["type"])
            print("Item Name:", item["name"])
            print("Location:", item["location"])
            print("Reported By:", item["person"])
            print("Contact:", item["contact"])
            print("Status:", item["status"])

            # Display a separator
            print("-----------------------------")


# ------------------------------------------
# 3. FUNCTION TO SEARCH FOR AN ITEM
# ------------------------------------------

# Create a function to search items
def search_item():

    # Ask the user for an item name
    search = input("\nEnter item name to search: ")

    # Initially assume that no item is found
    found = False

    # Check every item in the list
    for item in items:

        # Compare the search text with the item name
        # lower() makes the search case-insensitive
        if search.lower() in item["name"].lower():

            # Display the matching item details
            print("\nItem found!")
            print("Item ID:", item["id"])
            print("Type:", item["type"])
            print("Item Name:", item["name"])
            print("Location:", item["location"])
            print("Status:", item["status"])

            # Change found to True
            found = True

    # Check whether no matching item was found
    if found == False:

        # Display a message if there is no match
        print("No matching item found.")


# ------------------------------------------
# 4. FUNCTION TO MARK AN ITEM AS RETURNED
# ------------------------------------------

# Create a function to update item status
def mark_returned():

    # Ask the user to enter the item ID
    item_id = input("\nEnter item ID: ")

    # Initially assume that the item is not found
    found = False

    # Check every item in the list
    for item in items:

        # Compare the stored ID with the entered ID
        # str() converts the ID into a string
        if str(item["id"]) == item_id:

            # Check whether the item is already returned
            if item["status"] == "Returned":

                # Display a message
                print("This item is already returned.")

            else:

                # Update the item status
                item["status"] = "Returned"

                # Display success message
                print("Item marked as returned successfully!")

            # Mark the item as found
            found = True

            # Stop the loop
            break

    # Check whether the entered ID is invalid
    if found == False:

        # Display an error message
        print("Invalid item ID.")


# ------------------------------------------
# 5. MAIN PROGRAM
# ------------------------------------------

# while True runs the menu continuously
while True:

    # Display the application title
    print("\n===== CAMPUS LOST & FOUND TRACKER =====")

    # Display all menu options
    print("1. Report Lost Item")
    print("2. Report Found Item")
    print("3. View All Items")
    print("4. Search Item")
    print("5. Mark Item as Returned")
    print("6. Exit")

    # Get the user's menu choice
    choice = input("\nEnter your choice: ")

    # If the user enters 1, report a lost item
    if choice == "1":

        # Call add_item with Lost as the item type
        add_item("Lost")

    # If the user enters 2, report a found item
    elif choice == "2":

        # Call add_item with Found as the item type
        add_item("Found")

    # If the user enters 3, display all items
    elif choice == "3":

        # Call the view_items function
        view_items()

    # If the user enters 4, search for an item
    elif choice == "4":

        # Call the search_item function
        search_item()

    # If the user enters 5, update item status
    elif choice == "5":

        # Call the mark_returned function
        mark_returned()

    # If the user enters 6, exit the application
    elif choice == "6":

        # Display a closing message
        print("Thank you for using Campus Lost & Found Tracker!")

        # Stop the while loop
        break

    # If the user enters anything else
    else:

        # Display an error message
        print("Invalid choice! Please try again.")

#====================================================================================================

# items = [] – Creates an empty list.
# {} – Creates a dictionary.
# def – Defines a function.
# input() – Gets information from the user.
# append() – Adds an item to a list.
# len() – Counts the number of items.
# for – Repeats through items in a list.
# if-else – Checks conditions.
# lower() – Converts text to lowercase.
# str() – Converts a value into a string.
# break – Stops a loop.