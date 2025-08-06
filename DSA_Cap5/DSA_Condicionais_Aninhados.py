idade = 18
if idade > 17:
    print('Você pode dirigir')

Nome = 'Bob'
if idade > 13:
    if Nome == 'Bob':
        print('Ok Bob, você está autorizado a entrar!')
    else:
        print('Desculpe, mas você não pode entrar!')

# __________________________________________________________

# Operador Logico AND (E)
idade = 13
if idade >= 13 and Nome == 'Bob':
    print('Ok Bob, você está autorizado a entrar!')

# __________________________________________________________

# Operador Logico OR (ou)
idade = 12
if (idade >= 13) or (Nome == 'Bob'):
    print('Ok Bob, você está autorizado a entrar!')