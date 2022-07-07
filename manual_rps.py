# Import randrange and time
from random import randrange
import time

# Add choices to a list
choices = ["rock", "paper", "scissors"]

def get_computer_choice():
    # Print to the consol and wait 3 sec to make it realistic that the computer choosing a number
    print("Computer Choosing...")
    time.sleep(3)

    # Generate random number from 0 to 2
    randnum = randrange(0, 3)

    # return the name of the choice
    return choices[randnum]

def get_user_choice():
    # Ask for user input, q for exit the program. If unknown word or number was added, start over.
    while True:
        try:
            choice = input("Your choice is: ")

            if choice.lower() == "rock":
                return "rock"
            elif choice.lower() == "paper":
                return "paper"
            elif choice.lower() == "scissors":
                return "scissors"
            elif choice.lower() == "q":
                return "exit"
            else:
                print("Invalid choice!")
                continue
        except:
            print("Invalid choice!")
            continue

def get_winner(computer_choice, user_choice):
    # Create condition who won, and return the winner name, or draw if same has been chosen

    # ! Rock
    if computer_choice == "rock" and user_choice == "rock":
        return "draw"
    elif computer_choice == "rock" and user_choice == "paper":
        return "user"
    elif computer_choice == "rock" and user_choice == "scissors":
        return "computer"
    # !Paper
    elif computer_choice == "paper" and user_choice == "rock":
        return "computer"
    elif computer_choice == "paper" and user_choice == "paper":
        return "draw"
    elif computer_choice == "paper" and user_choice == "scissors":
        return "user"
    # !Scissors
    elif computer_choice == "scissors" and user_choice == "rock":
        return "user"
    elif computer_choice == "scissors" and user_choice == "paper":
        return "computer"
    elif computer_choice == "scissors" and user_choice == "scissors":
        return "draw"
    elif user_choice == "exit":
        return "exit"

# This is the main function
def play():
    # Add function into infinite loop
    while True:
        # Create computer choice function and assign the return value to a variable
        computer_choice = get_computer_choice()

        # Create user choice function and assign the return value to a variable
        user_choice = get_user_choice()

        # Create winner function and assign the return value to a variable
        winner = get_winner(computer_choice, user_choice)

        # Conditions, if not met, start over. Print who won or if its draw
        if winner != "exit":
            print(f"Computer choose '{computer_choice.upper()}'")
            
        if winner == "draw":
            print("It is Draw!")
            print("Play Again!")
            time.sleep(3)
            continue
        elif winner == "computer":
            print("Computer Won!")
            break
        elif winner == "user":
            print("Congratulation, You Won!")
            break
        elif winner == "exit":
            break

# Create the Play function
play()