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