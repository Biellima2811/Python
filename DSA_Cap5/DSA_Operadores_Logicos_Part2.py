# Exemplo com o uso de variáveis

disciplina = 'Data Science'
nota_final = 70
if disciplina == 'Data Science' and nota_final >= 70:
    print('Você foi aprovado!')
else:
    print('Lamento, acho que você precisa estudar mais!')

# Usando mais de uma condição na clásula if

nota_final = 60
if disciplina == 'Data Science' and nota_final >= 70:
    print('Você foi aprovado!')
else:
    print('Lamento, acho que você precisa estudar mais!')

# Usando mais de uma condição na clásula IF e introduzindo Place (Guardador de lugar)
disciplina = 'Data Science'
nota_final = 90
semestre = 2
if disciplina == 'Data Science' and nota_final >= 80 and semestre != 1:
    print('Você for aprovado em %s com média final %r!' %(disciplina, nota_final))
else:
    print('Lamento, acho que você precisa estudar mais!')