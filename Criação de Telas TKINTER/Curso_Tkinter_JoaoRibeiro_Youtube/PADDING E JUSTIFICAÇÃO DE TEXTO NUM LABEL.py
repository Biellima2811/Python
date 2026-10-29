from tkinter import *
menu_inicial = Tk()
menu_inicial.title('Titulo')
menu_inicial.geometry('500x500')
label1 = Label(
    menu_inicial,
    text='Frase de teste',
    font='Arial 20',
    bd=1, 
    relief='solid',
    width=30, height=5,
    justify=LEFT, anchor='sw'
).pack()

label2 = Label(
    menu_inicial,
    text='Frase de teste 2, \nteste de Frase, \ntestezeira',
    font='Arial 20',
    bd=1, 
    relief='solid',
    padx=50, pady=50,
    justify=RIGHT
).pack()

menu_inicial.mainloop()