# List Comprehension

# List comprehension que imprime os números até 10
print([x for x in range(10)])

# List comprehension que imprime os números até 10 e grava em lista em python
listaNum = [x for x in range(10)]
print(listaNum)

# List comprehension que imprime os números menores que 5 em intervalo de 1 a 10
lista_numeros = [x for x in range(10) if x < 5]
print(f'Lista: {lista_numeros}')

# /////////////////////////////////////////////////////////////////////
# Lista de frutas
lista_frutas = ['banana', 'abacate', 'melancia', 'cereja', 'manga']
# Nova Lista
nova_lista = []

# Loop tradicional para buscar as palavras com letra "M"
for x in lista_frutas:
    if 'm' in x:
        nova_lista.append(x)
print('Lista:', nova_lista)

# Mesmo resultado anterior mas com list comprehension
nova_lista = [x for x in lista_frutas if 'm' in x]
print(f'Lista: {nova_lista}')

# /////////////////////////////////////////////////////////////////////
# Dict comprehension
# Dicionario de alunos e notas
dict_alunos = {'Bob':68, 'Michel':84, 'Zico':57, 'Ana':93}

# Criando um novo dicionario imprimindo os pares de chave:valor
dict_alunos_status = {k:v for (k,v) in dict_alunos.items()}
print('Status: %s' %(dict_alunos_status))

# Criando um novo dicionario com o status: nota maior que 70, aprovado, senão, reprovado
dict_alunos_status = {k:('Aprovado' if v > 70 else 'Reprovado') for k, v in dict_alunos.items()}
print(f'Status: {dict_alunos_status}')