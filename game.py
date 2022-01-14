import random

options = ['rock','paper', 'scissors']

def comp_op(pick):
    choice = random.randint(0,2)
    return pick[choice]

def game():

        print("""
            -----Welcome to Rock_Paper_Scissors ----
            You can:
            - view the rules -- type 'rules'
            - play the game -- type 'play'
            - or quit  -- type 'quit'
            """)

        while True:
            action = input("What would you like to do? ")
            if action.lower() == 'quit':
                break

            elif action.lower() == 'rules':
                print("""
                ---------The Rules---------
                -Rock beats scissors
                -scissors beats paper
                -paper beats rock

                capice?
                """)

            elif action.lower() == 'play':
                
                comp_choice = comp_op(options)
                user_choice = input("""
                    ---------The Game---------  
                    Please enter object: 
                        1: rock 
                        2: paper 
                        3: scissors 
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
                    else:
                        print(f"The computer picked {comp_choice}")
                        print("Computer wins this round")
game()

    user_choice = input("Please enter a number- 1: Rock 2: Scissors 3: Paper")
    comp_choice = comp_op()
    if user_choice == comp_op:
        "Tie"


print(comp_op(options))





