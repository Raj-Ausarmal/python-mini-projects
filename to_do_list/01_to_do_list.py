print("==============================")
print("          TO-DO LIST")
print("==============================")

tasks = []

while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            print("\nYour tasks:")
            for number, task in enumerate(tasks, 1):
                print(f"{number}. {task}")

    elif choice == "3":
        if not tasks:
            print("No tasks to remove.")
        else:
            for number, task in enumerate(tasks, 1):
                print(f"{number}. {task}")

            number = int(input("Enter task number to remove: "))

            if 1 <= number <= len(tasks):
                print(f"Removed: {tasks.pop(number - 1)}")
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
