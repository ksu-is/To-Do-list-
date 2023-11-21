def show_menu():
    print("1. View To-Do List\n2. Add Task\n3. Mark Task as Done\n4. Quit")

def main():
    todo_list = []

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

