import tkinter as tk

janela = tk.Tk()
janela.geometry('500x500')
label1 = tk.Label(janela,
                  text='123456789', 
                  font='Arial 20',
                  bd=1,
                  relief='solid',
                  width=25, height=4,
                  anchor='center').pack()
janela.mainloop()