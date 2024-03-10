from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

class Menu_:
    def __init__(self, window, i, tab = []):
        self.i = i
        self.tab = tab = []
        self.window = window
        self.area_texto = ttk.Notebook(self.window)
        self.area_texto.pack(padx=10,pady=10)
        self.width = window.winfo_screenwidth()
        self.height = window.winfo_screenheight()
    def Sobre(self):
       sobre = Toplevel(self.window)
       sobre.title("Sobre")
       sobre.geometry("800x500")
       sobre_texto1 = Label(sobre, text="Bem vindo ao LuxText, seu editor de texto pensado para você!")
       sobre_texto2 = Label(sobre, text="Implementado utilizando o Tkinter e python, versão beta 1.0")
       sobre_texto1.pack(padx=10, pady=10,anchor="center")
       sobre_texto2.pack(padx=10, pady=10,anchor="center")
       sobre.mainloop()

    def Novo_arquivo(self):
        self.i = self.i + 1
        self.tab.append(self.i-1)
        self.tab[self.i-1] = Frame(self.area_texto, width=self.width, height=self.height)
        self.tab[self.i-1].pack(fill="both", expand=1)
        self.area_texto.add(self.tab[self.i-1], text=f"Não salvo {self.i-1}")
        entrada = Text(self.tab[self.i-1], width=self.width,height=self.height)
        entrada.pack()
