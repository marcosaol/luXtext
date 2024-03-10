from tkinter import *
from tkinter import ttk

class Menu:
    def __init__(self,nome_arquivo = "Não salvo", texto_sobre = ""):
        self.nome_arquivo = nome_arquivo
        self.texto_sobre = texto_sobre

    def arquivo(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo

    def Sobre(self, texto_sobre):
        texto_sobre = "Bem vindo ao LuxText um editor de texto feito com pyhton pensado para você"
        self.texto_sobre = texto_sobre