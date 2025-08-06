# Loop FOR

# Criando uma tupla e imprimindo cada um dos valores.
tp = (2,3,4)
for i in tp:
    print(i)
# _________________________________________________________________________

# Criando um lista e imprimindo cada um dos valores
ListaDeStrings = ['Data', 'Science', 'Academy']
for i in ListaDeStrings:
    print(i)
# _________________________________________________________________________

# Imprimindo os valores no intervalor entre 0 e 5 (exclusivo)
for contador in range(0 , 5):
    print(contador) # A contagem será até 4, pois o 5 é exclusivo!
# _________________________________________________________________________

# Imprimindo os número pares da lista de números
lista = [1,2,3,4,5,6,7,8,9,10]
for num in lista:
    if num % 2 == 0:
        print(num)
tp_list = (1,2,3,4,5,6,7,8,9,10)
for i in tp_list:
    if i % 2 == 0:
        print(i)

# Listando os número no intervalo entre 0 e 101, com incremento em 2
for i in  range(0, 101, 2):
    print(i)
# _________________________________________________________________________

# Strings também são sequências
for caracter in 'Python é um liguagem de programação divertida!!':
    print(caracter)