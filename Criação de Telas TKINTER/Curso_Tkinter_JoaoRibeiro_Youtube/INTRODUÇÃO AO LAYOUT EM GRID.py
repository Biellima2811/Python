from tkinter import *

menu_inicial = Tk()
#menu_inicial.geometry('600x300')

label_1 = Label(menu_inicial, 
                text='Label 1', 
                font='Arial 15', 
                bg='red').grid(row=0, column=0)

label_2 = Label(menu_inicial, 
                text='Label 2', 
                font='Arial 15', 
                bg='green').grid(row=0, column=1)

label_2 = Label(menu_inicial, 
                text='Label 3', 
                font='Arial 15', 
                bg='blue').grid(row=0, column=2)

btn1 = Button(menu_inicial, text='Click aqui!').grid(row=1, column=0)
btn1 = Button(menu_inicial, text='Click aqui!').grid(row=1, column=1)
btn1 = Button(menu_inicial, text='Click aqui!').grid(row=1, column=2)

menu_inicial.mainloop()