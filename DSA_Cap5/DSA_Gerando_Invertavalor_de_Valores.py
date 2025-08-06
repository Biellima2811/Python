# Função Range
# Exemplos.

# Imprimindo números de 1 a 10
for i in range(1,11):
    print(i)

# Imprimindo números pares entre 50 a 100
for i in range(50,101,2):
    print(i)

# Imprimindo os números pares negativos entre 0 a -20
for i in range(0, -20, -2):
    print(i)

# Usando o taminho de uma lista na função range()
lista = ['Abacaxi', 'Banana', 'Morango', 'Uva']
lista_tamanho = len(lista)
for i in range(0, lista_tamanho):
    print(lista[i])