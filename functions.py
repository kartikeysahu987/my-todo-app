def read_todos(filepath='todos.txt'):
    with open(filepath , 'r') as file:
        todos = file.readlines()

    return todos
def write_lines(todo,filepath='todos.txt'):
    with open(filepath, 'w') as file:
        file.writelines(todo)
    return
