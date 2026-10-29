""" LABEL TEXTVARIABLE E STRINGVAR """
from tkinter import *
menu_inicial = Tk()
menu_inicial.geometry('650x450')
texto = StringVar()
texto.set('Novo texto teste')
label1 = Label(
    font="Arial 20",
    bg='red',
    fg='white',
    textvariable=texto
).pack()

texto.set("Gabriel Pika Grossa")
menu_inicial.mainloop()