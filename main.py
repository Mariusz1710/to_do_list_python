import os


tasks = {"wash the dishes":"to do","give Misiowa her food":"to do","go shopping":"done","learn programming":"in progress"}

def show_tasks():
    i = 1
    print("-------------------------------------------------------------------")
    for task in tasks:
        print(str(i) + ". " + task)
        i += 1
    print("-------------------------------------------------------------------")
    os.system("pause")

def add_task():
    task = input("Enter a task:")
    tasks.append(task)
    print("The task has been added")
    os.system("pause")

def del_task():
    task = int(input("Enter the number of the task which you want to delete"))
    tasks.pop(task-1)
    print("The has been deleted")
    os.system("pause")

def save_tasks_to_file():
    file = open("tasks.txt","w")

    for task in tasks:
        file.write(task + "\n")

choice = "-1"


while choice != "5":
    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        del_task()
    elif choice == "4":
        save_tasks_to_file()

    os.system("cls")
    print("1. Show tasks")
    print("2. Add a task")
    print("3. Delete a task")
    print("4. Save a task")
    print("5. Exit")

    choice = input("Enter the number of the option: ")
    print()

print("Thank you for using our program")