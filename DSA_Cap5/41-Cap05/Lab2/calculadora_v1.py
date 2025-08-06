# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!
print("\n******************* Calculadora em Python *******************")
def soma(num1, num2):
    return num1 + num2
def subtracao(num1, num2):
    return num1 - num2
def multiplacacao(num1, num2):
    return num1 * num2
def divisao(num1, num2):
    return num1 / num2

while True:
    print("\n******************* Calculadora em Python *******************")
    print('\t1 - Soma')
    print('\t2 - Subtração')
    print('\t3 - Multiplicação')
    print('\t4 - Divisão')
    print('\t5 - sair')
    opcao = int(input('Selecione uma opção: ex:(1,2,3,4,5 - sair) '))

    # --/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-//-/-/-/-/
    if opcao == 1:
        x = int(input('Insira o primeiro numero: '))
        y = int(input('Insira o segundo numero: '))
        print(f'Resultado: %d + %d = {soma(x, y)}\n' %(x, y))
    elif opcao == 2:
        x = int(input('Insira o primeiro numero: '))
        y = int(input('Insira o segundo numero: '))
        print(f'Resultado: %d + %d = {subtracao(x, y)}\n' % (x, y))
    elif opcao == 3:
        x = int(input('Insira o primeiro numero: '))
        y = int(input('Insira o segundo numero: '))
        print(f'Resultado: %d + %d = {multiplacacao(x, y)}\n' % (x, y))
    elif opcao == 4:
        x = int(input('Insira o primeiro numero: '))
        y = int(input('Insira o segundo numero: '))
        print(f'Resultado: %d + %d = {divisao(x, y)}\n' % (x, y))
    elif opcao == 5:
        print('Encerrendo a calculadora')
        break
    else:
        print('Opção invalida!')