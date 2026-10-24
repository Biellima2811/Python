import tkinter as tk
from tkinter import ttk

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Meu ERP")
        self.geometry("1000x650")
        self.minsize(760, 480)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        ttk.Label(self, text="Bem-vindo ao sistema").grid(row=0, column=0, sticky="nsew")

if __name__== "__main__":
    MainWindow().mainloop()