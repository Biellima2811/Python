from tkinter import *

menu_inicial = Tk()
menu_inicial.title('Titulo')

# Dimensoes da janela 
largura = 500
altura = 300

# Resolução da tela do sistema.
largura_screen = menu_inicial.winfo_screenwidth()
altura_screen = menu_inicial.winfo_screenheight()

# Posição da janela
posx = largura_screen / 2 - largura / 2
posy = altura_screen / 2 - altura / 2

# Definir a geometry 
menu_inicial.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

menu_inicial.mainloop()