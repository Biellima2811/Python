from tkinter import *

menu_incial = Tk()
menu_incial.title("Titulo")
menu_incial.geometry("450x300+200+200")
menu_incial['bg'] = 'blue'
# botao
btn = Button(menu_incial, text="Botão de teste", bg="black", fg="white").grid(row= 6, column=2, columnspan=3, padx=1.5, pady=4.5)

menu_incial.mainloop()