import tkinter as tk
from tkinter import ttk
import Funcao_Conf_Imagem # Importa o módulo com as funções

janela = tk.Tk()
janela.title('Exibir Imagem')
janela.geometry('400x250')

# Cria label para imagem
lbl_imagem = tk.Label(janela)
lbl_imagem.place(x=0, y=0)  # Inicia com place (não use pack aqui)

# Carrega a imagem (com referência global)
imagem = Funcao_Conf_Imagem.carregar_imagem()
lbl_imagem.configure(image=imagem)

# Passa a imagem como parâmetro para evitar recarregar
janela.bind(
    '<Configure>',
    lambda e: Funcao_Conf_Imagem.centralizar_imagem(e, janela, lbl_imagem, imagem)
)

# Label de texto
lbl_biel = ttk.Label(
    janela,
    text='GL Systems and Solutions IT',
    foreground='purple',
    background='lightgreen',
    anchor='center',
    borderwidth=3,
    relief='groove'
)
lbl_biel.pack(ipadx=20, ipady=20)

# Garante que o texto fique acima da imagem, se necessário
lbl_biel.lift()

janela.mainloop()
