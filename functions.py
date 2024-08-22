def get_todos():
    """
    This function read todos.txt file content
    and then return a list of todos
    :return: list of todos
    """
    with open('todos.txt', 'r') as file:
        todos = file.readlines()
    return todos
def set_todos(todos):
    """
    This function recieve todos.txt list as a argument
    Then write the latest changes on todos.txt.file
    :param: todos list
    """
    with open('todos.txt', 'w') as file:
        file.writelines(todos)