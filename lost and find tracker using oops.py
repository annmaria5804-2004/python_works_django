
# ==========================================
# CAMPUS LOST & FOUND TRACKER
# Using Class and Methods (OOP)
# ==========================================


# Create a class
class LostFoundTracker:

    # Constructor method
    def __init__(self):

        # Empty list to store all items
        self.items = []


    # ------------------------------------------
    # 1. METHOD TO ADD A LOST OR FOUND ITEM
    # ------------------------------------------

    def add_item(self, item_type):

        # Get item details
        name = input("Enter item name: ")
        location = input("Enter location: ")
        person = input("Enter your name: ")
        contact = input("Enter contact number: ")

        # Create a dictionary
        item = {
            "id": len(self.items) + 1,
            "type": item_type,
            "name": name,
            "location": location,
            "person": person,
            "contact": contact,
            "status": "Open"
        }

        # Add item to the list
        self.items.append(item)

        print("\nItem added successfully!")
        print("Your Item ID is:", item["id"])


    # ------------------------------------------
    # 2. METHOD TO VIEW ALL ITEMS
    # ------------------------------------------

    def view_items(self):

        # Check whether the list is empty
        if len(self.items) == 0:

            print("\nNo items reported yet.")

        else:

            print("\n===== ALL REPORTED ITEMS =====")

            # Loop through all items
            for item in self.items:

                print("\nItem ID:", item["id"])
                print("Type:", item["type"])
                print("Item Name:", item["name"])
                print("Location:", item["location"])
                print("Reported By:", item["person"])
                print("Contact:", item["contact"])
                print("Status:", item["status"])

                print("-----------------------------")


    # ------------------------------------------
    # 3. METHOD TO SEARCH FOR AN ITEM
    # ------------------------------------------

    def search_item(self):

        search = input("\nEnter item name to search: ")

        found = False

        # Check every item
        for item in self.items:

            # Case-insensitive search
            if search.lower() in item["name"].lower():

                print("\nItem found!")
                print("Item ID:", item["id"])
                print("Type:", item["type"])
                print("Item Name:", item["name"])
                print("Location:", item["location"])
                print("Status:", item["status"])

                found = True

        if found == False:

            print("No matching item found.")


    # ------------------------------------------
    # 4. METHOD TO MARK ITEM AS RETURNED
    # ------------------------------------------

    def mark_returned(self):

        item_id = input("\nEnter item ID: ")

        found = False

        # Check every item
        for item in self.items:

            # Compare item IDs
            if str(item["id"]) == item_id:

                if item["status"] == "Returned":

                    print("This item is already returned.")

                else:

                    item["status"] = "Returned"

                    print("Item marked as returned successfully!")

                found = True

                break

        if found == False:

            print("Invalid item ID.")


    # ------------------------------------------
    # 5. METHOD TO DISPLAY MAIN MENU
    # ------------------------------------------

    def main_menu(self):

        # Display menu continuously
        while True:

            print("\n===== CAMPUS LOST & FOUND TRACKER =====")

            print("1. Report Lost Item")
            print("2. Report Found Item")
            print("3. View All Items")
            print("4. Search Item")
            print("5. Mark Item as Returned")
            print("6. Exit")

            choice = input("\nEnter your choice: ")

            if choice == "1":

                self.add_item("Lost")

            elif choice == "2":

                self.add_item("Found")

            elif choice == "3":

                self.view_items()

            elif choice == "4":

                self.search_item()

            elif choice == "5":

                self.mark_returned()

            elif choice == "6":

                print("Thank you for using Campus Lost & Found Tracker!")

                break

            else:

                print("Invalid choice! Please try again.")


# ------------------------------------------
# 6. CREATE OBJECT AND RUN PROGRAM
# ------------------------------------------

# Create an object of the class
tracker = LostFoundTracker()

# Call the main_menu method
tracker.main_menu()

