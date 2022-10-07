from tkinter import*
import tkinter as tk
from PIL import ImageTk, Image

relajate = Tk()
relajate.title("Relajate")
relajate.geometry("1000x600")
relajate.config(bg="white")

borde = Frame(relajate, width=1000,height=650)
borde.configure(bg="white")
borde.pack()


titulo = ImageTk.PhotoImage(Image.open("TITULO RELAJATE.png"))
imagen = Label(borde, image = titulo)
imagen.place(x=0,y=0)

texto = ImageTk.PhotoImage(Image.open("TEXTO RELAJATE.png"))
imagen = Label(borde, image = texto)
imagen.place(x=0,y=150)

fotita = ImageTk.PhotoImage(Image.open("IMAGEN RELAJATE.png"))
imagen = Label(borde, image=fotita)
imagen.place(x=780, y=300)