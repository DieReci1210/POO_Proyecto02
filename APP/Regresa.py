from tkinter import*
import tkinter as tk
from PIL import ImageTk, Image

regresa = Tk()
regresa.title("Regresa")
regresa.geometry("1000x600")
regresa.config(bg="white")

borde = Frame(regresa, width=1000,height=650)
borde.configure(bg="white")
borde.pack()


titulo = ImageTk.PhotoImage(Image.open("TITULO REGRESA.png"))
imagen = Label(borde, image = titulo)
imagen.place(x=0,y=0)

texto = ImageTk.PhotoImage(Image.open("TEXTO REGRESA.png"))
imagen = Label(borde, image = texto)
imagen.place(x=0,y=150)

                        



