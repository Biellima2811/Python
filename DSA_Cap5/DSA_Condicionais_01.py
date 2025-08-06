# Condicionais IF (se)

if 5 > 2:
    print('A senteça é verdadeira!')

# _____________________________________________

# Condional If...Else

if 5 < 2:
    print('A senteça é verdadeira!')
else:
    print('A sentença é falsa.')

# _____________________________________________

# Condicional If...Else com variável

dia = 'Terça'
if dia == 'Segunda':
    print('Hoje fará sol!')
else:
    print('Hoje vai chover!')

# _____________________________________________

# Podemos usar o operado elfi para validar mais de um condição

if dia == 'Segunda':
    print('Hoje fará sol!')
elif dia == 'Terça':
    print('Hoje vai chover!')
else:
    print('Sem previsão do tempo para o dia selecionado.')