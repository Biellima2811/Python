from tkinter import PhotoImage
import os

def carregar_imagem():
    # Caminho absoluto para garantir que a imagem seja encontrada
    caminho_imagem = os.path.join(
        os.path.dirname(__file__),
        'Boson - Tkinter (Curso)',
        'imagem.png'
    )
    
    # Mantém uma referência global da imagem
    global imagem
    imagem = PhotoImage(file=caminho_imagem)
    return imagem

def centralizar_imagem(event, janela, lbl_imagem, imagem):
    # Obtém dimensões da janela
    largura_janela = janela.winfo_width()
    altura_janela = janela.winfo_height()
    
    # Usa a imagem passada como parâmetro
    largura_imagem = imagem.width()
    altura_imagem = imagem.height()
    
    # Centraliza
    posicao_x = (largura_janela - largura_imagem) // 2
    posicao_y = (altura_janela - altura_imagem) // 2
    
    lbl_imagem.place(x=posicao_x, y=posicao_y)
