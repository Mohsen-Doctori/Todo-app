# print("hello world")
from functions import get_todos,set_todos
user_prompt = "enter a todo:"
todos = []
while True:
    user_action = input("enter add,show,edit,compelet,exit:")
    if user_action.startswith("add"):
            todos= get_todos()
            todo =user_action[4:]+"\n"
            todos.append(todo)
            set_todos(todos)
    if user_action.startswith("show"):
            todos = get_todos()
            for index, todo in enumerate(todos):
                print(index+1,"-",todo)
    if user_action.startswith("edit"):
        try:
            todos= get_todos()
            number=user_action[5:]+"\n"
            new_todo = input("edit this todo here")
            todos[int(number)-1]=new_todo
            set_todos(todos)
        except IndexError:
            print("your index is out of range")
    if user_action.startswith("compelet"):
        try:
            todos= get_todos()
            number =user_action[9:]+"\n"
            todos.pop(int(number) - 1)
            set_todos(todos)
        except IndexError:
            print("your index is out of range")
    if user_action.startswith("exit"):
            break
print("done!")
