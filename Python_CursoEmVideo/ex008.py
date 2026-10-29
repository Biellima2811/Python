"""Escreva um programa que leita um valor em metros e o exiba convertido em
centímetros e milimetros"""
print('Conversor de Medidas')
cursor = int(input('Informe um valor em metros: '))
centimetro = cursor * 100
milimetros = cursor * 1000
quilometro = cursor / 1000
hectometro = cursor / 100
decametro = cursor / 10
decimetro = cursor * 10
print(f"Valor inserido: {cursor} \n", \
      "=" * 20, "\nValores Convertidos\n", "=" * 20,
      "\nCentimetro: {} cm" \
      "\nMilimetro: {} mm" \
      "\nQuilômetro: {} km" \
      "\nHectômetro: {} hm" \
      "\nDecâmetro: {} dam" \
      "\nDecímetro: {} dm"
      .format(centimetro,
              milimetros,
              quilometro,
              hectometro, 
              decametro, decimetro))