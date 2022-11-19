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
from tkinter import scrolledtext




class Relajate(Tk):
    
    def __init__(self):
        super().__init__()
        self.geometry("850x750")
        self.resizable(False, False)
        self.bg = PhotoImage(file="Relax.png")
        self.bg1 = Label(self, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        self.foto = PhotoImage(file = "Medita.png")
        self.button = tk.Button(self,  image = self.foto, borderwidth=6, highlightthickness=0, command=  self.video1)
        self.button.place(x=60, y=490)
        
        self.foto1 = PhotoImage(file = "Relajate.png")
        self.button1 = tk.Button(self,  image = self.foto1, borderwidth=6, highlightthickness=0, command = self.escribelo)
        self.button1.place(x=300, y=490)
        
        self.foto2 = PhotoImage(file = "Gratitud.png")
        self.button2 = tk.Button(self,  image = self.foto2, borderwidth=6, highlightthickness=0, command = self.gratitud)
        self.button2.place(x=540, y=490)
        
        
    
    def video1(self):
        self.videoplayer = TkinterVideo(master=self, scaled=True)
        self.videoplayer.load(r"1.mp4")
        self.videoplayer.pack(expand=True, fill="both")
        self.videoplayer.play()
        self.mainloop()
        
    def escribelo(self):
        
        self.geometry("850x750")
        self.resizable(False,False)
        self.bg = PhotoImage(file="Escribelo.png")
        self.bg1 = Label(self, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        self.entrada = StringVar()
        self.text_area = scrolledtext.ScrolledText(self.nweWindow, 
                                 wrap = tk.WORD, 
                                      width = 63, 
                                      height = 28, 
                                      font = ("League Spartan",
                                              13))
        self.text_area.grid(column = 0, pady = 145, padx = 134)
        self.returnbutton = tk.Button(self,text="Sign in", cursor="hand2", bg = "white", border = 0,  fg = "#28847F", font=("League Spartan underline",11)).place(x=264,y=520)
    def gratitud(self):   
        self.geometry("850x750")
        self.resizable(False,False)
        self.bg6 = PhotoImage(file="G.png")
        self.bg7 = Label(self, image=self.bg6).place(x=0, y=0, relwidth=1, relheight=1)

        
    

    
r = Relajate()
r.mainloop()


