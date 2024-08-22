try:
    waiting_list =["jhon","marry"]
    name = input("enter your name ")
    number = waiting_list.index(name)
    print(f"{name}'s number is {number}")
except ValueError:
    print("Sorry we can't find that person")