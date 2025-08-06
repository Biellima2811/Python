"""
While e For Juntos
Iremos encontrar número primos em uma coleção de números usando loop While e For Juntos.

Um número primo é um número natural maior do que 1 que é divisivel apenas por 1 e por ele mesmo. Isso significa que não
há nnehum outro número inteiro que possa dividir o núemro primo sem deixa resto. Por exemeplo, o número 2 é primo, pois
é divisivel apenas por 1 e 2. O número 4 não é primo, pois é divisivel por 2.

Pseudocódigo:

Inicialize uma lista vazia para armazena os números primos
para cada número N entre 2 e 30:
    inicialize uma variável eh_primo como verdadeira
    Para cada número i entre 2 e n/2:
        Se N é divisivel por i, então:
            Altere a variável eh_primo para falso
            Pare de verificar os outro números
    Se a variável eh_primo ainda é verdadeira, adcione N à lista de números primos
Imprima a lista de números primos
"""
# Encontrando número primos entre 2 e 30 usando loop for e while

# Variável para armazenar número primos
primos = []

# Loop for para percorrer número de 2 a 30
for num in range(2, 31):
    # Variavel de controle
    eh_primo = True

    # Loop while para verificar se o número é primo
    i = 2
    while i <= num // 2:
        if num % i == 0:
            eh_primo = False
            break
        i += 1

    # Adicionando o número primo na lista
    if eh_primo:
        primos.append(num)

# Imrpimindo a lista de números primos
print(primos)

#Outro exemplo
# Encontrando número primos entre 2 e 30 usando loop for e whiel

# Loop for para percorrer números de 2 a 30
for i in range(2,30):

    # Variável de controle
    j = 2

    # Contador
    valor = 0

    # Loop while para verificar se o número é primo
    while j < i:
        if i % j == 0:
            valor = 1
            j += 1
        else:
            j += 1
    if valor == 0:
        print(str(i) + ' é um número primo.')
        valor = 0
    else:
        valor = 0
