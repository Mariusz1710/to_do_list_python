import os
from colorama import Fore,Back,Style

tasks = {"wash the dishes":"to do","give Misiowa her food":"to do","go shopping":"done","learn programming":"in progress"}

def show_tasks():
    i = 1
    print("-------------------------------------------------------------------")
    for task,status in tasks.items():
        if status == "to do":
            print(Fore.RED + str(i) + ". " + task)
        elif status == "done":
            print(Fore.GREEN + str(i) + ". " + task)
        elif status == "in progress":
            print(Fore.BLUE + str(i) + ". " + task)
        i += 1
        print(Style.RESET_ALL)
    print("-------------------------------------------------------------------")
    os.system("pause")

def add_task():
    choice = "a"
    status = -1
    while choice != "x":
        print("Enter 'x' as a task if you want to exit")
        task = input("Enter a task:")
        if task == "x":
            return
        while True:
            status = int(input("""Enter the status of the task:
1. To do
2. In progress
3. Done"""))
            if status in (1,2,3):
                if status == 1:
                    tasks[task] = "to do"
                elif status == 2:
                    tasks[task] = "in progress"
                elif status == 3:
                    tasks[task] = "done"
                print(tasks)
                print("The task has been added")
                os.system("pause")
                return
            else:
                print("The wrong status!")

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