import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import*
from tkinter.messagebox import showinfo
import ast
from tkVideoPlayer import TkinterVideo
from tkVideoPlayer import TkinterVideo
import pygame
pygame.init()

class Duermete(Tk):
    
    def __init__(self):
        super().__init__()
        self.title("Registro")
        self.geometry("850x750")
        self.resizable(False, False)
        self.bg2 = PhotoImage(file="c.png")
        self.bg3 = Label(self, image=self.bg2).place(x=0, y=0, relwidth=1, relheight=1)
        self.label3 = Label(self, text = "Modo Lluvia", fg = "black", bg = "white", font = ("Microsoft YaHei UI Bold", 14)).place(x=258, y=610)

        self.foto = PhotoImage(file = "2.png")
        self.button = tk.Button(self,  image = self.foto, borderwidth=0, highlightthickness=0, command = self.video1 )
        self.button.place(x=40, y=450)
        self.label = Label(self, text = "Modo Oceano", fg = "black", bg = "white", font = ("Microsoft YaHei UI Bold", 14)).place(x=60, y=610)

        self.foto2 = PhotoImage(file = "1.png")
        self.button2 = tk.Button(self,  image = self.foto2, borderwidth=0, highlightthickness=0, command = self.video2)
        self.button2.place(x=245, y=450)
        
        self.label = Label(self, text = "Modo Bosque", fg = "black", bg = "white", font = ("Microsoft YaHei UI Bold", 14)).place(x=458, y=610)

        
        self.foto3 = PhotoImage(file = "3.png")
        self.button3 = tk.Button(self,  image = self.foto3, borderwidth=0, highlightthickness=0, command = self.video3)
        self.button3.place(x=445, y=450)
        self.label4 = Label(self, text = "Modo Noche", fg = "black", bg = "white", font = ("Microsoft YaHei UI Bold", 14)).place(x=658, y=610)

        
        self.foto4 = PhotoImage(file = "4.png")
        self.button4 = tk.Button(self,  image = self.foto4, borderwidth=0, highlightthickness=0, command = self.video4)
        self.button4.place(x=645, y=450)
        
        
    def video1(self):
        self.videoplayer = TkinterVideo(master=self, scaled=True)
        self.videoplayer.load(r"Waves.mp4")
        self.videoplayer.pack(expand=True, fill="both")
        self.foto = PhotoImage(file = "BB1.png")
        self.button = tk.Button(self,  image = self.foto, borderwidth=0, highlightthickness=0, command=self.regresar).place(x=270, y=600)
        self.foto2 = PhotoImage(file = "BB2.png")
        self.button2 = tk.Button(self,  image = self.foto2, borderwidth=0, highlightthickness=0, command=self.stop1).place(x=430, y=600)
        self.videoplayer.play()
        self.mainloop()
    
    def play1(self):
        pygame.mixer.music.load("1.mp3") #Loading File Into Mixer
        pygame.mixer.music.play()
    def stop1(self):
        pygame.mixer.music.stop()
        statusbar['text'] = "Music Stopped"
        
        
    def video2(self):
        
        self.videoplayer2 = TkinterVideo(master=self, scaled=True)
        self.videoplayer2.load(r"LL.mp4")
        self.videoplayer2.pack(expand=True, fill="both")
        self.foto = PhotoImage(file = "BB1.png")
        self.button = tk.Button(self,  image = self.foto, borderwidth=0, highlightthickness=0, command=self.play2).place(x=270, y=600)
        self.foto2 = PhotoImage(file = "BB2.png")
        self.button2 = tk.Button(self,  image = self.foto2, borderwidth=0, highlightthickness=0, command=self.stop2).place(x=430, y=600)
        self.videoplayer2.play()
        self.mainloop()
    
    def play2(self):
        pygame.mixer.music.load("3l.mp3") #Loading File Into Mixer
        pygame.mixer.music.play()
    def stop2(self):
        pygame.mixer.music.stop()
        statusbar['text'] = "Music Stopped"
        
    def video3(self):  
        self.videoplayer3 = TkinterVideo(master=self, scaled=True)
        self.videoplayer3.load(r"forest.mp4")
        self.videoplayer3.pack(expand=True, fill="both")
        self.foto5 = PhotoImage(file = "BB1.png")
        self.button3 = tk.Button(self,  image = self.foto5, borderwidth=0, highlightthickness=0, command=self.play3).place(x=270, y=600)
        self.foto4 = PhotoImage(file = "BB2.png")
        self.button2 = tk.Button(self,  image = self.foto4, borderwidth=0, highlightthickness=0, command=self.stop3).place(x=430, y=600)
        self.videoplayer3.play()
        self.mainloop()
    
    def play3(self):
        pygame.mixer.music.load("forest.mp3") #Loading File Into Mixer
        pygame.mixer.music.play()
    def stop3(self):
        pygame.mixer.music.stop()
        statusbar['text'] = "Music Stopped"
    
    def video4(self):
        self.videoplayer = TkinterVideo(master=self, scaled=True)
        self.videoplayer.load(r"N4.mp4")
        self.videoplayer.pack(expand=True, fill="both")
        self.foto = PhotoImage(file = "BB1.png")
        self.button = tk.Button(self,  image = self.foto, borderwidth=0, highlightthickness=0, command=self.play4).place(x=270, y=600)
        self.foto2 = PhotoImage(file = "BB2.png")
        self.button2 = tk.Button(self,  image = self.foto2, borderwidth=0, highlightthickness=0, command=self.stop4).place(x=430, y=600)
        self.videoplayer.play()
        self.mainloop()
    
    def play4(self):
        pygame.mixer.music.load("2.mp3") #Loading File Into Mixer
        pygame.mixer.music.play()
    def stop4(self):
        pygame.mixer.music.stop()
        statusbar['text'] = "Music Stopped"
            

d = Duermete()
d.mainloop()

