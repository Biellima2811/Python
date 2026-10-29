from tkinter import *

menu_inicial = Tk()
menu_inicial.title("Primeiro APP")

# Configuração do tamanho da tela e posicionamento de inicialização.
menu_inicial.geometry("450x350+200+200")

"""Configuração renderização da tela, horizontal e veritical"""
# menu_inicial.resizable(False, True)

"""Configura o maximo da tela"""
# menu_inicial.maxsize(width=800, height=650)
"""Configura o minimo da tela """
# menu_inicial.minsize(500, 250)
"""Inicia com a tela maximizada com tamanho da tela"""
# menu_inicial.state("zoom")

"""Iniciar com a tela minimizada"""
# menu_inicial.state("iconic")
menu_inicial.iconbitmap("Curso_Tkinter/images/favicon.ico")
# Metodo para executa a tela em loop para execução de processo que foram definidos
menu_inicial.mainloop()
