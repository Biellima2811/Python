lista1 = [10,16,24,39,47]
lista2 = [32,89,47,76,12]
soma = 0

# Lista podem ser concatenadas!
for num in lista1 + lista2:
    if num % 2 == 0:
        soma += num
print('Soma do valores pares: %s' %(soma))

# ---------------------------------------------------
matriz = [[42,23,34],
          [100,215,114],
          [10.1,98.7,12.3]]
maior_numero = 0
# Loop Externo
for linha in matriz:
    #Loop Interno
    for num in linha:
        #Condicional
        if num > maior_numero:
            maior_numero = num
print('Maior número: ', maior_numero)

# ---------------------------------------------------

# Listando as chaves de um dicionario
dict = {'k1': 'Python',
        'k2':'R',
        'k3': 'Scala'}
for item in dict:
    print(item)
# Imprimindo chave e valor do dicionário. Usando o método items() para retornar os itens de um dicionário.
for k, v in dict.items():
    print(k, v)