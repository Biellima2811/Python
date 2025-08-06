import tkinter as tk

# instanciar janela
janela = tk.Tk()
janela.title('Primiero APP')
janela.geometry('300x300') 

# Criar e posicionar um label com a mensagem
lblmsg = tk.Label(janela, text='Ola pessoal')
lblmsg.pack()

# Exibir a janela
janela.mainloop()