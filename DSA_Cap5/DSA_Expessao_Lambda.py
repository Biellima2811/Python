# Expressão Lambda

# Definindo um função - 3 Linhas de codigo.
def potencia(num):
    resultado = num ** 2
    return resultado
print(potencia(5))

# Defindo uma função - 2 linhas de código.
def potencia(num):
    return num ** 2
print(potencia(5))

# Definindo uma função - 1 linha de código
def potencia(num): return num ** 2
print(potencia(5))

# Definindo um expressão lambda (função anonima)
potencia = lambda num: num ** 2
print(potencia(5))

# Lembrar: operadores de comparção retornam boolean: true or false
Par = lambda x: x % 2 == 0
print(Par(3))
print(Par(2))

frist = lambda s: s[0]
texto = 'Python'
print(frist(texto))

reverso = lambda s: s[::-1]
print(reverso(texto))

addNum = lambda x, y: x + y
soma = addNum(5,95)
print(soma)