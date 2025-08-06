# Fazendo Split dos Dados.
def split_strings_palvras(text):
    return text.split(' ')
texto = 'Esta função será bastante útil para separar grandes volumes de dados.'

# Isso divide a string em uma lista de palavras
print(split_strings_palvras(texto))

# Podemos atribuir o output de uma função para uma variavel.
token = split_strings_palvras(texto)

print(token)

# Fazendo split dos dados.
def split_strings_letras(text):
    texto = text.upper()
    for letra in texto:
        print(letra)
split_strings_letras(texto)