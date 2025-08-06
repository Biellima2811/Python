lista_1 = ["Arroz, Frango, Tomate, Leite"]
#Criação de uma lista como string
print(type(lista_1))
print(lista_1)

# -------------------------------------------

lista_2 = ["Arroz", "Frango", "Tomate", "Leite"]
# Criação de uma lista de strings independentes.
print(type(lista_2))
print(lista_2)

# --------------------------------------------
'''
Crição de outra lista, porem usando o fatiamento. 
cada item, corresponde a um indice. 
'''
lista_3 = [23, 100, 'Cientista de dados']
item1 = lista_3[0]
item2 = lista_3[1]
item3 = lista_3[2]
print(item1,',', item2, ',', item3)


lista_2[2] = 'chocolate'
print(lista_2)

del lista_2[1] # Exclusão de um indice na lista

print(lista_2)
