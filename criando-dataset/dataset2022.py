import pandas as pd
import numpy as np

# Escolho a Soja
# Cresce mais rápido na estação: Primavera / Verão

# 20 amostras por mes

verao2022 = pd.DataFrame([
    #ano  mes estacao  crescimento
    #Janeiro 2022
    [2022, 1, 'Verão',      42],
    [2022, 1, 'Verão',      44],
    [2022, 1, 'Verão',      43],
    [2022, 1, 'Verão',      43],
    [2022, 1, 'Verão',      43],
    [2022, 1, 'Verão',      43],
    [2022, 1, 'Verão',      43],
    [2022, 1, 'Verão',      43],
    [2022, 1, 'Verão',      43],
    [2022, 1, 'Verão',      43],
    [2022, 1, 'Verão',      43],
    [2022, 1, 'Verão',      43],
    [2022, 1, 'Verão',      44],
    [2022, 1, 'Verão',      44],
    [2022, 1, 'Verão',      44],
    [2022, 1, 'Verão',      44],
    [2022, 1, 'Verão',      44],
    [2022, 1, 'Verão',      44],
    [2022, 1, 'Verão',      44],
    [2022, 1, 'Verão',      44],
    #Fevereiro 2022
    [2022, 2, 'Verão',      44],
    [2022, 2, 'Verão',      44],
    [2022, 2, 'Verão',      44],
    [2022, 2, 'Verão',      44],
    [2022, 2, 'Verão',      44],
    [2022, 2, 'Verão',      44],
    [2022, 2, 'Verão',      44],
    [2022, 2, 'Verão',      44],
    [2022, 2, 'Verão',      44],
    [2022, 2, 'Verão',      44],
    [2022, 2, 'Verão',      44],
    [2022, 2, 'Verão',      44],
    [2022, 2, 'Verão',      44],
    [2022, 2, 'Verão',      44],
    [2022, 2, 'Verão',      44],
    [2022, 2, 'Verão',      44],
    [2022, 2, 'Verão',      44],
    [2022, 2, 'Verão',      44],
    [2022, 2, 'Verão',      44],
    [2022, 2, 'Verão',      44],
    #Março 2022
    [2022, 3, 'Verão',      44],
    [2022, 3, 'Verão',      44],
    [2022, 3, 'Verão',      44],
    [2022, 3, 'Verão',      44],
    [2022, 3, 'Verão',      44],
    [2022, 3, 'Verão',      44],
    [2022, 3, 'Verão',      44],
    [2022, 3, 'Verão',      44],
    [2022, 3, 'Verão',      44],
    [2022, 3, 'Verão',      44],
    [2022, 3, 'Verão',      44],
    [2022, 3, 'Verão',      44],
    [2022, 3, 'Verão',      44],
    [2022, 3, 'Verão',      44],
    [2022, 3, 'Verão',      44],
    [2022, 3, 'Verão',      44],
    [2022, 3, 'Verão',      44],
    [2022, 3, 'Verão',      44],
    [2022, 3, 'Verão',      44],
    [2022, 3, 'Verão',      44]


], columns=['Ano', 'Mes', 'Estacao', 'Crescimento']);


outono2022 = pd.DataFrame([
    #ano  mes estacao  crescimento
    # Março 2022
    [2022, 3, 'Outono',      51],
    [2022, 3, 'Outono',      50],
    [2022, 3, 'Outono',      52],
    [2022, 3, 'Outono',      53],
    [2022, 3, 'Outono',      52],
    [2022, 3, 'Outono',      52],
    [2022, 3, 'Outono',      52],
    [2022, 3, 'Outono',      52],
    [2022, 3, 'Outono',      53],
    [2022, 3, 'Outono',      53],
    [2022, 3, 'Outono',      53],
    [2022, 3, 'Outono',      53],
    [2022, 3, 'Outono',      53],
    [2022, 3, 'Outono',      53],
    [2022, 3, 'Outono',      53],
    [2022, 3, 'Outono',      53],
    [2022, 3, 'Outono',      53],
    [2022, 3, 'Outono',      53],
    [2022, 3, 'Outono',      53],
    [2022, 3, 'Outono',      53],
    # Abril 2022
    [2022, 4, 'Outono',      60],
    [2022, 4, 'Outono',      60],
    [2022, 4, 'Outono',      60],
    [2022, 4, 'Outono',      60],
    [2022, 4, 'Outono',      60],
    [2022, 4, 'Outono',      60],
    [2022, 4, 'Outono',      60],
    [2022, 4, 'Outono',      60],
    [2022, 4, 'Outono',      60],
    [2022, 4, 'Outono',      60],
    [2022, 4, 'Outono',      60],
    [2022, 4, 'Outono',      65],
    [2022, 4, 'Outono',      65],
    [2022, 4, 'Outono',      65],
    [2022, 4, 'Outono',      65],
    [2022, 4, 'Outono',      65],
    [2022, 4, 'Outono',      65],
    [2022, 4, 'Outono',      65],
    [2022, 4, 'Outono',      65],
    [2022, 4, 'Outono',      65],
    # Maio 2022
    [2022, 5, 'Outono',      65],
    [2022, 5, 'Outono',      65],
    [2022, 5, 'Outono',      65],
    [2022, 5, 'Outono',      65],
    [2022, 5, 'Outono',      65],
    [2022, 5, 'Outono',      65],
    [2022, 5, 'Outono',      65],
    [2022, 5, 'Outono',      65],
    [2022, 5, 'Outono',      65],
    [2022, 5, 'Outono',      65],
    [2022, 5, 'Outono',      65],
    [2022, 5, 'Outono',      65],
    [2022, 5, 'Outono',      65],
    [2022, 5, 'Outono',      65],
    [2022, 5, 'Outono',      65],
    [2022, 5, 'Outono',      65],
    [2022, 5, 'Outono',      65],
    [2022, 5, 'Outono',      65],
    [2022, 5, 'Outono',      65],
    [2022, 5, 'Outono',      65],
    # Junho  2022
    [2022, 6, 'Outono',      65],
    [2022, 6, 'Outono',      65],
    [2022, 6, 'Outono',      65],
    [2022, 6, 'Outono',      65],
    [2022, 6, 'Outono',      65],
    [2022, 6, 'Outono',      65],
    [2022, 6, 'Outono',      65],
    [2022, 6, 'Outono',      65],
    [2022, 6, 'Outono',      65],
    [2022, 6, 'Outono',      65],
    [2022, 6, 'Outono',      65],
    [2022, 6, 'Outono',      65],
    [2022, 6, 'Outono',      65],
    [2022, 6, 'Outono',      65],
    [2022, 6, 'Outono',      65],
    [2022, 6, 'Outono',      65],
    [2022, 6, 'Outono',      65],
    [2022, 6, 'Outono',      65],
    [2022, 6, 'Outono',      65],
    [2022, 6, 'Outono',      65]

], columns=['Ano', 'Mes', 'Estacao', 'Crescimento']);



inverno2022 = pd.DataFrame([
    #ano  mes estacao  crescimento
    # Junho  2022
    [2022, 6, 'Inverno',      98],
    [2022, 6, 'Inverno',      98],
    [2022, 6, 'Inverno',      98],
    [2022, 6, 'Inverno',      98],
    [2022, 6, 'Inverno',      98],
    [2022, 6, 'Inverno',      98],
    [2022, 6, 'Inverno',      98],
    [2022, 6, 'Inverno',      98],
    [2022, 6, 'Inverno',      98],
    [2022, 6, 'Inverno',      98],
    [2022, 6, 'Inverno',      98],
    [2022, 6, 'Inverno',      98],
    [2022, 6, 'Inverno',      98],
    [2022, 6, 'Inverno',      98],
    [2022, 6, 'Inverno',      98],
    [2022, 6, 'Inverno',      98],
    [2022, 6, 'Inverno',      98],
    [2022, 6, 'Inverno',      98],
    [2022, 6, 'Inverno',      98],
    [2022, 6, 'Inverno',      98],
    # Julho  2022
    [2022, 7, 'Inverno',      110],
    [2022, 7, 'Inverno',      110],
    [2022, 7, 'Inverno',      110],
    [2022, 7, 'Inverno',      110],
    [2022, 7, 'Inverno',      110],
    [2022, 7, 'Inverno',      110],
    [2022, 7, 'Inverno',      110],
    [2022, 7, 'Inverno',      110],
    [2022, 7, 'Inverno',      110],
    [2022, 7, 'Inverno',      110],
    [2022, 7, 'Inverno',      110],
    [2022, 7, 'Inverno',      110],
    [2022, 7, 'Inverno',      110],
    [2022, 7, 'Inverno',      110],
    [2022, 7, 'Inverno',      110],
    [2022, 7, 'Inverno',      110],
    [2022, 7, 'Inverno',      110],
    [2022, 7, 'Inverno',      110],
    [2022, 7, 'Inverno',      110],
    [2022, 7, 'Inverno',      110],
    # Agosto  2022
    [2022, 8, 'Inverno',      110],
    [2022, 8, 'Inverno',      110],
    [2022, 8, 'Inverno',      110],
    [2022, 8, 'Inverno',      110],
    [2022, 8, 'Inverno',      110],
    [2022, 8, 'Inverno',      110],
    [2022, 8, 'Inverno',      110],
    [2022, 8, 'Inverno',      110],
    [2022, 8, 'Inverno',      110],
    [2022, 8, 'Inverno',      115],
    [2022, 8, 'Inverno',      115],
    [2022, 8, 'Inverno',      115],
    [2022, 8, 'Inverno',      115],
    [2022, 8, 'Inverno',      115],
    [2022, 8, 'Inverno',      115],
    [2022, 8, 'Inverno',      115],
    [2022, 8, 'Inverno',      115],
    [2022, 8, 'Inverno',      115],
    [2022, 8, 'Inverno',      115],
    [2022, 8, 'Inverno',      115],
    # Setembro 2022
    [2022, 9, 'Inverno',      110],
    [2022, 9, 'Inverno',      110],
    [2022, 9, 'Inverno',      110],
    [2022, 9, 'Inverno',      95],
    [2022, 9, 'Inverno',      95],
    [2022, 9, 'Inverno',      95],
    [2022, 9, 'Inverno',      95],
    [2022, 9, 'Inverno',      95],
    [2022, 9, 'Inverno',      95],
    [2022, 9, 'Inverno',      95],
    [2022, 9, 'Inverno',      95],
    [2022, 9, 'Inverno',      95],
    [2022, 9, 'Inverno',      95],
    [2022, 9, 'Inverno',      95],
    [2022, 9, 'Inverno',      95],
    [2022, 9, 'Inverno',      95],
    [2022, 9, 'Inverno',      95],
    [2022, 9, 'Inverno',      95],
    [2022, 9, 'Inverno',      95],
    [2022, 9, 'Inverno',      95]

], columns=['Ano', 'Mes', 'Estacao', 'Crescimento']);



primavera2022 = pd.DataFrame([
    #ano  mes estacao  crescimento
    # Setembro 2022
    [2022, 9, 'Primavera',    56],
    [2022, 9, 'Primavera',    55],
    [2022, 9, 'Primavera',    55],
    [2022, 9, 'Primavera',    55],
    [2022, 9, 'Primavera',    54],
    [2022, 9, 'Primavera',    55],
    [2022, 9, 'Primavera',    56],
    [2022, 9, 'Primavera',    57],
    [2022, 9, 'Primavera',    55],
    [2022, 9, 'Primavera',    56],
    [2022, 9, 'Primavera',    57],
    [2022, 9, 'Primavera',    55],
    [2022, 9, 'Primavera',    55],
    [2022, 9, 'Primavera',    50],
    [2022, 9, 'Primavera',    55],
    [2022, 9, 'Primavera',    52],
    [2022, 9, 'Primavera',    51],
    [2022, 9, 'Primavera',    53],
    [2022, 9, 'Primavera',    52],
    [2022, 9, 'Primavera',    50],
    # Outubro 2022
    [2022, 10, 'Primavera',    50],
    [2022, 10, 'Primavera',    51],
    [2022, 10, 'Primavera',    52],
    [2022, 10, 'Primavera',    53],
    [2022, 10, 'Primavera',    52],
    [2022, 10, 'Primavera',    48],
    [2022, 10, 'Primavera',    48],
    [2022, 10, 'Primavera',    48],
    [2022, 10, 'Primavera',    48],
    [2022, 10, 'Primavera',    47],
    [2022, 10, 'Primavera',    47],
    [2022, 10, 'Primavera',    47],
    [2022, 10, 'Primavera',    47],
    [2022, 10, 'Primavera',    47],
    [2022, 10, 'Primavera',    47],
    [2022, 10, 'Primavera',    47],
    [2022, 10, 'Primavera',    47],
    [2022, 10, 'Primavera',    47],
    [2022, 10, 'Primavera',    47],
    [2022, 10, 'Primavera',    47],
    # Novembro 2022
    [2022, 11, 'Primavera',    47],
    [2022, 11, 'Primavera',    47],
    [2022, 11, 'Primavera',    47],
    [2022, 11, 'Primavera',    47],
    [2022, 11, 'Primavera',    47],
    [2022, 11, 'Primavera',    47],
    [2022, 11, 'Primavera',    47],
    [2022, 11, 'Primavera',    47],
    [2022, 11, 'Primavera',    47],
    [2022, 11, 'Primavera',    47],
    [2022, 11, 'Primavera',    47],
    [2022, 11, 'Primavera',    47],
    [2022, 11, 'Primavera',    47],
    [2022, 11, 'Primavera',    43],
    [2022, 11, 'Primavera',    43],
    [2022, 11, 'Primavera',    43],
    [2022, 11, 'Primavera',    43],
    [2022, 11, 'Primavera',    43],
    [2022, 11, 'Primavera',    43],
    [2022, 11, 'Primavera',    43],
    # Dezembro 2022
    [2022, 12, 'Primavera',    43],
    [2022, 12, 'Primavera',    43],
    [2022, 12, 'Primavera',    43],
    [2022, 12, 'Primavera',    43],
    [2022, 12, 'Primavera',    43],
    [2022, 12, 'Primavera',    43],
    [2022, 12, 'Primavera',    43],
    [2022, 12, 'Primavera',    43],
    [2022, 12, 'Primavera',    43],
    [2022, 12, 'Primavera',    43],
    [2022, 12, 'Primavera',    43],
    [2022, 12, 'Primavera',    43],
    [2022, 12, 'Primavera',    43],
    [2022, 12, 'Primavera',    43],
    [2022, 12, 'Primavera',    43],
    [2022, 12, 'Primavera',    43],
    [2022, 12, 'Primavera',    43],
    [2022, 12, 'Primavera',    43],
    [2022, 12, 'Primavera',    43],
    [2022, 12, 'Primavera',    43]

], columns=['Ano', 'Mes', 'Estacao', 'Crescimento']);


# Juntando os datasets das estações de 2022 para ter um dataset completo

# Lista contendo os quatro DataFrames
datasets_juntar = [verao2022, outono2022, inverno2022, primavera2022]

# Concatenando os DataFrames na vertical (mesmo número de colunas)
dataset2022 = pd.concat(datasets_juntar, ignore_index=True)

print( dataset2022.describe() )


# Conferindo o padrão pra ver se ta ficando do jeito que eu quero
import matplotlib.pyplot as plt
import pandas as pd

# Filtrando os dados de 2020
dados_2022 = dataset2022[dataset2022['Ano'] == 2022]

dataset2022.to_csv('datasets/soja2022.csv', sep=';', index=False)

# Agora vamos agrupar os dados por mês e somar o Crescimento
crescimento_mensal = dados_2022.groupby('Mes')['Crescimento'].mean()

# Criando o gráfico
plt.figure(figsize=(10, 6))
plt.plot(crescimento_mensal.index, crescimento_mensal.values, marker='o', color='b', linestyle='-', linewidth=2, markersize=6)

# Adicionando título e rótulos
plt.title('Evolução do Crescimento - 2022', fontsize=14)
plt.ylim(0, 150)  
plt.xlabel('Mês', fontsize=12)
plt.ylabel('Crescimento', fontsize=12)
plt.xticks(crescimento_mensal.index, ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'])
plt.grid(True)
plt.tight_layout()

# Exibindo o gráfico
plt.show()