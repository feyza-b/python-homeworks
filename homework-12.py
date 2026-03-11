todo_list = []

while True:

    print("1- Add")
    print("2- List")
    print("3- Delete")
    print("4- Complete")
    print("5- Exit")

    choice = input("Choose: ")

    if choice == "1":
        title = input("Enter the task: ")

        todo = {}
        todo["id"] = len(todo_list) + 1
        todo["title"] = title
        todo["completed"] = False

        todo_list.append(todo)

    elif choice == "2":
        for todo in todo_list:
            print(todo["id"], "-", todo["title"], "-", todo["completed"])

    elif choice == "3":
        delete_id = int(input("Enter id to delete: "))
        for todo in todo_list:
            if todo["id"] == delete_id:
                todo_list.remove(todo)

    elif choice == "4":
        complete_id = int(input("Enter id to complete: "))
        for todo in todo_list:
            if todo["id"] == complete_id:
                todo["completed"] = "completed"

    elif choice == "5":
        break