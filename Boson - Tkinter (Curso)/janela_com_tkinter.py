# Janela com tkinter
import tkinter as tk

# janela = tk.Tk()

# janela.title('Janela Principal')

# janela.geometry('500x400+200+100') # Configuração do tamanho da janela com espaçamentos 

# janela.config(bg='lightblue') # Configurações de cores no fundo.

# janela.maxsize(800,600) # Tamnho maximo da janela

# janela.minsize(200,200) # Tamnho minimo da janela

# janela.resizable(False, False) # Esse metoro define se a janela pode ser ou não redimencionanda, na vertical ou horizontal 

# janela.state('zoomed') # Incia a janala com tela cheia

# janela.attributes('-alpha', 0.6) # Deixa a janela transparete

# janela.iconbitmap('Boson - Tkinter (Curso)\glicon.ico')

def abrir_segunda_janela():
    segunda_janela = tk.Toplevel()
    segunda_janela.title('Segunda Janela')
    segunda_janela.config(bg='#20EE70')
    
    # Tamanho da janela
    largura_janela = 300
    altura_janela = 200
    
    # Obter as dimensões da tela do monitor
    largura_tela = segunda_janela.winfo_screenmmwidth()
    altura_janela = segunda_janela.winfo_screenmmwidth()
    
    # Calcular as coordenada par centralizar a janela 2
    x = (largura_janela - largura_tela) // 2
    y = (altura_janela - altura_janela) // 2
    
    # Definir a geometria da janela 2
    segunda_janela.geometry(f'{largura_janela}x{altura_janela}+{x}+{y}')
    

def Janela_principal():
    # Cria janela principal
    janela_principal = tk.Tk()
    janela_principal.title('Janela Principal')
    janela_principal.geometry('600x500')

    # Metodo BIND, quando clica no botão esquerdo do mouse, ele vai gera o evento, vai executar em abri a segunda janela. 
    janela_principal.bind('<Button-1>', lambda event: abrir_segunda_janela()) 

    # Main lopp
    janela_principal.mainloop()

Janela_principal()