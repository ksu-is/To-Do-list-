def show_menu():
    print("1. View To-Do List\n2. Add Task\n3. Mark Task as Done\n4. Quit")

def main():
    todo_list = []

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("Your to-do list is empty." if not todo_list else f"To-Do List:\n{', '.join(todo_list)}")
        elif choice == "2":
            todo_list.append(input("Enter the task: "))
            print("Task added successfully!")
        elif choice == "3":
            print(f"Task '{todo_list.pop(int(input('Enter the task number to mark as done: ')) - 1)}' marked as done!" if todo_list else "Your to-do list is empty.")
        elif choice == "4":
            print("Goodbye!")
