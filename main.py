import cv2
from keras.models import load_model
import numpy as np
# Import tkinter for GUI
import tkinter
from tkinter import *
# import get_prediction function
from camera_rps import get_prediction
from datetime import datetime, timedelta
model = load_model('keras_model.h5')

# Specify the location of the tkinter frame
tkinter_frame_location=[500,200]

# Function to change the tkinter frame position
def change_position(root_variable,x,y):
    root_variable.geometry("+{}+{}".format(x,y))
    root_variable.update()

# initialise tkinter window
gui=tkinter.Tk()
# Change the frame name
gui.title('CV2 control panel...')
gui_size=[tkinter_frame_location[0],tkinter_frame_location[1]-150]
change_position(gui,gui_size[0],gui_size[1])
frmMain = Frame(gui)

# Create total scores of computer and user, start with 0
total_scores = {"computer_total": 0, "user_total": 0}


def camera_app():
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    # Get the current time
    time_now = datetime.now()
    # Get the time after 1 second to generate waiting time between choices
    time_after_sec = time_now + timedelta(seconds=1)
    # Will be saved the current choice here
    current_choice = ""
    

    while True:
        # Make the game info text empty in tkinter frame
        game_info["text"] = ""

        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        print(prediction)
        # Get the result of the prediction list, send it to the get_prediction function
        prediction_result = get_prediction(prediction)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        # If the choice different, update the waiting time and wait again 1 second
        if current_choice != prediction_result["user_choice"]:
            current_choice = prediction_result["user_choice"]
            time_after_sec = datetime.now() + timedelta(seconds=5)

        current_time = datetime.now()

        # Make sure the 1 sec waiting time is elapsed and user choice is not nothing
        if current_time >= time_after_sec and prediction_result["user_choice"] != "":
            # Change the tkinter label texts
            user_choice["text"] = prediction_result["user_choice"]

            computer_choice["text"] = prediction_result["computer_choice"]

            # Find the winner and add score to the counter, and change game info text
            if prediction_result["winner"] == "user":
                user_point = int(user_score.cget("text"))
                user_point += 1
                total_scores["user_total"] += 1
                user_score["text"] = str(user_point)
                game_info["text"] = "You won this round!"

            elif prediction_result["winner"] == "computer":
                computer_point = int(computer_score.cget("text"))
                computer_point += 1
                total_scores["computer_total"] += 1
                computer_score["text"] = str(computer_point)
                game_info["text"] = "Computer won this round!"
            elif prediction_result["winner"] == "draw":
                game_info["text"] = "It is a Draw! Let`s try again!"

            # If the scores reached 3, its mean the game is over, so need to change button text etc
            if total_scores["user_total"] == 3 or total_scores["computer_total"] == 3:
                new_game_button["text"] = "New Game"
                
    
            if total_scores["computer_total"] == 3:
                game_info['text'] = "Computer Won!"
            elif total_scores["user_total"] == 3:
                game_info['text'] = "Congratulation! You Won!"
            break
            
    # After the loop release the cap object
    cap.release()
    #Destroy all the windows
    cv2.destroyAllWindows()

####### TKINTER GUI ###########
###############################          
def start_game_window():
    # Creating the starting window GUI
    global start_button

    header_text = tkinter.Label(gui, text="Rock Paper Scissors Game", font=("Arial", 20, "bold"))
    header_text.grid(row=0, column=0, pady=20, padx=50)
    
    # When button pressed, run running game window function
    start_button = tkinter.Button(gui, text="Start Game", command=running_game_window, height=5, width=20)
    start_button.grid(row=2, column=0, pady=10, padx=20)
    start_button.config(height=2, width=20)

def start_new_game():
    if total_scores["computer_total"] == 3 or total_scores["user_total"] == 3:
        global new_start_btn

        new_game_button.destroy()
        
        new_start_btn = tkinter.Button(gui, text="New Game", command=create_new_start_btn, height=5, width=20)
        new_start_btn.grid(row=5, column=1, pady=10, padx=20)
        new_start_btn.config(height=2, width=20)

        

def create_new_start_btn():
    # Delete widgets and reset user and computer scores
    total_scores["computer_total"] = 0
    total_scores["user_total"] = 0
    computer_label.destroy()
    computer_score.destroy()
    computer_choice.destroy()
    user_label.destroy()
    user_score.destroy()
    user_choice.destroy()
    new_start_btn.destroy()
    game_info.destroy()
    
    start_game_window()

# This is the window when game is in progress
def running_game_window():
    # Create some global widgets
    global computer_label
    global computer_choice
    global computer_score
    global user_label
    global user_choice
    global user_score
    global game_info
    global new_game_button

    # delete start_button and widgets
    start_button.destroy()
    computer_label = tkinter.Label(gui, text="Computer", font=("Arial", 12, "bold"))
    computer_label.grid(row=2, column=0, pady=5, padx=2, sticky=NW)
    computer_label.config(height=2, width=20)
    
    user_label = tkinter.Label(gui, text="User", font=("Arial", 12, "bold"))
    user_label.grid(row=2, column=1, pady=5, padx=2, sticky=NW)
    user_label.config(height=2, width=20)

    computer_score = tkinter.Label(gui, text="0", font=("Arial", 20, "bold"))
    computer_score.grid(row=3, column=0, pady=0, padx=2, sticky=NW)
    computer_score.config(height=2, width=14)

    user_score = tkinter.Label(gui, text="0", font=("Arial", 20, "bold"))
    user_score.grid(row=3, column=1, pady=0, padx=2, sticky=NW)
    user_score.config(height=2, width=14)

    computer_choice = tkinter.Label(gui, text="Computer chosen", font=("Arial", 10, "bold"))
    computer_choice.grid(row=4, column=0, pady=0, padx=27, sticky=NW)
    computer_choice.config(height=2, width=20)

    user_choice = tkinter.Label(gui, text="", font=("Arial", 10, "bold"))
    user_choice.grid(row=4, column=1, pady=0, padx=28, sticky=NW)
    user_choice.config(height=2, width=20)

    game_info = tkinter.Label(gui, text="", font=("Arial", 12, "bold"))
    game_info.grid(row=5, column=0, pady=0, padx=50, sticky=NW)
    game_info.config(height=2)

    new_game_button = tkinter.Button(gui, text="Choose one", command=lambda:[camera_app(), start_new_game()], height=5, width=20)
    new_game_button.grid(row=5, column=1, pady=10, padx=20)
    new_game_button.config(height=2, width=20)

# Make tkinter frame responsive
frmMain.grid(row=0, column=0, sticky="NESW")
frmMain.grid_rowconfigure(0, weight=1)
frmMain.grid_columnconfigure(0, weight=1)
gui.grid_rowconfigure(0, weight=1)
gui.grid_columnconfigure(0, weight=1)

# Create the first window GUI
start_game_window()

# start the tkinter mainloop
gui.mainloop()
####################################################
####################################################
            

