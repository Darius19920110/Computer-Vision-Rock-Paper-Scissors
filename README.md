# Computer-Vision-Rock-Paper-Scissors

> This is a Rock Paper Scissor Game Project
> ![r_p_s_main_screen](https://user-images.githubusercontent.com/59298965/177686875-73420a3b-e545-43a0-87e3-f49c854c98a0.png)
> ![r_p_s_computer_chosen_screen](https://user-images.githubusercontent.com/59298965/177686902-56110784-3b2c-4655-95b5-f507be91d853.png)
> ![r_p_s_in_game_screen](https://user-images.githubusercontent.com/59298965/177686922-7fbde68e-f5b3-4f1c-99d8-09c33cd2c394.png)
> ![r_p_s_showing_rock](https://user-images.githubusercontent.com/59298965/177686937-21dc1b39-009f-4efc-b1c5-ad722c3154c0.png)


## Milestone 1

- Made 4 groups of photos: rock, paper, scissors and nothing.
- Took photos of my hand showing rock,  paper, scissors and absolutely nothing.
- Uploaded those to the teachable Machine website, and trained these models.
- Converted the model to a Keras.h5 model and downloaded.

## Milestone 2

- Set Up virtual environment with conda
- Install dependencies (opencv-python, tensorflow, ipykernel, keras)
- Set up video capture window without conditions, added keras.h5 model to code.
```python
mport cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    # Press q to close the window
    print(prediction)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
```

## Milestone 3

- Create the rock, paper, scissors game logic with user input, without camera recognition.
- I created 4 functions:
    #### Get the computer choice
    - added the choices into a list.
    - used randrange to add an index to a list to pick random choice.
    - return the random choice
    #### Get User choice
    - I put the entire function in the while loop, because if the user input conditions does not valid, asking for input again.
    - return the user input
    #### Get Winner
    - Made If conditions to decide if computer or user the winner or draw.
    - return the results
    #### Play
    - This is the main function, wrap in all functions, also check who is the winner based on the return, and print to the screen, if draw, play function starts over, thats why I put this function into while loop.
```python
from random import random, randrange
from secrets import choice
import time

choices = ["rock", "paper", "scissors"]

def get_computer_choice():
    print("Computer Choosing...")
    time.sleep(3)

    randnum = randrange(0, 3)

    return choices[randnum]

def get_user_choice():
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


def play():
    while True:
        computer_choice = get_computer_choice()

        user_choice = get_user_choice()

        winner = get_winner(computer_choice, user_choice)

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

play()
```
## Milestone 4
- Creating the game logic with camera input
- Creating a basic GUI with tkinter

## Conclusions
- I learned how to use the camera to get user inputs.
- I was familiar with the rest of the tasks
- I did not used Classes, because it is small program, but can be upgrade to it for better scalability.
