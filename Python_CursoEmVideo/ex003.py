n1 = int(input('Informe um numero: '))
n2 = int(input('Informe outro numero: '))
soma = n1 + n2
print(f'A soma de {n1} + {n2} = {soma}')
if (n1 > n2):
    antessor = soma - 1
    print('Antessor de {} é {}'.format(soma, antessor))
else:
    sucessor = soma + 1
    print('Sucessor de {} é {}'.format(soma, sucessor))
