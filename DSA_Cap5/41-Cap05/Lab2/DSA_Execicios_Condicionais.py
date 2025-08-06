'''
Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a Domingo ou
 igual a sábado, imprima na tela "Hoje é dia de descanso", caso contrário imprima na tela "Você precisa trabalhar!"
'''
def tempo(dia):
    texto = dia.upper()
    if texto == 'SABADO' or texto == 'DOMINGO':
        return 'Hoje é dia de descanso.'
    else:
        return 'Você precisa trabalhar'
#dia_senama = tempo(input('Informe o dia: '))
#print(dia_senama)
# */*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
'''
Exercício 2 - Crie uma lista de 5 frutas e verifique se a fruta 'Morango' faz parte da lista
'''
lista_Frutas = ['Manga', 'Tomate', 'Banana', 'Abacate', 'Maça']
if 'Morango' in lista_Frutas:
    print('Morango faz parte da lista')
else:
    print('Morango não faz parte da lista')
# */*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
'''
# Exercício 3 - Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e 
guarde os resultados em uma lista
'''
# Criando a tupla de 4 elementos
tp_1 = (1,2,3,4)
# Criando a tupla de 4 elementos
list_tp1 = [x * 2 for x in tp_1]
print('Tupla multiplicado por 2:', list_tp1)
# */*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
'''
# Exercício 4 - Crie uma sequência de números pares entre 100 e 150 e imprima na tela
'''
for i in range(100, 152, 2):
    print(i)
'''
# Exercício 5 - Crie uma variável chamada temperatura e atribua o valor 40. 
Enquanto temperatura for maior que 35, imprima as temperaturas na tela.
'''
temperatura = 40
while temperatura > 35:
    print(f'Temperatura: %d°' %(temperatura))
    temperatura -= 1 # Decrementa a temperatura em 1 a cada iteração
# */*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
'''
# Exercício 6 - Crie uma variável chamada contador = 0. 
Enquanto counter for menor que 100, imprima os valores na tela, 
mas quando for encontrado o valor 23, interrompa a execução do programa.
'''
contador = 0
while contador < 100:
    if contador == 23:
        break
    print(contador)
    contador += 1
# */*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
'''
Exercício 7 - Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da variável for menor ou igual a 20, 
adicione à lista, apenas os valores pares e imprima a lista
'''
num = 4
lista_vazia = []
while num <= 20:
    if num % 2 == 0:
        lista_vazia.append(num)
    num += 1
print(lista_vazia)
# */*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
'''
Exercício 8 - Transforme o resultado desta função range em uma lista: range(5, 45, 2)
'''
# Criando um objeto range de 5 a 45 com passo 2
nums = range(5, 45, 2)
# Convertendo o objeto range em uma lista
convert_lista = list(nums)
# Imprimindo a lista convertida
print(convert_lista)
# */*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
'''
# Exercício 9 - Faça a correção dos erros no código abaixo e execute o programa. Dica: são 3 erros.
'''
temperatura = float(input('Qual a temperatura? '))
if temperatura > 30:
    print('Vista roupas leves.')
else:
    print('Busque seus casacos.')
# */*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
'''
Exercício 10 - Faça um programa que conte quantas vezes a letra "r" aparece na frase abaixo. 
Use um placeholder na sua instrução de impressão
“A gratidão é a virtude das almas nobres. O quão feliz é uma pessoa depende da profundidade de sua gratidão.” 
'''
frase = "A gratidão é a virtude das almas nobres. O quão feliz é uma pessoa depende da profundidade de sua gratidão."
qtde_r = frase.count('r') # Contado quantas vezes a letra 'r' aparece.
print('A letra "r" aparece %d vezes na frase' %(qtde_r))
