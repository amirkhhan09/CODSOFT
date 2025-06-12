# todo.py

# 🔸 Author: Amir Khan
# 🔸 Internship: CodSoft (Python Programming)
# 🔸 Task 1: To-Do List App

todo_items = []

def display_menu():
    print("\n📝 TO-DO LIST MENU")
    print("1. ➕ Add Task")
    print("2. 📄 View Tasks")
    print("3. ✏️ Edit Task")
    print("4. ❌ Remove Task")
    print("5. 🚪 Exit")

def add_task():
    task = input("Enter your new task: ")
    todo_items.append(task)
    print(f"✅ Task '{task}' added!")

def view_tasks():
    if not todo_items:
        print("⚠️ Your to-do list is empty.")
    else:
        print("\n📋 Your Tasks:")
        for index, task in enumerate(todo_items, start=1):
            print(f"{index}. {task}")

def edit_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to update: "))
        if 1 <= task_num <= len(todo_items):
            new_task = input("Enter new task: ")
            todo_items[task_num - 1] = new_task
            print("✏️ Task updated successfully!")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❗ Please enter a valid number.")

def remove_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(todo_items):
            removed = todo_items.pop(task_num - 1)
            print(f"🗑️ Task '{removed}' deleted.")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❗ Please enter a valid number.")

# 🔁 Main Loop
while True:
    display_menu()
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        edit_task()
    elif choice == '4':
        remove_task()
    elif choice == '5':
        print("👋 Exiting... Good luck with your tasks!")
        break
    else:
        print("❗ Invalid input. Please choose between 1-5.")
