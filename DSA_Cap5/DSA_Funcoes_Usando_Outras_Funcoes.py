from math import sqrt
def numPrimo(num): # Verificando se um número é primo.
    if (num % 2) == 0 and num > 2:
        return 'Este número não é primo.'
    for i in range(3, int(sqrt(num)) + 1,2):
        if (num % i) == 0:
            return 'Este número não é primo.'
    return 'Este número é primo.'

print(numPrimo(13))

caixa_baixa = 'Este Texto Deveria Esta Todo Em LowerCase'

def lowercase(text):
    return text.lower()

lowercaded_string = lowercase(caixa_baixa)
print(lowercaded_string)