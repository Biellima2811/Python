import tkinter as tk
from tkinter import ttk, PhotoImage

def Exemplo1():
    # Exemplo 1 - Label Simples
    janela = tk.Tk()
    janela.geometry('300x200')
    janela.title('Uso de labels')

    # Criar um label
    label = tk.Label(janela, text='Aula de Labels')
    label.pack() # Empacotar o label na janela

    # MainLoop
    janela.mainloop()


def Exemplo2():
    # Exemplo 1 - Label Simples
    janela = tk.Tk()
    janela.geometry('300x200')
    janela.title('Uso de labels')
    
    # Mostrar label comum
    label1 = ttk.Label(
        janela,
        text='Texto de label 1',
        font=('Helvetica', 18)
    )
    
    # Posicionamento do label com o empacotamento
    label1.pack(ipadx=10, 
                ipady=30)
    
    label2 = ttk.Label(
        janela,
        text='Texto do Label 2',
        font=('Arial', 20),
        foreground='Orange'
    )
    
    label2.pack(ipadx=10, ipady=60)
    
    janela.mainloop()

def exemplo3():
    def centralizar_imagem(event):
        largura_janela = janela.winfo_width()
        altura_janela = janela.winfo_height()
        largura_imagem = imagem.width()
        altura_imagem = imagem.height()
        
        posicao_x = (largura_janela - largura_imagem) // 2
        posicao_y = (altura_janela - altura_imagem) // 2
        
        lbl_imagem.place(x=posicao_x, y=posicao_y)
        
    
    # Criar janela
    janela = tk.Tk()
    janela.title('Exibir Imagem')
    janela.geometry('400x250')
    
    # Carregar a imagem
    imagem = PhotoImage(file=r'Boson - Tkinter (Curso)\imagem.png')
    
    # Criar label e exibir a imagem
    lbl_imagem = ttk.Label(janela, image=imagem)
    
    # Centralizar imagem ao redimensionar janela
    janela.bind('<Configure>', centralizar_imagem)
    
    lbl_imagem.pack()
    
    # Adicionar label comum
    lbl_biel = ttk.Label(
        janela,
        text='Boson Treinamentos',
        foreground='purple',
        background='lightgreen',
        anchor='center',
        borderwidth=4,
        relief='groove',
    )
    
    lbl_biel.pack(ipadx=20, ipady=20)
        
    # Loop principal
    janela.mainloop()

Exemplo1()