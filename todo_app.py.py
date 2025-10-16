
import os

FILENAME = "tasks.txt"

def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as file:
        tasks = [line.strip() for line in file.readlines()]
    return tasks

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def todo_app():
    tasks = load_tasks()
    print("=== TO-DO LIST APP ===")

    while True:
        print("\nOptions:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Clear All")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            new_task = input("Enter new task: ")
            tasks.append(new_task)
            save_tasks(tasks)
            print("Task added!")
        elif choice == "3":
            show_tasks(tasks)
            num = int(input("Enter task number to remove: "))
            if 0 < num <= len(tasks):
                removed = tasks.pop(num - 1)
                save_tasks(tasks)
                print(f"Removed: {removed}")
            else:
                print("Invalid number!")
        elif choice == "4":
            confirm = input("Are you sure? (y/n): ").lower()
            if confirm == "y":
                tasks.clear()
                save_tasks(tasks)
                print("All tasks cleared!")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again!")

todo_app()
