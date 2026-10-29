
import tkinter as tk

login = tk.Tk()
login.title('Tela de Login')
login.geometry('300x140')
login.resizable(False, False)

# Rótulo do usuário
lbl_usuario = tk.Label(
    login,
    text='Usuário:',
    font=('Arial', 12)
)
lbl_usuario.grid(row=0, column=0, padx=10, pady=5, sticky='w')

# Campo do usuário
entry_usuario = tk.Entry(login)
entry_usuario.grid(row=0, column=1, padx=10, pady=5)

# Rótulo da senha
lbl_senha = tk.Label(
    login,
    text='Senha:',
    font=('Arial', 12)
)
lbl_senha.grid(row=1, column=0, padx=10, pady=5, sticky='w')

# Campo da senha
entry_senha = tk.Entry(login, show='*')
entry_senha.grid(row=1, column=1, padx=10, pady=5)

# Botão de entrada
btn_entrar = tk.Button(
    login,
    text='Entrar'
)
btn_entrar.grid(row=2, column=1, padx=10, pady=10, sticky='e')

login.mainloop()
