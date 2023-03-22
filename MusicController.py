import pygame
from tkinter import *
from tkinter.filedialog import askdirectory
from PIL import Image, ImageTk
import os


music_player = Tk()
music_player.title("Music Player")
music_player.geometry("800x900")
music_player.config(bg='#fff')
music_player.resizable(False, False)
music_player.iconbitmap("icon.ico")
#music_player.attributes('-alpha',0.9)لتجعل الشاشة شفافة


play_list = Listbox(font="Felt 30 bold",bg='#4a536b',selectmode=SINGLE)
play_list.pack(fill="both", expand="no")

my_img1 = ImageTk.PhotoImage(Image.open('url.jpg'))
my_label =Label(music_player,image=my_img1)
my_label.place(x=0,y=400)


icon1 = PhotoImage(file='music.png')
icon2 = PhotoImage(file='stop.png')
icon3 = PhotoImage(file='pause.png')
icon4 = PhotoImage(file='play-button-arrowhead.png')

var =StringVar()
song_title = Label(music_player,font="Felt 30 bold", textvariable=var, fg='green')
song_title.place(x=0,y=530)


directory = askdirectory()
os.chdir(directory)
song_list = os.listdir()

for item in song_list:
    pos = 0
    play_list.insert(pos, item)
    pos += 1
pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(play_list.get(ACTIVE))
    var.set(play_list.get(ACTIVE))
    pygame.mixer.music.play()
def stop():
    pygame.mixer.music.stop()
def pause():
    pygame.mixer.music.pause()
def unpause():
    pygame.mixer.music.unpause()

Button1 = Button(music_player, image=icon1, command=play)
Button2 = Button(music_player, image = icon2, command=stop)
Button3 = Button(music_player, image=icon3, command=pause)
Button4 = Button(music_player, image = icon4, command=unpause)

Button1.place(x=700, y = 800)
Button2.place(x=700, y = 850)
Button3.place(x=700, y = 700)
Button4.place(x=700, y = 750)

music_player.mainloop()
