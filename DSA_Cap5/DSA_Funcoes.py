# Funções

print('Hello World')

# Definindo uma função
def primeiraFunc():
    print('Hello World')

primeiraFunc()

# Definindo um função
def primeiraFunc():
    nome = 'Bob'
    print('Hello %s' %(nome))
primeiraFunc()
# ___________________________________________

# Definindo uma função com parêmetro
def segundaFunc(nome):
    print('Hello %s' %(nome))

segundaFunc('Aluno')
# ___________________________________________

# Função para imprimir numeros
def imprimeNumeros():

    # Loop
    for i in range(0,5):
        print('Numero ' + str(i))
imprimeNumeros()

# ___________________________________________
# Função para somar números
def addNum(fristnum, secundnum):
    print('Primeiro número: %i' %(fristnum))
    print('Segundo número: %o' %(secundnum))
    print('Soma: ', fristnum + secundnum)

addNum(4,6) #Chamada da função e passando parâmetros
addNum(45,9)
# ___________________________________________

# Função com número variavel de argumentos
def printVarInfo(arg1, *vartuple):
    # Imprimindo o valor de primeiro argumento.
    print(f'O parâmentro passado foi: {arg1}')

    # Imprimindo o valor do segundo argumento.
    for item in vartuple:
        print(f'O parâmentro passo foi: {item}')
    return;
printVarInfo(10) # Fazendo a chamada á função usando apenas 1 argumento.
printVarInfo('Chocolate', 'Morango')
printVarInfo('Data', 'Science', 'Academy')

