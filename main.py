import os
from colorama import Fore,Back,Style

tasks = {}

def load_tasks_from_file():
    try:
        file = open("tasks.txt")
        task_list = file.readlines()

        for tsk in task_list:
            t = tsk.strip("\n")
            t = t.split("STATUS")
            tasks[t[0]] = t[1]

    except:
        return

def show_tasks():
    i = 1
    print(Fore.RED + "Red colour - TO DO")
    print(Fore.BLUE + "Blue colour - IN PROGRESS")
    print(Fore.GREEN + "Green colour - DONE" + Style.RESET_ALL)
    print("-------------------------------------------------------------------")
    for task,status in tasks.items():
        if status == "to do":
            print(Fore.RED + str(i) + ". " + task + Style.RESET_ALL)
        elif status == "done":
            print(Fore.GREEN + str(i) + ". " + task + Style.RESET_ALL)
        elif status == "in progress":
            print(Fore.BLUE + str(i) + ". " + task + Style.RESET_ALL)
        i += 1
        
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
            try:
                print("""Enter the status of the task:
1. To do
2. In progress
3. Done""")
                status = int(input())

                if status in (1,2,3):
                    if status == 1:
                        tasks[task] = "to do"
                    elif status == 2:
                        tasks[task] = "in progress"
                    elif status == 3:
                        tasks[task] = "done"
                    print("The task has been added")
                    os.system("pause")
                    return
                else:
                    print("The wrong status!")
            except:
                print("The status must be a digit")

def del_task():
    
    while True:
        try:
            task = int(input('Enter the number of the task which you want to delete. Enter "0" if you want to exit'))
        except:
            print("The number must be a digit!")
            continue

        i = 0
        rem = -1

        if task == 0:
            return

        for key in tasks:
            if i == (task-1):
                rem = key
            i += 1
    
        if rem != -1:
            tasks.pop(rem)
            print("The has been deleted")
            os.system("pause")
            return
        else:
            print("There is no such number of a task!")
            os.system("pause")

def change_status():

    while True:
        try:
            task = int(input('Enter the number of the task which you want to change the status. Enter "0" if you want to exit'))
        except:
            print("The number must be a digit")
            os.system("pause")
            continue
        i = 0
        chg = -1
        status = -1

        if task == 0:
            return

        for key in tasks:
            if i == (task-1):
                chg = key
            i +=1

        if chg != -1:
            
            while status not in (1,2,3):
                try:
                    print("Choose the status:")
                    print(Fore.RED + "1. To do")
                    print(Fore.BLUE + "2. In progress")
                    print(Fore.GREEN + "3. Done" + Style.RESET_ALL)
                    print("0. Exit")

                    status = int(input())

                    if status in (1,2,3):
                        if status == 1:
                            tasks[chg] = "to do"
                        elif status == 2:
                            tasks[chg] = "in progress"
                        elif status == 3:
                            tasks[chg] = "done"
                        print("The status has changed")
                        os.system("pause")
                        return
                    elif status == 0:
                        break
                    else:
                        print("There is no such number of a status")
                        os.system("pause")
                except:
                    print("The status must be a digit")
                    os.system("pause")
        else:
            print("There is no such number of a task!")
            os.system("pause")


def save_tasks_to_file():
    file = open("tasks.txt","w")

    for task,status in tasks.items():
        file.write(task + " STATUS" + status + "\n")

choice = "-12345"
load_tasks_from_file()

while choice != "6":
    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        del_task()
    elif choice == "4":
        change_status()
    elif choice == "5":
        save_tasks_to_file()
    elif choice == "6":
        save_tasks_to_file()
        exit()
    elif choice == "-12345":
        pass
    else:
        print("You have entered the wrong option!")
        os.system("pause")

    os.system("cls")
    print("1. Show tasks")
    print("2. Add a task")
    print("3. Delete a task")
    print("4. Change a status of a task")
    print("5. Save a task")
    print("6. Exit")

    choice = input("Enter the number of the option: ")
    print()

print("Thank you for using our program")