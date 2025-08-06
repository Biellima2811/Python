# Criando uma tupla
tupla1 = ('Geografia', 23, 'Elefantes', 9.8, 'Python')
print(tupla1)

'''
# obs:  Tuplas não suportam append()
tupla1.append('Chocolate')

# obs:  Tuplas não suportam del
del tupla1['Elefantes']

Tuplas são imultaveis, caso deseja altera algo converta para uma lista!
'''
print(tupla1[0])
print(len(tupla1))

t2 = ('A', 'B', 'C')
print(f'Tupla: {t2}')
# Conversão de tupla para lista
lista_t2 = list(t2)
print(f'Lista: {lista_t2}')
lista_t2.append('D')
print(lista_t2)

# Conversão de lista para tupla
t2 = tuple(lista_t2)
print(t2)



