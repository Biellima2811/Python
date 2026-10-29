"""Crie um programa que leia quanto dinhiero uma pessoa tem na carteira 
e mostre quantos Dolares ela pode comparar"""

print("*** Conversor de Moedas - US$ | R$ ***")
print("1 - Moeda Estrangeira para moeda Local"
      "\n2 - Moeda Local para moeda Estrangeira")
opcao = int(input("Escolha uma opçao acima: "))
Dolar = 5.35
if (opcao == 1):
    carteira = float(input("Quanto tem na carteira: R$"))
    valor_final = Dolar * carteira
    print(f"Com valor informado na carteira de ${carteira:.2f} Dolares, pode comprar $ {valor_final:.2f} Reais. ")
else:
    carteira = float(input("Quanto tem na carteira: R$"))
    valor_final = carteira / Dolar
    print(f"Com valor informado na carteira de R${carteira:.2f} reais, pode comprar $ {valor_final:.2f} Dolares. ")