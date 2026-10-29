print('** Calculadora de Media **')
nota1 = float(input('Informe a 1° nota: '))
nota2 = float(input('Informe a 2° nota: '))
soma = nota1 + nota2
media = soma / 2
if (media >= 6):
    print("Aprovado!!" \
    "\nA soma de {} e {}, total da nota: {}, media: {:.2f}".format(nota1, nota2, soma, media))
else:
    print("Reprovado!, Tente novamente..." \
    "\nA soma de {} e {}, total da nota: {}, media: {:.2f}".format(nota1, nota2, soma, media))