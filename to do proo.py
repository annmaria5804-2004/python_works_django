
# To-Do List Application
#=========================================================================
tasks = [] # Create an empty list

# Function to add a task
def add_task():

    task = input("Enter your task: ") # append() is a list method used to add a new item to the end of a list.

    tasks.append({
        "name": task,
        "completed": False # It tells us whether the task is completed or not.
    })

    print("Task added successfully!")


# Function to view tasks
def view_tasks():

    if len(tasks) == 0: # calculates the number of items in a list.tasks is our list.
        print("No tasks available")

    else:
        print("\nYour Tasks:")
# represents the task dictionary.
        for i, task in enumerate(tasks, start=1): # i represents the task number.

            if task["completed"]:
                status = "Completed"
            else:
                status = "Pending"

            print(i, task["name"], "-", status)


# Function to complete a task
def complete_task():

    view_tasks() # Calls the view_tasks() function.

    if len(tasks) == 0:
        return # immediately stops the function.

    number = int(input("Enter task number: "))

    if 1 <= number <= len(tasks): # This checks whether the entered task number is valid.

        tasks[number - 1]["completed"] = True # Let's understand why we use number - 1.Python list indexing starts from zero. 

        print("Task completed successfully!")

    else:
        print("Invalid task number")


# Function to delete a task
def delete_task():

    view_tasks()

    if len(tasks) == 0:
        return

    number = int(input("Enter task number to delete: "))

    if 1 <= number <= len(tasks):

        tasks.pop(number - 1)

        print("Task deleted successfully!")

    else:
        print("Invalid task number")


# Main program
while True: #A while loop executes repeatedly as long as its condition is true.

    print("\n===== TO-DO LIST APPLICATION =====")

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        print("Thank you for using To-Do List!")
        break #break is used to stop the loop.

    else:
        print("Invalid choice!")
