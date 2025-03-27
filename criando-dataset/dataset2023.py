import pandas as pd
import numpy as np

# Escolho a Soja
# Cresce mais rápido na estação: Primavera / Verão

# 20 amostras por mes

verao2023 = pd.DataFrame([
    #ano  mes estacao  crescimento
    #Janeiro 2023
    [2023, 1, 'Verão',      52],
    [2023, 1, 'Verão',      54],
    [2023, 1, 'Verão',      55],
    [2023, 1, 'Verão',      56],
    [2023, 1, 'Verão',      57],
    [2023, 1, 'Verão',      60],
    [2023, 1, 'Verão',      61],
    [2023, 1, 'Verão',      63],
    [2023, 1, 'Verão',      63],
    [2023, 1, 'Verão',      63],
    [2023, 1, 'Verão',      63],
    [2023, 1, 'Verão',      63],
    [2023, 1, 'Verão',      63],
    [2023, 1, 'Verão',      63],
    [2023, 1, 'Verão',      63],
    [2023, 1, 'Verão',      63],
    [2023, 1, 'Verão',      63],
    [2023, 1, 'Verão',      63],
    [2023, 1, 'Verão',      64],
    [2023, 1, 'Verão',      64],
    #Fevereiro 2023
    [2023, 2, 'Verão',      64],
    [2023, 2, 'Verão',      64],
    [2023, 2, 'Verão',      64],
    [2023, 2, 'Verão',      64],
    [2023, 2, 'Verão',      64],
    [2023, 2, 'Verão',      64],
    [2023, 2, 'Verão',      64],
    [2023, 2, 'Verão',      68],
    [2023, 2, 'Verão',      68],
    [2023, 2, 'Verão',      68],
    [2023, 2, 'Verão',      68],
    [2023, 2, 'Verão',      68],
    [2023, 2, 'Verão',      68],
    [2023, 2, 'Verão',      68],
    [2023, 2, 'Verão',      68],
    [2023, 2, 'Verão',      68],
    [2023, 2, 'Verão',      68],
    [2023, 2, 'Verão',      68],
    [2023, 2, 'Verão',      68],
    [2023, 2, 'Verão',      70],
    #Março 2023
    [2023, 3, 'Verão',      70],
    [2023, 3, 'Verão',      70],
    [2023, 3, 'Verão',      70],
    [2023, 3, 'Verão',      70],
    [2023, 3, 'Verão',      70],
    [2023, 3, 'Verão',      70],
    [2023, 3, 'Verão',      70],
    [2023, 3, 'Verão',      70],
    [2023, 3, 'Verão',      70],
    [2023, 3, 'Verão',      70],
    [2023, 3, 'Verão',      70],
    [2023, 3, 'Verão',      70],
    [2023, 3, 'Verão',      70],
    [2023, 3, 'Verão',      70],
    [2023, 3, 'Verão',      70],
    [2023, 3, 'Verão',      70],
    [2023, 3, 'Verão',      70],
    [2023, 3, 'Verão',      70],
    [2023, 3, 'Verão',      70],
    [2023, 3, 'Verão',      70]


], columns=['Ano', 'Mes', 'Estacao', 'Crescimento']);


outono2023 = pd.DataFrame([
    #ano  mes estacao  crescimento
    # Março 2023
    [2023, 3, 'Outono',      75],
    [2023, 3, 'Outono',      75],
    [2023, 3, 'Outono',      75],
    [2023, 3, 'Outono',      75],
    [2023, 3, 'Outono',      75],
    [2023, 3, 'Outono',      75],
    [2023, 3, 'Outono',      75],
    [2023, 3, 'Outono',      78],
    [2023, 3, 'Outono',      78],
    [2023, 3, 'Outono',      78],
    [2023, 3, 'Outono',      78],
    [2023, 3, 'Outono',      78],
    [2023, 3, 'Outono',      80],
    [2023, 3, 'Outono',      80],
    [2023, 3, 'Outono',      80],
    [2023, 3, 'Outono',      80],
    [2023, 3, 'Outono',      80],
    [2023, 3, 'Outono',      80],
    [2023, 3, 'Outono',      80],
    [2023, 3, 'Outono',      80],
    # Abril 2023
    [2023, 4, 'Outono',      82],
    [2023, 4, 'Outono',      83],
    [2023, 4, 'Outono',      84],
    [2023, 4, 'Outono',      85],
    [2023, 4, 'Outono',      86],
    [2023, 4, 'Outono',      87],
    [2023, 4, 'Outono',      88],
    [2023, 4, 'Outono',      89],
    [2023, 4, 'Outono',      90],
    [2023, 4, 'Outono',      91],
    [2023, 4, 'Outono',      92],
    [2023, 4, 'Outono',      93],
    [2023, 4, 'Outono',      94],
    [2023, 4, 'Outono',      95],
    [2023, 4, 'Outono',      96],
    [2023, 4, 'Outono',      97],
    [2023, 4, 'Outono',      97],
    [2023, 4, 'Outono',      97],
    [2023, 4, 'Outono',      97],
    [2023, 4, 'Outono',      97],
    # Maio 2023
    [2023, 5, 'Outono',      97],
    [2023, 5, 'Outono',      97],
    [2023, 5, 'Outono',      97],
    [2023, 5, 'Outono',      97],
    [2023, 5, 'Outono',      97],
    [2023, 5, 'Outono',      97],
    [2023, 5, 'Outono',      97],
    [2023, 5, 'Outono',      97],
    [2023, 5, 'Outono',      101],
    [2023, 5, 'Outono',      102],
    [2023, 5, 'Outono',      103],
    [2023, 5, 'Outono',      104],
    [2023, 5, 'Outono',      105],
    [2023, 5, 'Outono',      106],
    [2023, 5, 'Outono',      107],
    [2023, 5, 'Outono',      108],
    [2023, 5, 'Outono',      109],
    [2023, 5, 'Outono',      110],
    [2023, 5, 'Outono',      111],
    [2023, 5, 'Outono',      112],
    # Junho  2023
    [2023, 6, 'Outono',      113],
    [2023, 6, 'Outono',      114],
    [2023, 6, 'Outono',      115],
    [2023, 6, 'Outono',      116],
    [2023, 6, 'Outono',      117],
    [2023, 6, 'Outono',      120],
    [2023, 6, 'Outono',      121],
    [2023, 6, 'Outono',      122],
    [2023, 6, 'Outono',      122],
    [2023, 6, 'Outono',      122],
    [2023, 6, 'Outono',      123],
    [2023, 6, 'Outono',      123],
    [2023, 6, 'Outono',      123],
    [2023, 6, 'Outono',      123],
    [2023, 6, 'Outono',      123],
    [2023, 6, 'Outono',      123],
    [2023, 6, 'Outono',      123],
    [2023, 6, 'Outono',      123],
    [2023, 6, 'Outono',      123],
    [2023, 6, 'Outono',      123]

], columns=['Ano', 'Mes', 'Estacao', 'Crescimento']);



inverno2023 = pd.DataFrame([
    #ano  mes estacao  crescimento
    # Junho  2023
    [2023, 6, 'Inverno',      138],
    [2023, 6, 'Inverno',      138],
    [2023, 6, 'Inverno',      139],
    [2023, 6, 'Inverno',      139],
    [2023, 6, 'Inverno',      140],
    [2023, 6, 'Inverno',      140],
    [2023, 6, 'Inverno',      140],
    [2023, 6, 'Inverno',      140],
    [2023, 6, 'Inverno',      140],
    [2023, 6, 'Inverno',      140],
    [2023, 6, 'Inverno',      141],
    [2023, 6, 'Inverno',      141],
    [2023, 6, 'Inverno',      141],
    [2023, 6, 'Inverno',      141],
    [2023, 6, 'Inverno',      141],
    [2023, 6, 'Inverno',      141],
    [2023, 6, 'Inverno',      142],
    [2023, 6, 'Inverno',      142],
    [2023, 6, 'Inverno',      142],
    [2023, 6, 'Inverno',      142],
    # Julho  2023
    [2023, 7, 'Inverno',      142],
    [2023, 7, 'Inverno',      142],
    [2023, 7, 'Inverno',      142],
    [2023, 7, 'Inverno',      142],
    [2023, 7, 'Inverno',      143],
    [2023, 7, 'Inverno',      143],
    [2023, 7, 'Inverno',      143],
    [2023, 7, 'Inverno',      143],
    [2023, 7, 'Inverno',      143],
    [2023, 7, 'Inverno',      143],
    [2023, 7, 'Inverno',      143],
    [2023, 7, 'Inverno',      143],
    [2023, 7, 'Inverno',      143],
    [2023, 7, 'Inverno',      143],
    [2023, 7, 'Inverno',      143],
    [2023, 7, 'Inverno',      143],
    [2023, 7, 'Inverno',      143],
    [2023, 7, 'Inverno',      143],
    [2023, 7, 'Inverno',      143],
    [2023, 7, 'Inverno',      143],
    # Agosto  2023
    [2023, 8, 'Inverno',      144],
    [2023, 8, 'Inverno',      144],
    [2023, 8, 'Inverno',      144],
    [2023, 8, 'Inverno',      144],
    [2023, 8, 'Inverno',      144],
    [2023, 8, 'Inverno',      144],
    [2023, 8, 'Inverno',      144],
    [2023, 8, 'Inverno',      144],
    [2023, 8, 'Inverno',      144],
    [2023, 8, 'Inverno',      144],
    [2023, 8, 'Inverno',      144],
    [2023, 8, 'Inverno',      145],
    [2023, 8, 'Inverno',      145],
    [2023, 8, 'Inverno',      145],
    [2023, 8, 'Inverno',      145],
    [2023, 8, 'Inverno',      145],
    [2023, 8, 'Inverno',      145],
    [2023, 8, 'Inverno',      145],
    [2023, 8, 'Inverno',      145],
    [2023, 8, 'Inverno',      145],
    # Setembro 2023
    [2023, 9, 'Inverno',      150],
    [2023, 9, 'Inverno',      150],
    [2023, 9, 'Inverno',      150],
    [2023, 9, 'Inverno',      150],
    [2023, 9, 'Inverno',      140],
    [2023, 9, 'Inverno',      130],
    [2023, 9, 'Inverno',      125],
    [2023, 9, 'Inverno',      110],
    [2023, 9, 'Inverno',      105],
    [2023, 9, 'Inverno',      100],
    [2023, 9, 'Inverno',      100],
    [2023, 9, 'Inverno',      100],
    [2023, 9, 'Inverno',      100],
    [2023, 9, 'Inverno',      100],
    [2023, 9, 'Inverno',      100],
    [2023, 9, 'Inverno',      100],
    [2023, 9, 'Inverno',      100],
    [2023, 9, 'Inverno',      100],
    [2023, 9, 'Inverno',      100],
    [2023, 9, 'Inverno',      100]

], columns=['Ano', 'Mes', 'Estacao', 'Crescimento']);



primavera2023 = pd.DataFrame([
    #ano  mes estacao  crescimento
    # Setembro 2023
    [2023, 9, 'Primavera',    95],
    [2023, 9, 'Primavera',    95],
    [2023, 9, 'Primavera',    95],
    [2023, 9, 'Primavera',    90],
    [2023, 9, 'Primavera',    90],
    [2023, 9, 'Primavera',    90],
    [2023, 9, 'Primavera',    90],
    [2023, 9, 'Primavera',    90],
    [2023, 9, 'Primavera',    90],
    [2023, 9, 'Primavera',    90],
    [2023, 9, 'Primavera',    90],
    [2023, 9, 'Primavera',    90],
    [2023, 9, 'Primavera',    90],
    [2023, 9, 'Primavera',    90],
    [2023, 9, 'Primavera',    90],
    [2023, 9, 'Primavera',    90],
    [2023, 9, 'Primavera',    90],
    [2023, 9, 'Primavera',    90],
    [2023, 9, 'Primavera',    90],
    [2023, 9, 'Primavera',    90],
    # Outubro 2023
    [2023, 10, 'Primavera',    90],
    [2023, 10, 'Primavera',    90],
    [2023, 10, 'Primavera',    90],
    [2023, 10, 'Primavera',    90],
    [2023, 10, 'Primavera',    90],
    [2023, 10, 'Primavera',    90],
    [2023, 10, 'Primavera',    90],
    [2023, 10, 'Primavera',    90],
    [2023, 10, 'Primavera',    80],
    [2023, 10, 'Primavera',    80],
    [2023, 10, 'Primavera',    80],
    [2023, 10, 'Primavera',    80],
    [2023, 10, 'Primavera',    80],
    [2023, 10, 'Primavera',    80],
    [2023, 10, 'Primavera',    70],
    [2023, 10, 'Primavera',    70],
    [2023, 10, 'Primavera',    70],
    [2023, 10, 'Primavera',    70],
    [2023, 10, 'Primavera',    70],
    [2023, 10, 'Primavera',    70],
    # Novembro 2023
    [2023, 11, 'Primavera',    60],
    [2023, 11, 'Primavera',    60],
    [2023, 11, 'Primavera',    60],
    [2023, 11, 'Primavera',    60],
    [2023, 11, 'Primavera',    60],
    [2023, 11, 'Primavera',    60],
    [2023, 11, 'Primavera',    60],
    [2023, 11, 'Primavera',    60],
    [2023, 11, 'Primavera',    52],
    [2023, 11, 'Primavera',    52],
    [2023, 11, 'Primavera',    52],
    [2023, 11, 'Primavera',    52],
    [2023, 11, 'Primavera',    52],
    [2023, 11, 'Primavera',    52],
    [2023, 11, 'Primavera',    52],
    [2023, 11, 'Primavera',    52],
    [2023, 11, 'Primavera',    52],
    [2023, 11, 'Primavera',    52],
    [2023, 11, 'Primavera',    45],
    [2023, 11, 'Primavera',    45],
    # Dezembro 2023
    [2023, 12, 'Primavera',    45],
    [2023, 12, 'Primavera',    40],
    [2023, 12, 'Primavera',    40],
    [2023, 12, 'Primavera',    40],
    [2023, 12, 'Primavera',    40],
    [2023, 12, 'Primavera',    40],
    [2023, 12, 'Primavera',    40],
    [2023, 12, 'Primavera',    40],
    [2023, 12, 'Primavera',    40],
    [2023, 12, 'Primavera',    40],
    [2023, 12, 'Primavera',    42],
    [2023, 12, 'Primavera',    43],
    [2023, 12, 'Primavera',    43],
    [2023, 12, 'Primavera',    43],
    [2023, 12, 'Primavera',    43],
    [2023, 12, 'Primavera',    43],
    [2023, 12, 'Primavera',    43],
    [2023, 12, 'Primavera',    43],
    [2023, 12, 'Primavera',    43],
    [2023, 12, 'Primavera',    43]

], columns=['Ano', 'Mes', 'Estacao', 'Crescimento']);


# Juntando os datasets das estações de 2023 para ter um dataset completo

# Lista contendo os quatro DataFrames
datasets_juntar = [verao2023, outono2023, inverno2023, primavera2023]

# Concatenando os DataFrames na vertical (mesmo número de colunas)
dataset2023 = pd.concat(datasets_juntar, ignore_index=True)

dataset2023['Crescimento'] = dataset2023['Crescimento'] + 25;

print( dataset2023.describe() )


# Conferindo o padrão pra ver se ta ficando do jeito que eu quero
import matplotlib.pyplot as plt
import pandas as pd

# Filtrando os dados de 2020
dados_2023 = dataset2023[dataset2023['Ano'] == 2023]

dataset2023.to_csv('datasets/soja2023.csv', sep=';', index=False)

# Agora vamos agrupar os dados por mês e somar o Crescimento
crescimento_mensal = dados_2023.groupby('Mes')['Crescimento'].mean()

# Criando o gráfico
plt.figure(figsize=(10, 6))
plt.plot(crescimento_mensal.index, crescimento_mensal.values, marker='o', color='b', linestyle='-', linewidth=2, markersize=6)

# Adicionando título e rótulos
plt.title('Evolução do Crescimento - 2023', fontsize=14)
plt.xlabel('Mês', fontsize=12)
plt.ylabel('Crescimento', fontsize=12)
plt.xticks(crescimento_mensal.index, ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'])
plt.grid(True)
plt.tight_layout()

# Exibindo o gráfico
plt.show()