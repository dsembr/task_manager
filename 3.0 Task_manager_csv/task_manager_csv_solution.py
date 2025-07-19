# Simple To-Do List Manager - Step by Step Project

# Build a simple To-Do List app in Python.
# Features:
#   1. Add a new task to a list of things to do.
#   2. View all tasks to be done (with numbers).
#   3. Mark a task as done (move it from "to do" to "done" list and renumber).
#   4. View all completed (done) tasks.
#   5. Quit the program.


import csv
# TODO 1: Create two empty lists at the top of your script:
#    - 'tasks' for tasks to be done
#    - 'done_tasks' for completed tasks

# Example:
all_tasks = []
done_tasks = []

# TODO 1B: Read files
def read_files():
    # Read tasks.csv
    try:
        with open("tasks.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row != []:
                    all_tasks.append(row[0])
    except FileNotFoundError:
        pass

    # Read done_tasks.csv
    try:
        with open("done_tasks.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row != []:
                    done_tasks.append(row[0])
    except FileNotFoundError:
        pass

read_files()
# TODO 2: Create a function called 'add_task'
#    - This function should:
#        1. Ask the user to enter a new task using input()
#        2. If the task is not empty, add it to the 'all_tasks' list
#        3. Print a message to say the task was added
def add_task():
    task = input("Enter a new task: ").strip()
    # if task != "":
    if task:
        all_tasks.append(task)
        print(f"The task '{task}'  has been added to your tasks")
    else:
        print("Task cannot be empty.")


    
    




# TODO 3: Create a function called 'view_tasks'
#    - This function should:
#        1. If there are no tasks, print "No tasks to do."
#        2. Otherwise, print each task in the 'all_tasks' list with a number (use f-strings and index+1)
def view_tasks():
    # if all_tasks ==  "":
    if not all_tasks:
        print("No tasks to do. ")
    else:
        print("These are the tasks you have left to do: ")
        for i in range(len(all_tasks)):
            print(f"{i+1}. {all_tasks[i]}")

# TODO 4: Create a function called 'view_done_tasks'
#    - This function should:
#        1. If there are no completed tasks, print "No tasks have been completed yet."
#        2. Otherwise, print each task in the 'done_tasks' list with a number
def view_done_task():
    if not done_tasks:
        print("No tasks have been completed yet.")
    else:
        print("These are the tasks that have been completed: ")
        for i in range(len(done_tasks)):
            print(f"{i+1}. {done_tasks[i]}")
# TODO 5: Create a function called 'mark_done'
#    - This function should:
#        1. If there are no tasks, print a message and return
#        2. Call your 'view_tasks' function to show current tasks
#        3. Ask the user for the number of the task they finished (use int(input(...)))
#        4. If the number is valid, remove that task from 'tasks' and add it to 'done_tasks'
#        5. Print a message saying which task was completed
#        6. If the number is not valid, print "Invalid task number."
def mark_done():
    if not all_tasks:
        print("No task to mark as done")
        return
    view_tasks()
    num = int(input("Enter the number of the task you have completed"))
    if 1 <= num <= len(all_tasks):
        completed_task = all_tasks.pop(num - 1)
        done_tasks.append(completed_task)
        print(f" Great Job! You have completed: {completed_task}")
    else:
        print("Invalid Task number")


# all_tasks = ['Reading the bible', 'Cooking', 'Dancing']
# 1. Reading the bible #0
# 2. Cooking #1
# 3. Dancing #2
# TODO 6: Write the main menu loop (not in a function)
#    - Use a while loop to:
#        1. Print menu options:
#             1. Add a task
#             2. View tasks to be done
#             3. Mark a task as done
#             4. View completed tasks
#             5. Quit
#        2. Ask for user input (choice)
#        3. If the user enters 1, call 'add_task'
#        4. If 2, call 'view_tasks'
#        5. If 3, call 'mark_done'
#        6. If 4, call 'view_done_tasks'
#        7. If 5, break the loop and exit the program
#        8. For any other input, print "Invalid choice. Try again."

def save_all_tasks():
    # Save all_tasks to tasks.csv
    with open("tasks.csv", "w", newline="") as file:
        writer = csv.writer(file)
        for task in all_tasks:
            writer.writerow([task])

    # Save done_tasks to done_tasks.csv
    with open("done_tasks.csv", "w", newline="") as file:
        writer = csv.writer(file)
        for task in done_tasks:
            writer.writerow([task])
# Example (inside your while loop):
continue_app = True

while continue_app:
    print("\n To- Do List  Manager")
    print("1. Add a task")
    print("2. View tasks to be done")
    print("3. Mark a task as done")
    print("4. View Completed Tasks")
    print("5. Quit")

    choice = int(input("Enter your choice: ").strip())
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        view_done_task()
    elif choice == "5":
        print("Bye! See you later. All your tasks have been saved")
        save_all_tasks()
        continue_app = False
        break
    else:
        print("Invalide Choice. Try again.")



