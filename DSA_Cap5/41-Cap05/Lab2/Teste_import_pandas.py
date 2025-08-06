import json
import pandas as pd
print(pd.__version__)
arq = r'C:\Users\biell\OneDrive\Documentos\Projetos de Programação\Projetos Python\DSA_Cap5\41-Cap05\Lab2\vimeo.json'
df = pd.read_json(arq)
# Lendo o arquivo JSON com pandas
df = pd.read_json(arq)

# Exibindo as primeiras linhas do DataFrame
print("Primeiras linhas do DataFrame:")
print(df.head()) # mostra as primeiras 5 linhas do DataFrame para uma visualização rápida dos dados.

# Exibindo informações sobre a estrutura do DataFrame
print("\nInformações sobre o DataFrame:")
print(df.info()) # exibe informações sobre a estrutura do DataFrame, incluindo o número de entradas, colunas,
                # tipos de dados e memória usada.

# Exibindo o DataFrame completo (cuidado com arquivos grandes)
print("\nDataFrame completo:")
print(df)


# Iterando sobre cada linha do DataFrame
for index, row in df.iterrows():
    print(f"Índice: {index}")
    print(row)