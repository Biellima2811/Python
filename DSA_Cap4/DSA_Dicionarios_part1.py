'''
# Isso é um dicionario
# Para identificar colocamos {} '': e um valor

estudantes_disct = {'Pedro':24, 'Ana':22, 'Ronaldo':26, 'Janaina':25}
print(type(estudantes_disct))
print(estudantes_disct)
print(estudantes_disct["Pedro"])
# No dicionario não exites a chave 'Marcelo' com o comando abaixo,
# será adicionado ao dicionario
estudantes_disct['Marcelo'] = 23
print(estudantes_disct['Marcelo'])
print(estudantes_disct)

# ----------------------------------------------
# Caso desejar limpar o dicionario, usar o metodo clear
estudantes_disct.clear()
print(estudantes_disct)

# ----------------------------------------------
# Delete o dicionario
del estudantes_disct
print(estudantes_disct)

'''
# ----------------------------------------------
estudantes = {'Pedro':24, 'Ana':22, 'Ronaldo':26, 'Janaina':25}
print(len(estudantes))
print(estudantes.keys()) # Retornas as chaves
print(estudantes.values()) # Retorna os valores
print(estudantes.items()) # Retorna os itens (Dicionario completo)

# ----------------------------------------------

# Atualização de um dicionario com outro.
estudantes2 = {'Camila':27, 'Adriana':28, 'Roberta':26}
print(estudantes2)

print('Antes: \n', estudantes)
# Usando metodo UPDATE
estudantes.update(estudantes2)
print('Depois: \n', estudantes)


# ----------------------------------------------
# Criando o dicionario vazio e adcionando valores
dic1 = {}
dic1['Chave_um'] = 2
print(dic1)

dic1[10] = 5
print(dic1)

dic1[9.13] = 'Python'
print(dic1)

# ----------------------------------------------
# Fatiamento de um dicionario

dist2 = {} # Dicionario vazio!

dist2['Key1'] = 'Data Sciente'
dist2['Key2'] = 10
dist2['Key3'] = 100
print(dist2)

# Atribuição a variavel com fatiamento do dicionario.

a = dist2['Key1']
b = dist2['Key2']
c = dist2['Key3']
print(a, b, c)