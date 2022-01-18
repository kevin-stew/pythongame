import random

options = ['rock','paper', 'scissors']
info = ['rules', 'play', 'quit', 'rpc', 'gn']

def comp_op(pick):
    choice = random.randint(0,2)
    return pick[choice]

def game():
    print("""
--------Welcome to Gaming Console 3000-------
You can:
1) Play 'Rock, Paper, Scissors' -- type 'rpc'
2) Play 'Guess the Number' -- type 'gn'
3) Quit  -- type 'quit'
""")

    while True:
        action = input("What would you like to do? ")
        if action.lower() == 'quit':
            break

        elif action.lower() == 'rules':
            print("""
---------The Rules---------
-Rock beats Scissors
-Scissors beats Paper
-Paper beats Rock

Capice?
            """)

        elif action not in info:
            print("""
-----------!!ERROR!!------------
Please remember, you can:
- view the rules -- type 'rules'
- play the game -- type 'play'
- or quit  -- type 'quit'
        """)
            
        elif action.lower() == 'rpc':
            rpc()

        elif action.lower() == 'gn':
            gn()

def rpc():           
    comp_choice = comp_op(options)
    user_choice = input("""
---------The Game---------  
Please enter an object: 
    - rock 
    - paper 
    - scissors  
        """)
    
    if user_choice == comp_choice:
        print(f"The computer picked {comp_choice}")
        print("Tie game")
    elif user_choice != comp_choice:
        if user_choice == 'rock' and comp_choice == 'scissors':
            print(f"The computer picked {comp_choice}")
            print("You win this round!")
        elif user_choice == 'scissors' and comp_choice == 'paper':
            print(f"The computer picked {comp_choice}")
            print("You win this round!")
        elif user_choice == 'paper' and comp_choice == 'rock':
            print(f"The computer picked {comp_choice}")
            print("You win this round!")
        elif user_choice not in options:
            print("""
            
-----------!!ERROR!!------------ 
As a reminder, your choices are: 
    - rock 
    - paper 
    - scissors 
        """)
        else:
            print(f"The computer picked {comp_choice}")
            print("Computer wins this round")

def gn():
        user_score = 0
        choice = random.randint(1,11)
        user_choice = ''
        while user_choice != 'quit' or user_choice != choice:
            user_choice = int(input("""
---------Random Number Game---------  
Please enter a number between 1 and 10
            """))
            if user_choice == choice:
                
                user_choice2 = input(f"""
                
------------CORRECT GUESS!------------
It took you {user_score + 1} attempts.

You can:
1) To return to the main menu -- type 'menu'
2) If you would like to play again -- type 'play'
        """)
                if user_choice2.lower() == 'play':
                    gn()
                elif user_choice2.lower() == 'menu':
                    game()                
            else:
                print("You guessed the wrong number. :(")
                user_score += 1

game()





