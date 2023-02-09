# Todo Manager

todos = []
is_quit = False

while not is_quit:
    print("Type 'help' to see commands\n"
          "Type '1' to show todos\n"
          "Type '2' to create a todo\n"
          "Type '3' to remove a todo\n"
          "Type 'q' to quit\n")
    response = input("What would you like to do: ")

    if response == '2':
        todo = input("Enter the name of the todo: \n")
        todos.append(todo)
        print("Todo added to list\n")

    elif response == '1':
        if todos:
            print("Todos:")
            for i, todo in enumerate(todos):
                print(f"{i+1}. {todo}")
        else:
            print("No todos added")

    elif response == '3':
        if todos:
            print("Todos:")
            for i, todo in enumerate(todos):
                print(f"{i+1}. {todo}")

            index = int(input("Enter the number of the todo to delete: ")) - 1
            if 0 <= index < len(todos):
                del todos[index]
                print("Todo removed")
            else:
                print("Invalid index")
        else:
            print("No todos added")

    elif response == 'q':
        is_quit = True

    elif response == 'help':
        pass  # No need to repeat the instructions

    else:
        print("Invalid input")
