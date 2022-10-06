from tkinter import*
import tkinter as tk
from PIL import ImageTk, Image



menu = Tk()
menu.geometry("1000x600")
menu.configure(bg="white")


borde = Frame(menu, width=1000,height=650)
borde.configure(bg="white")
borde.pack()

logo = ImageTk.PhotoImage(Image.open("LOGO APP.png"))
imagen = Label(borde, image = logo)
imagen.pack()


imagen_botona = ImageTk.PhotoImage(Image.open("Boton03 (1).png"))

botona = ttk.Button(image=imagen_botona)
botona.place(x=390,y=328)


imagen_botonb = ImageTk.PhotoImage(Image.open("Boton01.png"))

botona = ttk.Button(image=imagen_botonb)
botona.place(x=50,y=125)

imagen_botonC = ImageTk.PhotoImage(Image.open("Boton04 (1).png"))

botona = ttk.Button(image=imagen_botonC)
botona.place(x=206,y=328)

imagen_botond = ImageTk.PhotoImage(Image.open("Boton02.png"))

botona = ttk.Button(image=imagen_botond)
botona.place(x=577,y=328)




menu.mainloop()
