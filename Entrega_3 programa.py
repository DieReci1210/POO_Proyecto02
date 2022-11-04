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
import tkinter as tk
from tkinter import ttk
import sqlite3


class Main(tk.Tk):
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        self.title('Mentally')
        self.geometry("1000x600")
        self.resizable(False, False)
        
        paginas = tk.Frame(self)
        paginas.pack(side="top", fill="both", expand=True)
        paginas.grid_rowconfigure(0, weight=1)
        paginas.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        for Paginas in (Registro, Login, App, Relajate, Duermete):
            frame = Paginas(paginas, self)
            self.frames[Paginas] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            
        self.show_Ventana(Registro)
            
    def show_Ventana(self, paginas):
        ventana = self.frames[paginas]
        ventana.tkraise()
            
class Registro(tk.Frame):
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent, bg = "white" )
        self.image1 = tk.PhotoImage(file="PI5.png")
        self.w = self.image1.width()
        self.h = self.image1.height()


        self.panel1 = tk.Label(self, image=self.image1)
        self.panel1.pack(side='top', fill='both', expand='yes')

        self.panel1.image = self.image1
        
        
        
                
        self.username = StringVar()
        self.contraseña = StringVar()
        self.email = StringVar()
        self.confirm = StringVar()
        
        
        
        self.entrada_username= tk.Entry(self, textvariable=self.username, width=29,bd=0,font=("League Spartan",13)).place(x=50,y=185)
        
        
        self.entrada_contraseña = tk.Entry(self, textvariable=self.contraseña, width=25,bd=0,  font=("League Spartan",15),show="*").place(x=45,y=335)
        
        self.entrada_email= tk.Entry(self, textvariable=self.email, width=29,bd=0, font=("League Spartan",13)).place(x=50,y=263)
        self.confirm_entrada = tk.Entry(self, textvariable=self.confirm, width=25,bd=0,  font=("League Spartan",15),show="*").place(x=45,y=422)

        self.label = tk.Label(self, text = "Already have an account?", fg = "black", bg = "white", font = ('Microsoft YaHei UI Light', 11)).place(x=70, y=520)
    
        self.button2 = tk.Button(self,text="Sign in", cursor="hand2", bg = "white", border = 0,  fg = "#28847F", font=("League Spartan underline",11), command = (lambda: self.cambiar_Pagina(controller))).place(x=264,y=520)

        self.button = tk.Button(self,text="Create new Account", bg = "#7CBD7D", width = 45, pady = 7,  relief = "flat", border = 0, font = ("League Spartan",12), command = (lambda: self.save())).place(x=20,y=465)
           
            
    def save(self):
        self.name = self.username.get()
        self.contra = self.contraseña.get()
        self.em = self.email.get()
        conn = sqlite3.connect("Mentally.db")
        with conn:
            cur=conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS Info(username, contraseña, email)")
            cur.execute("INSERT INTO Info(username, email, contraseña) VALUES(?,?,?)", (self.name, self.contra, self.em))
            conn.commit()
            


    def cambiar_Pagina(self, controller):
        controller.show_Ventana(Login)
        self.button2.config()


class Login(tk.Frame):


    def __init__(self, parent, controller):
    
    

        tk.Frame.__init__(self, parent, bg = "white" )
        self.image1 = tk.PhotoImage(file="PI4.png")
        self.w = self.image1.width()
        self.h = self.image1.height()


        self.panel1 = tk.Label(self, image=self.image1)
        self.panel1.pack(side='top', fill='both', expand='yes')

        self.panel1.image = self.image1
        
        self.username = StringVar()
        self.contraseña = StringVar()
        
        self.entrada_username= tk.Entry(self, textvariable=self.username, width=29,bd=0,font=("League Spartan",13)).place(x=70,y=270)
        
        self.entrada_contraseña = tk.Entry(self, textvariable=self.contraseña, width=29,bd=0,font=("League Spartan",15),show="*").place(x=70,y=360)

        self.label = tk.Label(self, text = "Don´t have an account yet?", fg = "black", bg = "white", font = ('Microsoft YaHei UI Light', 11)).place(x=70, y=520)
        self.button2 = tk.Button(self,text="Sign up", cursor="hand2", bg = "white", border = 0, fg = "#28847F", font=("League Spartan underline",11), command = (lambda: self.cambiar_Pagina(controller))).place(x=266,y=521)
        
        self.button = tk.Button(self,text="Ingresar", bg = "#7CBD7D", width = 39,pady = 10,  relief = "flat", border = 0, font = ("League Spartan",12), command = (lambda: self.login(controller))) .place(x=50,y=435)
        
    def login(self, controller):
       
        conn = sqlite3.connect("Mentally.db")
        c = conn.cursor()
        
        self.name = self.username.get()
        self.contra = self.contraseña.get()
        
        c.execute('SELECT * FROM Info WHERE username = ? AND contraseña = ?', (self.name, self.contra))

        if c.fetchall():
            controller.show_Ventana(App)
            self.button2.config()

        c.close()

        
            
    def cambiar_Pagina(self, controller):
        controller.show_Ventana(Registro)
        self.button2.config()
        
    
        
class App(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg = "white" )
        self.image1 = tk.PhotoImage(file="Menu(Principal).png")
        self.w = self.image1.width()
        self.h = self.image1.height()
        
        self.panel1 = tk.Label(self, image=self.image1)
        self.panel1.pack(side='top', fill='both', expand='yes')

        self.panel1.image = self.image1
    


    # Creación de botones
        self.foto = PhotoImage(file = "B4.png")
        self.button = tk.Button(self,  image = self.foto, borderwidth=0, highlightthickness=0)
        self.button.place(x=40, y=330)
        self.label1 = Label(self, text = "Alegrate", fg = "black", font = ("League Spartan bold", 16)).place(x=810, y=550)
        
        self.foto2 = PhotoImage(file = "B3.png")
        self.button2 = tk.Button(self,  image = self.foto2, borderwidth=0, highlightthickness=0, command = (lambda: self.cambiar_Pagina2(controller)))
        self.button2.place(x=280, y=330)
        self.label2 = Label(self, text = "Regresa", fg = "black", font = ("League Spartan bold", 16)).place(x=570, y=550)
        
        self.foto3 = PhotoImage(file = "11.png")
        self.button3 = tk.Button(self,  image = self.foto3, borderwidth=0, highlightthickness=0, command = (lambda: self.cambiar_Pagina1(controller)))
        self.button3.place(x=760, y=330)
        self.label3 = Label(self, text = "Relajate", fg = "black", font = ("League Spartan bold", 16)).place(x=350, y=550)
        
        self.foto4 = PhotoImage(file = "B1 (210 × 210 px).png")
        self.button4 = tk.Button(self,  image = self.foto4, borderwidth=0, highlightthickness=0, command = (lambda: self.cambiar_Duermete(controller)))
        self.button4.place(x=510, y=330)
        self.label4 = Label(self, text = "Duermete", fg = "black", font = ("League Spartan bold", 16)).place(x=120, y=550)
        
        self.button = Button(self,text="¡Mentally!", bg = "black", fg = "white", width = 25, pady = 7,  relief = "flat", border = 0, font = ("League Spartan",12)) .place(x=500,y=250)
    def cambiar_Pagina1(self, controller):
        controller.show_Ventana(Relajate)
        self.button3.config()
        
    def cambiar_Duermete(self, controller):
        controller.show_Ventana(Duermete)
        self.button4.config()
        
    def cambiar_Pagina2(self, controller):
        controller.show_Ventana(Regresa)
        self.button2.config()
    
#     def cambiar_Pagina3(self, controller):
#         controller.show_Ventana(Regresa)
#         self.button2.config()
#     
#     def cambiar_Pagina(self, controller):
#         controller.show_Ventana(Alegrate)
#         self.button1.config()
#         
class Relajate(tk.Frame):

        
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg = "white" )
        self.image1 = tk.PhotoImage(file="Relajate.png")
        self.w = self.image1.width()
        self.h = self.image1.height()
        
        self.panel1 = tk.Label(self, image=self.image1)
        self.panel1.pack(side='top', fill='both', expand='yes')

        self.panel1.image = self.image1
    



        self.foto = PhotoImage(file = "Meditalo.png")
        self.button = tk.Button(self,  image = self.foto, borderwidth=6, highlightthickness=0, command=self.video1)
        self.button.place(x=60, y=380)
        
        self.foto1 = PhotoImage(file = "Escribelo.png")
        self.button1 = tk.Button(self,  image = self.foto1, borderwidth=6, highlightthickness=0, command = self.escribelo)
        self.button1.place(x=350, y=380)
        
        self.foto2 = PhotoImage(file = "Agradece.png")
        self.button2 = tk.Button(self,  image = self.foto2, borderwidth=6, highlightthickness=0, command = self.gratitud)
        self.button2.place(x=640, y=380)
        
        self.button5 = tk.Button(self,text="⌂ ", cursor="hand2", bg = "#EFEFEF", border = 0,  fg = "black", font=("League Spartan underline",40), command = (lambda: self.cambiar_Pagina(controller))).place(x=900,y=10)
    
    def video1(self):
        self.videoplayer = tk.Toplevel()
        self.videoplayer = TkinterVideo(master=self.videoplayer, scaled=True)
        self.videoplayer.load(r"1.mp4")
        self.videoplayer.pack(expand=True, fill="both")
        self.videoplayer.play()
        self.mainloop()
        
    def escribelo(self):
        self.newWindow1 = tk.Toplevel()
        self.newWindow1.geometry("850x750")
        self.newWindow1.resizable(False,False)
        self.bg = PhotoImage(file="Escribir (850 × 750 px).png")
        self.bg1 = Label(self.newWindow1, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        self.entrada = StringVar()
        self.text_area = scrolledtext.ScrolledText(self.newWindow1, 
                                 wrap = tk.WORD, 
                                      width = 63, 
                                      height = 28, 
                                      font = ("League Spartan",
                                              13))
        self.text_area.grid(column = 0, pady = 145, padx = 134)
        
    def gratitud(self):   
       self.newWindow = tk.Toplevel()
       self.newWindow.geometry("850x750")
       self.newWindow.resizable(False,False)
       self.bg6 = PhotoImage(file="G.png")
       self.bg7 = Label(self.newWindow, image=self.bg6).place(x=0, y=0, relwidth=1, relheight=1)
                
    def cambiar_Pagina(self, controller):
        controller.show_Ventana(App)
        self.button5.config()

class Duermete(tk.Frame):
    
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent, bg = "white" )
        self.image1 = tk.PhotoImage(file="sueño.png")
        self.w = self.image1.width()
        self.h = self.image1.height()


        self.panel1 = tk.Label(self, image=self.image1)
        self.panel1.pack(side='top', fill='both', expand='yes')

        self.panel1.image = self.image1

        
        
        self.label3 = Label(self, text = "Modo Lluvia", fg = "black", bg = "white", font = ("Microsoft YaHei UI Bold", 14)).place(x=258, y=610)

        self.foto = PhotoImage(file = "2.png")
        self.button = tk.Button(self,  image = self.foto, borderwidth=0, highlightthickness=0)
        self.button.place(x=40, y=400)
        self.label = Label(self, text = "Modo Oceano", fg = "black", bg = "white", font = ("Microsoft YaHei UI Bold", 14)).place(x=60, y=610)

        self.foto2 = PhotoImage(file = "1.png")
        self.button2 = tk.Button(self,  image = self.foto2, borderwidth=0, highlightthickness=0)
        self.button2.place(x=270, y=400)
        
        self.label = Label(self, text = "Modo Bosque", fg = "black", bg = "white", font = ("Microsoft YaHei UI Bold", 14)).place(x=458, y=610)

        
        self.foto3 = PhotoImage(file = "3.png")
        self.button3 = tk.Button(self,  image = self.foto3, borderwidth=0, highlightthickness=0)
        self.button3.place(x=520, y=400)
        self.label4 = Label(self, text = "Modo Noche", fg = "black", bg = "white", font = ("Microsoft YaHei UI Bold", 14)).place(x=658, y=610)

        
        self.foto4 = PhotoImage(file = "4.png")
        self.button4 = tk.Button(self,  image = self.foto4, borderwidth=0, highlightthickness=0)
        self.button4.place(x=760, y=400)
        
        self.button6 = tk.Button(self,text="⌂ ", cursor="hand2", bg = "#EFEFEF", border = 0,  fg = "black", font=("League Spartan underline",30), command = (lambda: self.cambiar_Pagina(controller))).place(x=900,y=10)
        
    def cambiar_Pagina(self, controller):
        controller.show_Ventana(App)
        self.button6.config()
        

        
if __name__ == '__main__':
    app = Main()
    app.mainloop()
        
        
        
        
        
