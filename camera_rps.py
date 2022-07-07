# Import randrange and time
from random import random, randrange

# Add choices to a list
choices = ["rock", "paper", "scissors"]

# This is the main function
def get_prediction(prediction):
    # Send the prediction data to play function for calculations and return the value
    play_results = play(prediction)
    return play_results

def get_computer_choice():
    # Generate random number from 0 to 2
    randnum = randrange(0, 3)
    # return the name of the choice
    return choices[randnum]

def get_user_choice(prediction):
    # Creating basic instances
    choice_values = {"name": "", "number": 0, "index": 3}

    # Looping through from 0 to 3 => 0=rock, 1=paper, 2=scissors, 3=nothing
    # these are the values from the camera which choice is the user chosen
    for i in range(0, 4):
        # Find the highest number from the list, which is what the user chosen
        if float(prediction[0][i]) > choice_values["number"]:
            # assign the numerical values and the index of the highest number 
            choice_values["number"] = float(prediction[0][i])
            choice_values["index"] = i

    # Find the name of the choice
    if choice_values["index"] == 0:
        choice_values["name"] = "rock"
    elif choice_values["index"] == 1:
        choice_values["name"] = "paper"
    elif choice_values["index"] == 2:
        choice_values["name"] = "scissors"
    elif choice_values["index"] == 3:
        choice_values["name"] = "nothing"
    # Return the name of the choice
    return choice_values["name"]

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


def play(prediction):
    # Create computer choice function and assign the return value to a variable
    computer_choice = get_computer_choice()

    # Create user choice function and assign the return value to a variable
    user_choice = get_user_choice(prediction)

    # Check if user chosen nothing, return empty values
    if user_choice == "nothing":
        return {"computer_choice": "",
            "user_choice": "",
            "winner": ""
    }
    else:
        # If there is choice other then nothing, send choices to get_winner function to find the winner    
        winner = get_winner(computer_choice, user_choice)

        # return the computer choice, user choice and who is the winner
        return {"computer_choice": computer_choice,
            "user_choice": user_choice,
            "winner": winner
        }    