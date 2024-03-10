from tkinter import *
from tkinter import ttk
from definicoes import Menu

menu_inicial = Tk()
menu_inicial.title("LuxText")
menu_inicial.resizable(True, True)
menu_inicial.state("zoomed")

largura = 800
altura = 500
menu_inicial.geometry(f"{largura}x{altura}")
menu_inicial.minsize(largura, altura)

menu_inicial.iconbitmap("imgs/Lx.png")
menu_inicial.mainloop()