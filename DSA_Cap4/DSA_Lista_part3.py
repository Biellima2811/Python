# Funções Built-in
lista_numeros = [10,20,50,-3.4]
print(len(lista_numeros)) # Ler o tamanho da lista
print(max(lista_numeros)) # Busca o maior valor da lista
# --------------------------------------------------------

# Criando uma lista
lista_formacoes_dsa = ['Analista de Dados',
                       'Cientista de Dados',
                       'Engenheiro de Dados']
print(lista_formacoes_dsa)

# Permite adicionar um elemento a lista existente.
lista_formacoes_dsa.append('Engenheiro de IA')
print(lista_formacoes_dsa)
lista_formacoes_dsa.append('Engenheiro de IA')
print(lista_formacoes_dsa)

# --------------------------------------------------------

# Criação de um lista vazia;
a = []
print(a)
a.append(10)
print(a)
a.append(50)
print(a)

# --------------------------------------------------------

# Loop´s
# Copiando os itens de uma lista para outra.
old_list = [1,2,5,10]
new_list = []

for item in old_list:
    new_list.append(item)
print(new_list)

# --------------------------------------------------------

cidades = ['Recife', 'Manaus', 'Salvador']
print(cidades)
# Extend -> serv para adicionar mais elemente nas lista ja criada.
cidades.extend(['Fortaleza', 'Palmas'])
print(cidades)
print(cidades.index('Fortaleza'))

# Inserir um novo valor de acordo com indice.
cidades.insert(2, 110)
print(cidades)

# Remover o valor inserido na lista.
cidades.remove(110)
print(cidades)

# Metodo para muda a ordem da lista.
cidades.reverse()
print(cidades)

# --------------------------------------------------------
# Ordenar uma lista desordenada.
x = [3,7,4,1,0,9,6]
print(x)
x.sort()
print(x)