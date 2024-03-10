from tkinter import *
from tkinter import ttk
from tkinter.ttk import * 


class Menu_:
    def __init__(self, window):
        self.window = window
        self
    def Sobre(self):
       sobre = Toplevel(self.window)
       sobre.title("Sobre")
       sobre.geometry("800x500")
       sobre_texto1 = Label(sobre, text="Bem vindo ao LuxText, seu editor de texto pensado para você!")
       sobre_texto2 = Label(sobre, text="Implementado utilizando o Tkinter e python, versão beta 1.0")
       sobre_texto1.pack(padx=10, pady=10,anchor="center")
       sobre_texto2.pack(padx=10, pady=10,anchor="center")
       sobre.mainloop()