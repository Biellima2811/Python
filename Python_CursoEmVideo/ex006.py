import math

print(' ** Dobro, Tiplo, Raiz Quadrada **')
n = int(input("Informe um numero: "))
dobro = n * 2
triplo = n * 3
raizQ = math.sqrt(n)

print("=" * 20, ''
                '\nNumero digitado: {}'
                '\nSeu dobro: {}'
                '\nSeu triplo: {}'
                '\nSua raiz quadrada: {}'.format(n, dobro, triplo, raizQ))