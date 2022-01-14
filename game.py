import random

options = ['rock','paper', 'scissors']

def comp_op(pick):
    choice = random.randint(0,2)
    return pick[choice]

def game():
    user_choice = input("Please enter a number- 1: Rock 2: Scissors 3: Paper")
    comp_choice = comp_op()
    if user_choice == comp_op:
        "Tie"


print(comp_op(options))




