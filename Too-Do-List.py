tasks = []

def addTask():
    task = input("Please enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")

def listTasks():
    if not tasks:
        print("There are no tasks currently!")
    else:
        print("Current tasks:")
        for index, task in enumerate(tasks):
            print(f"Task #{index}: {task}")

def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Choose the number of the task you want to delete: "))
        if 0 <= taskToDelete < len(tasks):
            removed_task = tasks.pop(taskToDelete)
            print(f"Task '{removed_task}' has been removed.")
        else:
            print(f"Task #{taskToDelete} was not found.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except IndexError:
        print("Task number out of range. Please try again.")

print("Welcome to the TO-DO LIST App")
while True:
    print("\n")
    print("Please select one of the following options:")
    print("------------------------------------------")
    print("1. Add a task")
    print("2. Delete a task")
    print("3. List tasks")
    print("4. Quit")
   
    choice = input("Enter your choice: ")
   
    if choice == "1":
        addTask()
    elif choice == "2":
        deleteTask()
    elif choice == "3":
        listTasks()
    elif choice == "4":
        break
    else:
        print("Invalid input. Please try again.")

print("Goodbye!")
