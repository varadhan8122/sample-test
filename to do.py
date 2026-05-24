import json
import os

FILE_NAME = "todo_list.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, 'r') as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError):
            return []
    else:
        return []

def save_tasks(tasks):
    with open(FILE_NAME, 'w') as file:
        json.dump(tasks, file, indent=4)

def show_menu():
    print("\n--- TODO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    choice = input("Enter your choice (1-4): ")
    return choice

def add_task(tasks):
    task_title = input("Enter the task description: ")
    new_task = {
        "title": task_title,
        "done": False
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task '{task_title}' added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found. Your list is empty.")
    else:
        print("\n--- YOUR TASKS ---")
        for index, task in enumerate(tasks, start=1):
            status = "[]" if task['done'] else "[ ]"
            print(f"{index}. {status} {task['title']}")

def mark_done(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    try:
        task_num = int(input("\nEnter the task number to mark as done: "))
        if 0 < task_num <= len(tasks):
            tasks[task_num - 1]['done'] = True
            save_tasks(tasks)
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    try:
        task_num = int(input("\nEnter the task number to delete: "))
        if 0 < task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Task '{removed_task['title']}' deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()

    while True:
        choice = show_menu()

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_done(tasks)
        elif choice == '4':
            delete_task(tasks)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
