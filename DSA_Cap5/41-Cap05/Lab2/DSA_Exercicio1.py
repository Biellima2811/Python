# Exercício 1 - Crie uma função que imprima a sequência de números pares entre 1 e 20 (a função não recebe parâmetro)
# e depois faça uma chamada à função para listar os números
def imprimiPar():
    for i in range(1, 21):
        if i % 2 == 0:
            print(i)
imprimiPar()
# -/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/--/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/
# Exercício 2 - Crie uam função que receba uma string como argumento e retorne a mesma string em letras maiúsculas.
# Faça uma chamada à função, passando como parâmetro uma string
def exbirTexto(text):
    return text.upper()
texto = exbirTexto('Gabriel')
print(texto)
# -/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/--/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

# Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e
# imprima a lista
lista_carros = ['Gol', 'Celta', 'Honda', 'Fiat']
# Lista vazia
novos_carros = ['Corola', 'Ranger']
def add_list(lista):
    for carro in novos_carros:
        lista.append(carro)
    print(f'Lista: {lista_carros}')
add_list(lista_carros)

# -/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/--/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/
# Exercício 4 - Crie uma função que receba um argumento formal e uma possível lista de elementos. Faça duas chamadas
# à função, com apenas 1 elemento e na segunda chamada com 4 elementos
def argumentos(agr1, *vartuple):
    # Imprimindo o valor de primeiro argumento.
    print(f'Argumento passado foi: {agr1}')

    cont = 0
    # loop
    # Imprimindo o valor do segundo argumento.
    for i in vartuple:
        cont += 1
        print(f'{cont}° Parâmentro passado foi: {i}')
    return
argumentos(10)
argumentos('Biel', 'Carolina', 'Neném', 'Raj', 'Thomas')

# -/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/--/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/
'''
# Exercício 5 - Crie uma função anônima e atribua seu retorno a uma variável 
chamada soma. A expressão vai receber 2 números como parâmetro e retornar a 
soma deles.
'''
soma = lambda x, y: x + y
result = soma(10,12)
print(result)
'''
# Exercício 6 - Execute o código abaixo e certifique-se que compreende 
a diferença entre variável global e local.
'''
total = 0
def soma(arg1, arg2):
    total = arg1 + arg2;
    print('Dentro da função p total é: %d' %(total))
    return total;

soma(10,20);
print(f'Fora da função o total é: {total}')

'''
# Exercício 7 - Abaixo você encontra uma lista com temperaturas em graus Celsius
- Crie uma função anônima que converta cada temperatura para Fahrenheit
Dica: para conseguir realizar este exercício, você deve criar sua função lambda, dentro de uma função 
(que será estudada no próximo capítulo). Isso permite aplicar sua função a cada elemento da lista
- Como descobrir a fórmula matemática que converte de Celsius para Fahrenheit? Pesquise!!!
'''
Celsius = [39.2, 36.5, 37.3, 37.8]
# Função lambda para converter Celsius para Fahrenheit
Fahrenheit = lambda c: c * (9 / 5) + 32
# Usando map para aplicar a função lambda a cada elemento da lista
Fahrenheit_list = list(map(Fahrenheit, Celsius))
Fahrenheit_list_Format = [f'{temp:.2f}' for temp in Fahrenheit_list]
print (Fahrenheit_list_Format,'°F')

'''
# Exercício 8 - Crie uma list comprehension que imprima 
o quadrado dos números de 1 a 10
'''
quadrado = [x**2 for x in range(1,11)]
print(quadrado)

'''
# Exercício 9 - Crie uma list comprehension que imprima as palavras 
com a letra a no nome
'''
palavras = ["maça", "coiote", "banana", "terreno", "Python"]
nova_lista = [x for x in palavras if 'a' in x]
print(f'Lista: {nova_lista}')

'''
# Exercício 10 - Crie uma list comprehension que imprima os números menores 
que 5 em um intervalo de 1 a 10
'''
lista_numeros = [x for x in range(0,11) if x < 5]
print(f'Lista: {lista_numeros}')