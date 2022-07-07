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