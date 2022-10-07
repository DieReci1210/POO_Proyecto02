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



class Registro(Tk):
    
    def __init__(self):
        super().__init__()
        

        self.title("Registro")
        self.geometry("1000x600")
        self.resizable(False, False)
        self.bg = PhotoImage(file="PI5.png")
        self.bg1 = Label(self, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        
        self.username = StringVar()
        self.contraseña = StringVar()
        self.email = StringVar()
        self.confirm = StringVar()

        
        self.entrada_username=Entry(self, textvariable=self.username, width=29,bd=0,font=("League Spartan",13)).place(x=50,y=185)
        
        
        self.entrada_contraseña = Entry(self, textvariable=self.contraseña, width=25,bd=0,  font=("League Spartan",15),show="*").place(x=45,y=335)
        
        self.entrada_email=Entry(self, textvariable=self.email, width=29,bd=0, font=("League Spartan",13)).place(x=50,y=263)
        self.confirm_entrada = Entry(self, textvariable=self.confirm, width=25,bd=0,  font=("League Spartan",15),show="*").place(x=45,y=422)

        self.label = Label(self, text = "Already have an account?", fg = "black", bg = "white", font = ('Microsoft YaHei UI Light', 11)).place(x=70, y=520)
        self.button2 = Button(self,text="Sign in", cursor="hand2", bg = "white", border = 0,  fg = "#28847F", font=("League Spartan underline",11), command = self.sign).place(x=264,y=520)
        
        self.button = Button(self,text="Create new Account", bg = "#7CBD7D", width = 45, pady = 7,  relief = "flat", border = 0, font = ("League Spartan",12), command = self.sign_up) .place(x=20,y=465)
    
        
    def sign_up(self):
        self.user = self.username.get()
        self.contra = self.contraseña.get()
        self.e = self.email.get()
        self.c = self.confirm.get()
        
        if self.contra == self.c:
            try:
                messagebox.showinfo("Yey:)", "¡Felicidades! Tu cuenta se ha creado exítosamente.")
                self.file = open("01.txt", "r+")
                self.d = self.file.read()
                self.r=ast.literal_eval(self.d)
                
                self.dict2 = {self.user:self.contra}
                self.r.update(self.dict2)
                self.file.truncate(0)
                self.file.close()
                
                self.file = open("01.txt", "w")
                self.w = self.file.write(str(r))
                
                
                
            except:
                self.file = open("01.txt", "w")
                self.a = str({self.user:self.contra})
                self.file.write(self.a)
                self.file.close()
        else:
            messagebox.showinfo("Oops :(" , "contraseña incorrecta :(, volver a intentar")
                
    def sign(self):
        self.destroy()
                
r = Registro()
r.mainloop()




class Login(Tk):

    
    def __init__(self):
        super().__init__()
        

        self.title("Login")
        self.geometry("1000x600")
        self.resizable(False, False)
        self.bg = PhotoImage(file="PI4.png")
        self.bg1 = Label(self, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        
        self.username = StringVar()
        self.contraseña = StringVar()
        
        self.entrada_username=Entry(self, textvariable=self.username, width=29,bd=0,font=("League Spartan",13)).place(x=70,y=270)
        
        self.entrada_contraseña = Entry(self, textvariable=self.contraseña, width=29,bd=0,font=("League Spartan",15),show="*").place(x=70,y=360)

        self.label = Label(self, text = "Don´t have an account yet?", fg = "black", bg = "white", font = ('Microsoft YaHei UI Light', 11)).place(x=70, y=520)
        self.button2 = Button(self,text="Sign up", cursor="hand2", bg = "white", border = 0, fg = "#28847F", font=("League Spartan underline",11), command = self.sigup).place(x=266,y=521)
        
        self.button = Button(self,text="Ingresar", bg = "#7CBD7D", width = 39,pady = 10,  relief = "flat", border = 0, font = ("League Spartan",12), command = self.signin) .place(x=50,y=435)
        
    def signin(self):
        self.user = self.username.get()
        self.contra = self.contraseña.get()
        
        self.file = open("usuarios.txt", "r+")
        self.d = self.file.read()
        self.r=ast.literal_eval(self.d)
        
        print(self.r.keys())
        print(self.r.values())
        
        
        
        if self.user in self.r.keys() and self.contra == self.r[self.user]:
            self.destroy()
        
        else:
            messagebox.showerror("Oops", "Contraseña y/o usuario incorrectos :(")
    
        

    def sigup(self):
        self.r = Registro()
        self.r.mainloop()

                
l = Login()
l.mainloop()    







class App(Tk):
    def __init__(self):
        super().__init__()

    # Configura la venta Principal
        self.title("Registro")
        self.geometry("950x1000")
        self.resizable(False, False)
        self.bg = PhotoImage(file="M.png")
        self.bg1 = Label(self, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
    


    # Creación de botones
        self.foto = PhotoImage(file = "B4.png")
        self.button = tk.Button(self,  image = self.foto, borderwidth=0, highlightthickness=0, command = self.salir)
        self.button.place(x=40, y=420)
        self.label1 = Label(self, text = "Alegrate", fg = "black", font = ("League Spartan bold", 16)).place(x=780, y=640)
        
        self.foto2 = PhotoImage(file = "11.png")
        self.button2 = tk.Button(self,  image = self.foto2, borderwidth=0, highlightthickness=0, command = self.salir)
        self.button2.place(x=260, y=420)
        self.label2 = Label(self, text = "Regresa", fg = "black", font = ("League Spartan bold", 16)).place(x=550, y=640)
        
        self.foto3 = PhotoImage(file = "B3.png")
        self.button3 = tk.Button(self,  image = self.foto3, borderwidth=0, highlightthickness=0)
        self.button3.place(x=700, y=420)
        self.label3 = Label(self, text = "Relajate", fg = "black", font = ("League Spartan bold", 16)).place(x=303, y=640)
        
        self.foto4 = PhotoImage(file = "B1 (210 × 210 px).png")
        self.button4 = tk.Button(self,  image = self.foto4, borderwidth=0, highlightthickness=0)
        self.button4.place(x=478, y=420)
        self.label4 = Label(self, text = "Duermete", fg = "black", font = ("League Spartan bold", 16)).place(x=100, y=640)
        
        self.button = Button(self,text="Ver estadísticas", bg = "black", fg = "white", width = 25, pady = 7,  relief = "flat", border = 0, font = ("League Spartan",12)) .place(x=500,y=310)
        
    def salir(self):
        self.destroy()

app = App()
app.mainloop()


class Relajate(Tk):
    
    def __init__(self):
        super().__init__()
        self.geometry("850x750")
        self.resizable(False, False)
        self.bg = PhotoImage(file="Relax.png")
        self.bg1 = Label(self, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        self.foto = PhotoImage(file = "Medita.png")
        self.button = tk.Button(self,  image = self.foto, borderwidth=6, highlightthickness=0, command=self.video1)
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
        self.entrada2 = Label(self, textvariable=self.entrada,  bg="white", width=40, pady=220,  bd=0,font=("League Spartan",18)).place(x=150,y=185)
        self.escribir = Entry(self.entrada2, width = 50, border = 0).place(x=150,y=185)
    def gratitud(self):   
        self.geometry("850x750")
        self.resizable(False,False)
        self.bg6 = PhotoImage(file="G.png")
        self.bg7 = Label(self, image=self.bg6).place(x=0, y=0, relwidth=1, relheight=1)
        
    

    
r = Relajate()
r.mainloop()





