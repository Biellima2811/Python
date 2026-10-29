"""Crie um program que faça a tabulada de um numero"""
n = int(input('Digite um numero, para ver sua tabuada: '))
for i in range(1, 11):
    resultado = n * i
    print(f"{n} x {i:2} = {resultado}")