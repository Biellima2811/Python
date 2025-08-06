# Variavel global
var_global = 10 #Esta é uma variavel global

# Função
def multiplica_numeros(num1, num2):
    var_global = num1 * num2
    print(var_global)

print(var_global)
multiplica_numeros(10,30)

multiplica_numeros(5,25)
print(var_global)