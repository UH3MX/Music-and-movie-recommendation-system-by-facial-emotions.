from tkinter import *
import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
import cv2
import webbrowser

root = tk.Tk()
root.configure(background="black")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))


def play_song():
    webbrowser.open_new("https://www.youtube.com/watch?v=ZBvYre02Rps")

def play_song1():
    webbrowser.open_new("https://www.imdb.com/title/tt0272736/?ref_=ttls_li_tt")

def play_song2():
    webbrowser.open_new("https://www.youtube.com/watch?v=JunK_IrBj_s")

def play_song3():
    webbrowser.open_new("https://www.youtube.com/watch?v=jf2gOSORoqU")

def play_song4():
    webbrowser.open_new("https://www.youtube.com/watch?v=q1nBKfUtSOU")

def play_song5():
    webbrowser.open_new("https://www.youtube.com/watch?v=9Pq3UbRzxok")


root.title("happy")

label_l1 = tk.Label(root, text="!!___Happy Face Detected___!!", font=("Algerian", 35, 'bold'), bg="#ffccff", fg="black")
label_l1.place(x=250, y=20)

frame_alpr = tk.LabelFrame(root, text=" --Recommended Movies-- ", width=1200, height=820, bd=5, font=('Algerian', 14, ' bold '), bg="pink")
frame_alpr.grid(row=0, column=0, sticky='nw')
frame_alpr.place(x=40, y=90)

image3 = Image.open(r'C:/Users/dell/Downloads/100%_updated_music+movie_recommendation/100%_updated_music+movie_recommendation/happy_movies/1.jpg')
image3 = image3.resize((150, 150), Image.LANCZOS)
background_image3 = ImageTk.PhotoImage(image3)
background_label3 = tk.Label(root, image=background_image3, text="Yeh Jawaani Hai Deewani  ", compound='bottom')
background_label3.image = background_image3
background_label3.place(x=60, y=110)
my_link = tk.Button(root, text='Play', command=play_song, cursor='hand2', height=0, width=8, font=('times', 15, ' bold '), bg="brown4", fg="white")
my_link.place(x=80, y=290)

image4 = Image.open(r'C:/Users/dell/Downloads/100%_updated_music+movie_recommendation/100%_updated_music+movie_recommendation/happy_movies/2.jpg')
image4 = image4.resize((150, 150), Image.LANCZOS)
background_image4 = ImageTk.PhotoImage(image4)
background_label4 = tk.Label(root, image=background_image4, text="Mujhse Dosti Karoge!", compound='bottom')
background_label4.image = background_image4
background_label4.place(x=450, y=110)
my_link1 = tk.Button(root, text="Play ", command=play_song1, cursor='hand2', height=0, width=8, font=('times', 15, ' bold '), bg="brown4", fg="white")
my_link1.place(x=470, y=290)

image5 = Image.open(r'C:/Users/dell/Downloads/100%_updated_music+movie_recommendation/100%_updated_music+movie_recommendation/happy_movies/3.jpg')
image5 = image5.resize((150, 150), Image.LANCZOS)
background_image5 = ImageTk.PhotoImage(image5)
background_label5 = tk.Label(root, image=background_image5, text="Cocktail", compound='bottom')
background_label5.image = background_image5
background_label5.place(x=850, y=110)
my_link2 = tk.Button(root, text="Play ", command=play_song2, cursor='hand2', height=0, width=8, font=('times', 15, ' bold '), bg="brown4", fg="white")
my_link2.place(x=870, y=290)

image6 = Image.open(r'C:/Users/dell/Downloads/100%_updated_music+movie_recommendation/100%_updated_music+movie_recommendation/happy_movies/4.jpg')
image6 = image6.resize((150, 150), Image.LANCZOS)
background_image6 = ImageTk.PhotoImage(image6)
background_label6 = tk.Label(root, image=background_image6, text="Jab We Met", compound='bottom')
background_label6.image = background_image6
background_label6.place(x=840, y=360)
my_link3 = tk.Button(root, text="Play ", command=play_song3, cursor='hand2', height=0, width=8, font=('times', 15, ' bold '), bg="brown4", fg="white")
my_link3.place(x=870, y=540)

image7 = Image.open(r'C:/Users/dell/Downloads/100%_updated_music+movie_recommendation/100%_updated_music+movie_recommendation/happy_movies/5.jpg')
image7 = image7.resize((150, 150), Image.LANCZOS)
background_image7 = ImageTk.PhotoImage(image7)
background_label7 = tk.Label(root, image=background_image7, text="Rustom", compound='bottom')
background_label7.image = background_image7
background_label7.place(x=60, y=360)
my_link4 = tk.Button(root, text="Play ", command=play_song4, cursor='hand2', height=0, width=8, font=('times', 15, ' bold '), bg="brown4", fg="white")
my_link4.place(x=90, y=540)

image8 = Image.open(r'C:/Users/dell/Downloads/100%_updated_music+movie_recommendation/100%_updated_music+movie_recommendation/happy_movies/6.jpg')
image8 = image8.resize((150, 150), Image.LANCZOS)
background_image8 = ImageTk.PhotoImage(image8)
background_label8 = tk.Label(root, image=background_image8, text="Sita Ramam", compound='bottom')
background_label8.image = background_image8
background_label8.place(x=455, y=360)
my_link5 = tk.Button(root, text="Play ", command=play_song5, cursor='hand2', height=0, width=8, font=('times', 15, ' bold '), bg="brown4", fg="white")
my_link5.place(x=470, y=540)

root.mainloop()
