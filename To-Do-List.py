tasks = []

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Task")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    # Add Task
    if choice == 1:
        task = input("Enter new task: ")
        tasks.append({
            "task": task,
            "status": "Pending"
        })
        print("Task added successfully!")

    # View Task
    elif choice == 2:
        if len(tasks) == 0:
            print("No tasks available")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks):
                print(i + 1, ".", task["task"], "-", task["status"])

    # Complete Task
    elif choice == 3:
        number = int(input("Enter task number to complete: "))
        if number <= len(tasks):
            tasks[number - 1]["status"] = "Completed"
            print("Task completed!")
        else:
            print("Invalid task number")

    # Delete Task
    elif choice == 4:
        number = int(input("Enter task number to delete: "))
        if number <= len(tasks):
            tasks.pop(number - 1)
            print("Task deleted!")
        else:
            print("Invalid task number")

    # Exit
    elif choice == 5:
        print("Exiting To-Do List")
        break
    else:
        print("Invalid choice")