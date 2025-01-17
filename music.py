
from tkinter import *# means importing everything from tkinter
from tkinter import filedialog
import pygame
from pygame import mixer 
import datetime
import os

  
root=Tk()
root.title('Music player')
root.geometry("485x700+290+10")
root.configure(bg="#333333")
#root.resizable(width=False, height=False)
mixer.init()
pygame.mixer.init()


frameCnt =30
frames =[PhotoImage(file ="font.gif", format = 'gif - index %i' %(i)) for i in range(frameCnt)]  

def update(ind):
    frame = frame[ind]
    ind +=1
    if ind == frameCnt:
       ind = 0

    label.configure (image = frame)      
    root.after(40,update, ind)


label = Label(root)
label.place(x=0, y=0) 
root.after(0,update , 0)


def AddMusic():                                                    #function to call out music 
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
    
    for song in songs:
        if song.endswith(".mp3"):
            Playlist.insert(END,song)
def PlayMusic():                                                   #function to play music
    Music_Name = Playlist.get(ACTIVE)
    print(Music_Name(ACTIVE))
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()
    
      
Image_icon = PhotoImage(file ="icon.jpeg")                        #Importing the icon(logo)
root.iconphoto = (False , Image_icon)

Menu = PhotoImage(file="menu.jpeg")
Label(root,image=Menu).place(x=0,y=580,height=100 ,width=485)

Frame_Music = Frame(root, bd = 2 , relief = RIDGE )
Frame_Music.place(x=0, y=585, width=485, height= 100)

lower_frame=Frame(root,bg="white", width = 485, height = 180)  
lower_frame.place(x=0, y=400)

ButtonPlay = PhotoImage(file ="play.jpg")
Button(root, image=ButtonPlay, bg = "white", bd =0, height = 60, width = 60, command= PlayMusic).place(x = 215, y= 487)

ButtonStop = PhotoImage( file ="Stop.jpeg")
Button(root, image = ButtonStop, bg =  "white", bd = 0, height =60, width =60, command = mixer.music.stop).place(x=130, y=487)

ButtonPause = PhotoImage( file ="pause.jpeg.jpeg")
Button(root, image = ButtonPause, bg =  "white", bd = 0, height =60, width =60, command = mixer.music.pause).place(x=300, y=487)

Volume1 = PhotoImage(file = "volume.jpg")
panel = Label(root, image = Volume1).place(x=20, y=487)

Button(root, text = "Browse music", width=59 , height=1, font =("calibri", 12,"bold"), fg="Black",bg ="white", command = AddMusic).place(x=0, y=550)

Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width = 100, font =("Times new roman", 10), bg = "#333333", fg ="grey", selectbackground ="lightblue", cursor = "hand2", bd=0, yscrollcommand = Scroll.set)

Scroll.config(command = Playlist.yview)
Scroll.pack(side = RIGHT, fill = Y)
Playlist.pack(side = RIGHT, fill = BOTH)
 
song_list=Listbox(root, bg="black", fg="white", width=100)


root.mainloop()


