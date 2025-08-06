dict3 = {'chave1':1230, 'chave2':[22,453,73.4], 'chave3':['picanha', 'fraldinha', 'alcatra']}
print(dict3)
print(dict3['chave2'])
print(dict3['chave3'][0].upper())

var1 = dict3['chave2'][0] - 2
print(var1)

dict3['chave2'][0] -= 2
print(dict3['chave2'])
# ------------------------------------------------------------------
# Criando dicionarios Aninhados
dict_aninhado = {'key1': {'key2_aninhada': {'key3_aninhada':'Dict aninhado em Python'}}}
print(dict_aninhado)
print(dict_aninhado['key1']['key2_aninhada']['key3_aninhada'])