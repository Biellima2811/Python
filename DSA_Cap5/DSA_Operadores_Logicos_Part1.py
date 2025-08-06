idade = 18
nome = 'Bob'
if idade > 17:
    print('Você pode dirigir!')

idade = 18
if idade > 17 and nome == 'Bob':
    print('Autorizado!')

'''

# Operador and - Retorna TRUE se ambas as declarações forem verdadeiras
# Operador OR - Retorna TRUE se uma das declarações for verdadeiras
# Operador NOT - Inverte o resultado, retorna FALSE se o resultado for TRUE.

'''

# *** Operador AND ***
numero = 4
if (numero > 2) and (numero % 2 == 0):
    print('Isso está sendo impresso porque uma das duas condições são verdadeiras')
else:
    print('Isso está sendo impresso poruqe uma das duas condições é falsa.')

numero_1 = 7
if (numero_1 > 5) and (numero_1 % 2 == 0):
    print('Isso está sendo impresso porque uma das duas condições são verdadeiras')
#_________________________________________________________________________________

# *** Operador OR ***
if (numero > 5) or (numero % 2 == 0):
    print('Isso está sendo impresso porque uma das duas condições são verdadeiras')
#_________________________________________________________________________________

# *** Operador NOT ***
if not (numero > 5) and (numero % 2 == 0):
    print('Isso está sendo impresso porque uma das duas condições são verdadeiras')
else:
    print('Isso está sendo impresso poruqe uma das duas condições é falsa.')
#_________________________________________________________________________________

# Operador and, or e not
if (not (numero > 5) and (numero % 2 == 0)) or (numero == 4):
    print('Isso está sendo impresso porque uma das duas condições são verdadeiras ou a terceira é verdadeira! ')
#_________________________________________________________________________________
