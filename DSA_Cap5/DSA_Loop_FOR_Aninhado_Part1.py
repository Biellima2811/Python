# Loop FOR Aninhado

lista1 = [0,1,2,3,4]
lista2 = [1,2,3]
# Loop Externo
for elemento_lista1 in lista1:
    # Loop interno
    for elemento_lista2 in lista2:
        print('\n',elemento_lista1 * elemento_lista2)
    print('---')

# o número 47 aparece nas duas listas?
lista1 = [10,16,24,39,47]
lista2 = [32,89,47,76,12]

# Loop externo
for elemento_lista1 in lista1:

    #Loop Interno
    for elemento_lista2 in lista2:

        # Condicional
        if elemento_lista1 == 47 and elemento_lista2 == 47:
            print('O numero %i foi encontrado em ambas as listas! ' %(elemento_lista1))


# Some os números pares da primeira lista  com os números pares  da segunda lista.

lista1 = [10,16,24,39,47]
lista2 = [32,89,47,76,12]
soma = 0
# Loop Externo
for lista in [lista1, lista2]:

    # Loop Interno
    for num in lista:

        # Condicional
        if num % 2 == 0:
            soma += num
print(f'A soma dos números pares das duas listas é igual a {soma}')