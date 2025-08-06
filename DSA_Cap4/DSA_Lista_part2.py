# Lista de lista ou Aninhadas
listas = [[1,2,3], [10,15,14], [10.1, 8.7, 2.3]]
print(listas)

# a = listas[0] # Indicando a variavel 'a' como indice 0 da lista
# print(a) # Exibe a primeira lista dento das listas

# b = a[0]
# print(b) # Exibe o primeiro indice da primeira lista dentro das listas.

# Fatiamento das lista
lista_1 = listas[1] # Criação da variavel para busca o indice 1 das listas
lista_1_0 = lista_1[0] # Criação de outra para variavel para buscar o indice 0 da lista com indice 1
print(lista_1_0) # Exibição do resultado.


lista_2 = listas[2]
lista_2_0 = lista_2[0]
print(lista_2_0)
# ------------------------------------------------

# Atribuindo à variavel ao primeiro valor da lsita
a = listas[0][0]
print(a)

b = listas[1][2]
print(b)

# ------------------------------------------------

# Operações Aritimentica dentro de listas.
c = listas[0][2] + 10
print(c)

d = 10
e = d * listas[2][0]
print(e)

# ------------------------------------------------

# Concatenando Listas
lista_s1 = [34,22,56]
lista_s2 = [21,90,51]
lista_total = lista_s1 + lista_s2
# Exibe a junção de ambas as listas. (Sobrecaraga do operador +)
print(lista_total)

# ------------------------------------------------

# Operador IN

# Criando uma lista
lista_teste_op = [100,2,-5,3.4]

# Retorna um valor logico de acordo com a lista

# Verificando se o valor 10 pertence a lista
print(10 in lista_teste_op)

# Verificando se o valor 100 pertence a lista
print(100 in lista_teste_op)

# ------------------------------------------------


