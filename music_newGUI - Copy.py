
import tkinter as tk

import os
import cv2
import numpy as np
import time
import warnings 
from PIL import Image , ImageTk 
import matplotlib.image as mpimg
from playsound import playsound
from tkvideo import tkvideo

warnings.filterwarnings("ignore", category=DeprecationWarning)
from keras.models import load_model
import emotion_1 as validate

#import CNNModel 

# from win32com.client import Dispatch
# speak = Dispatch("SAPI.SpVoice")

##############################################+=============================================================
image_x, image_y = 64, 64
basepath="E:/100%_music_recommendation_new_gui_ready"

##############################################+=============================================================
root = tk.Tk()

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h)) #video 

root.configure(background="white")
root.state('zoomed')
root.title("Music Recommendation  System")
#####################################################+
image2 = Image.open('m4.jpg')
image2 = image2.resize((w,h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)


##########

label_l1 = tk.Label(root, text="Movie Recommendation System",font=("bookman old style", 35, 'bold'),
                    background="Black", fg="white", width=30, height=1)
label_l1.place(x=300, y=10)
############################################




###################################################################################################################
def update_label(str_T):
    #clear_img()
    result_label = tk.Label(root, text=str_T, font=("bold", 25), bg='bisque2', fg='black')
    result_label.place(x=350, y=150)            
#################################################################################################################
def social():
           # from subprocess import call
        # call(['python','detection_emotion_practice.py'])
    validate.upload()
    prediction_emotion()
def prediction_emotion():
    #clear_img()
    #update_label("Model Training Start...............")

    start = time.time()

    result = validate.files_count()
    #validate.files_count()
    end = time.time()
    #print("---" + result)
    ET = "Execution Time: {0:.4} seconds \n".format(end - start)

    msg = "Model Training Completed.." + '\n' + str(result) + '\n'+ ET

    update_label(msg)  
    if result=="Person is Happy.So this is the song for Him/Her":
        playsound('happy.mp3')
    elif result=="Person is Neutral.So this is the song for Him/Her":
        playsound('neutral.mp3')
    else:
        playsound('sad.mp3')
def prediction_emotion1():
    #clear_img()
    #update_label("Model Training Start...............")

    start = time.time()

    result = validate.files_count()
    #validate.files_count()
    # end = time.time()
    # #print("---" + result)
    # ET = "Execution Time: {0:.4} seconds \n".format(end - start)

    # msg = "Model Training Completed.." + '\n' + str(result) + '\n'+ ET

    # update_label(msg)  
    if result=="Person is Happy.So this is the song for Him/Her":
        #playsound('happy.mp3')
        from subprocess import call
        call(["python", "happy.py"])
        
    elif result=="Person is Neutral.So this is the song for Him/Her":
       # playsound('neutral.mp3')
        from subprocess import call
        call(["python", "neutral.py"])
        
    else:
       # playsound('sad.mp3')
        from subprocess import call
        call(["python", "sad.py"])
        
      
#def genery():
  #  from subprocess import call
   # call(["python","expression_Analysis.py"])        
        

        
def window():
    root.destroy()
#button2 = tk.Button(root, text="Music Genery ", command=genery,width=19, height=1, font=('times', 15, ' bold '),bg="lightblue",fg="black")
#button2.place(x=650, y=300)

button3 = tk.Button(root, text=" Expression Evaluation ",bd=5, command=social,width=19, height=1, font=('times', 15, ' bold '),bg="black",fg="white")
button3.place(x=650, y=500)
def on_enter(e):
    button3['background'] = 'gray'

def on_leave(e):
    button3['background'] = 'black'

button3.bind("<Enter>", on_enter)
button3.bind("<Leave>", on_leave)

# button4 = tk.Button(root, text=" Music Play List ", bd=5,command=prediction_emotion1,width=19, height=1, font=('times', 15, ' bold '),bg="lightblue",fg="black")
# button4.place(x=650, y=500)
# def on_enter(e):
#     button4['background'] = 'green'

# def on_leave(e):
#     button4['background'] = 'lightblue'

# button4.bind("<Enter>", on_enter)
# button4.bind("<Leave>", on_leave)


exit = tk.Button(root, text="Exit", bd=5,command=window, width=19, height=1, font=('times', 15, ' bold '),bg="red",fg="white")
exit.place(x=650, y=600)
def on_enter(e):
    exit['background'] = 'red'



root.mainloop()