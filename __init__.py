from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from definicoes import Menu_

root = Tk()

menu_ = Menu_(window = root, i = 0)

root.title("LuxText")
root.resizable(True, True)
root.state("zoomed")

largura = 800
altura = 500
root.geometry(f"{largura}x{altura}")
root.minsize(largura, altura)

 
menubar = Menu(root) 


arquivo = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Arquivo', menu = arquivo) 
arquivo.add_command(label ='Novo arquivo', command = menu_.Novo_arquivo) 
arquivo.add_command(label ='Abrir', command = None) 
arquivo.add_command(label ='Salvar', command = None) 
arquivo.add_separator() 
arquivo.add_command(label ='Fechar', command = menu_.Fechar)
arquivo.add_command(label ='Sair', command = root.destroy) 
  
 
editar = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Editar', menu = editar) 
editar.add_command(label ='Recortar', command = None) 
editar.add_command(label ='Copiar', command = None) 
editar.add_command(label ='Colar', command = None) 
editar.add_command(label ='Selecionar tudo', command = None) 
editar.add_separator() 
editar.add_command(label ='Achar', command = None) 

configuracao = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Configuração', menu = configuracao) 
configuracao.add_command(label ='Ajuda', command = None) 
configuracao.add_command(label ='Sobre', command = menu_.Sobre) 
configuracao.add_separator() 
configuracao.add_command(label ='Preferências', command = None) 
  
root.config(menu = menubar) 

root.mainloop()