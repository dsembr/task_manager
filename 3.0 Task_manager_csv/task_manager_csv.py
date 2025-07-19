import csv

# Simple To-Do List Manager - Step by Step Project

# Build a simple To-Do List app in Python.
# Features:
#   1. Add a new task to a list of things to do.
#   2. View all tasks to be done (with numbers).
#   3. Mark a task as done (move it from "to do" to "done" list and renumber).
#   4. View all completed (done) tasks.
#   5. Quit the program.

# TODO 1: Create two empty lists at the top of your script:
#    - 'all_tasks' for tasks to be done
#    - 'done_tasks' for completed tasks

all_tasks = []
done_tasks = []

#STEVEN
# TODO 2: Add functionality to read existing tasks from CSV files:
#    - Try to open "tasks.csv" and read its content into the 'all_tasks' list.
#    - Try to open "done_tasks.csv" and read its content into the 'done_tasks' list.
#    - Use the csv module.
#    - If the file is not found (FileNotFoundError), just use `pass` to skip loading.

# Example:
# import csv
#STEVEN
def read_files():
        
    try:
        with open("tasks.csv", "r") as file:
            reader_csv = csv.reader(file)
            for row in reader_csv: 
                if row != []:
                    all_tasks.append(row[0])
    except FileNotFoundError:
        pass

    try:
        with open("done_tasks.csv", "r") as file:
            reader_csv = csv.reader(file)
            for row in reader_csv: 
                if row != []:
                    done_tasks.append(row[0])
                    print(f"done_task : {row}")
    except FileNotFoundError:
        pass
read_files()
# TODO 3: Define a function called 'add_task'
def add_task():
    task = input("Enter a new task: ").strip()
    if task:
        all_tasks.append(task)
        print(f"The task '{task}' has been added to your tasks.")
    else:
        print("Task cannot be empty.")

# TODO 4: Define a function called 'view_tasks'
def view_tasks():
    if not all_tasks:
        print("No tasks to do.")
    else:
        print("These are the tasks you have left to do:")
        for i in range(len(all_tasks)):
            print(f"{i + 1}. {all_tasks[i]}")

# TODO 5: Define a function called 'view_done_task'
def view_done_task():
    if not done_tasks:
        print("No tasks have been completed yet.")
    else:
        print("These are the tasks that have been completed:")
        for i in range(len(done_tasks)):
            print(f"{i + 1}. {done_tasks[i]}")

# TODO 6: Define a function called 'mark_done'
def mark_done():
    if not all_tasks:
        print("No task to mark as done.")
        return
    view_tasks()
    try:
        num = int(input("Enter the number of the task you have completed: "))
        if 1 <= num <= len(all_tasks):
            completed_task = all_tasks.pop(num - 1)
            done_tasks.append(completed_task)
            print(f"Great Job! You have completed: {completed_task}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
#STEVEN
# TODO 7: Add functionality to save tasks to CSV files when the program ends:
#    - Write all_tasks to "tasks.csv"
#    - Write done_tasks to "done_tasks.csv"
#    - Use the csv module
#    - Each task should be written on its own line


def save_all_tasks():
    with open("Task.csv",mode="w",newline="") as file:
        write_csv = csv.writer(file)
        for task in all_tasks:
            write_csv.writerow([task])
            print(task)

    with open("Done_Task.csv",mode="w",newline="") as file:
        write_csv = csv.writer(file)
        for task in done_tasks:
            write_csv.writerow([task])
            print(task)

            
# Main Menu Loop
continue_app = True

while continue_app:
    print("\nTo-Do List Manager")
    print("1. Add a task")
    print("2. View tasks to be done")
    print("3. Mark a task as done")
    print("4. View completed tasks")
    print("5. Quit")

    choice = input("Enter your choice: ").strip()
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        view_done_task()
    elif choice == "5":
        save_all_tasks()
        print("Bye! See you later. All your tasks have been saved.")

        # TODO: Before exiting, save the current task lists to their respective CSV files.

        continue_app = False
    else:
        print("Invalid choice. Try again.")
