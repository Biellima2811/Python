# Loop While
'''
# Usando o loop while para imprimir os valores de 0 a 9
# A condição tem que deixar de ser verdadeira dentro do loop,
senão pode travar ou mesmo o computador.
'''
valor = 0
while valor < 10:
    print(valor)
    valor += 1

# Entra no loop somente se a condição for verdadeira
valor = 11
while valor < 10:
    print(valor)
    valor += 1

# Também é possivel usar a claúsula else para encerra o loop while
x = 0
while x < 10:
    print('O valor de x é iteração é: %x' %(x))
    print('x ainda é menor que 10, somando 1 a x')
    x += 1
else:
    print('Loop concluido!')
print(x)
print('\n ----')

'''
Pode ser usando dentro while: Pass, Break, Continue
'''
# Exemplos
# Se encontramos o número 4 interrompemos o loop
valor = 0
while valor < 10:
    if valor == 4:
        break
    else:
        pass
    valor += 1
    print(valor)

# Desconsideramos a letra z ao imprimir os caracteres da frase.
for letra in 'Python é zzz incrivel!':
    if letra == 'z':
        continue
    print(letra)