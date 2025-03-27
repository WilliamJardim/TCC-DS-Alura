import pandas as pd
import numpy as np

# Escolho a Soja
# Cresce mais rápido na estação: Primavera / Verão

# 20 amostras por mes

verao2020 = pd.DataFrame([
    #ano  mes estacao  crescimento
    #Janeiro 2020
    [2020, 1, 'Verão',      46],
    [2020, 1, 'Verão',      42],
    [2020, 1, 'Verão',      44],
    [2020, 1, 'Verão',      42],
    [2020, 1, 'Verão',      40],
    [2020, 1, 'Verão',      44],
    [2020, 1, 'Verão',      42],
    [2020, 1, 'Verão',      41],
    [2020, 1, 'Verão',      44],
    [2020, 1, 'Verão',      43],
    [2020, 1, 'Verão',      44],
    [2020, 1, 'Verão',      42],
    [2020, 1, 'Verão',      43],
    [2020, 1, 'Verão',      42],
    [2020, 1, 'Verão',      41],
    [2020, 1, 'Verão',      45],
    [2020, 1, 'Verão',      42],
    [2020, 1, 'Verão',      41],
    [2020, 1, 'Verão',      44],
    [2020, 1, 'Verão',      43],
    #Fevereiro 2020
    [2020, 2, 'Verão',      44],
    [2020, 2, 'Verão',      41],
    [2020, 2, 'Verão',      40],
    [2020, 2, 'Verão',      41],
    [2020, 2, 'Verão',      42],
    [2020, 2, 'Verão',      44],
    [2020, 2, 'Verão',      43],
    [2020, 2, 'Verão',      45],
    [2020, 2, 'Verão',      41],
    [2020, 2, 'Verão',      42],
    [2020, 2, 'Verão',      45],
    [2020, 2, 'Verão',      40],
    [2020, 2, 'Verão',      42],
    [2020, 2, 'Verão',      42],
    [2020, 2, 'Verão',      40],
    [2020, 2, 'Verão',      41],
    [2020, 2, 'Verão',      40],
    [2020, 2, 'Verão',      40],
    [2020, 2, 'Verão',      41],
    [2020, 2, 'Verão',      40],
    #Março 2020
    [2020, 3, 'Verão',      44],
    [2020, 3, 'Verão',      42],
    [2020, 3, 'Verão',      45],
    [2020, 3, 'Verão',      42],
    [2020, 3, 'Verão',      42],
    [2020, 3, 'Verão',      44],
    [2020, 3, 'Verão',      42],
    [2020, 3, 'Verão',      41],
    [2020, 3, 'Verão',      44],
    [2020, 3, 'Verão',      41],
    [2020, 3, 'Verão',      47],
    [2020, 3, 'Verão',      47],
    [2020, 3, 'Verão',      48],
    [2020, 3, 'Verão',      47],
    [2020, 3, 'Verão',      45],
    [2020, 3, 'Verão',      47],
    [2020, 3, 'Verão',      47],
    [2020, 3, 'Verão',      45],
    [2020, 3, 'Verão',      47],
    [2020, 3, 'Verão',      48]


], columns=['Ano', 'Mes', 'Estacao', 'Crescimento']);


outono2020 = pd.DataFrame([
    #ano  mes estacao  crescimento
    # Março 2020
    [2020, 3, 'Outono',      48],
    [2020, 3, 'Outono',      46],
    [2020, 3, 'Outono',      44],
    [2020, 3, 'Outono',      45],
    [2020, 3, 'Outono',      44],
    [2020, 3, 'Outono',      45],
    [2020, 3, 'Outono',      46],
    [2020, 3, 'Outono',      44],
    [2020, 3, 'Outono',      46],
    [2020, 3, 'Outono',      44],
    [2020, 3, 'Outono',      45],
    [2020, 3, 'Outono',      44],
    [2020, 3, 'Outono',      46],
    [2020, 3, 'Outono',      45],
    [2020, 3, 'Outono',      45],
    [2020, 3, 'Outono',      45],
    [2020, 3, 'Outono',      44],
    [2020, 3, 'Outono',      46],
    [2020, 3, 'Outono',      44],
    [2020, 3, 'Outono',      46],
    # Abril 2020
    [2020, 4, 'Outono',      48],
    [2020, 4, 'Outono',      48],
    [2020, 4, 'Outono',      48],
    [2020, 4, 'Outono',      48],
    [2020, 4, 'Outono',      48],
    [2020, 4, 'Outono',      48],
    [2020, 4, 'Outono',      48],
    [2020, 4, 'Outono',      48],
    [2020, 4, 'Outono',      49],
    [2020, 4, 'Outono',      49],
    [2020, 4, 'Outono',      49],
    [2020, 4, 'Outono',      49],
    [2020, 4, 'Outono',      49],
    [2020, 4, 'Outono',      49],
    [2020, 4, 'Outono',      49],
    [2020, 4, 'Outono',      49],
    [2020, 4, 'Outono',      49],
    [2020, 4, 'Outono',      49],
    [2020, 4, 'Outono',      49],
    [2020, 4, 'Outono',      49],
    # Maio 2020
    [2020, 5, 'Outono',      49],
    [2020, 5, 'Outono',      49],
    [2020, 5, 'Outono',      49],
    [2020, 5, 'Outono',      49],
    [2020, 5, 'Outono',      49],
    [2020, 5, 'Outono',      49],
    [2020, 5, 'Outono',      49],
    [2020, 5, 'Outono',      49],
    [2020, 5, 'Outono',      49],
    [2020, 5, 'Outono',      49],
    [2020, 5, 'Outono',      49],
    [2020, 5, 'Outono',      49],
    [2020, 5, 'Outono',      49],
    [2020, 5, 'Outono',      49],
    [2020, 5, 'Outono',      49],
    [2020, 5, 'Outono',      49],
    [2020, 5, 'Outono',      49],
    [2020, 5, 'Outono',      49],
    [2020, 5, 'Outono',      49],
    [2020, 5, 'Outono',      49],
    # Junho  2020
    [2020, 6, 'Outono',      65],
    [2020, 6, 'Outono',      64],
    [2020, 6, 'Outono',      62],
    [2020, 6, 'Outono',      63],
    [2020, 6, 'Outono',      67],
    [2020, 6, 'Outono',      68],
    [2020, 6, 'Outono',      62],
    [2020, 6, 'Outono',      65],
    [2020, 6, 'Outono',      64],
    [2020, 6, 'Outono',      65],
    [2020, 6, 'Outono',      63],
    [2020, 6, 'Outono',      60],
    [2020, 6, 'Outono',      61],
    [2020, 6, 'Outono',      92],
    [2020, 6, 'Outono',      95],
    [2020, 6, 'Outono',      96],
    [2020, 6, 'Outono',      97],
    [2020, 6, 'Outono',      95],
    [2020, 6, 'Outono',      94],
    [2020, 6, 'Outono',      92]

], columns=['Ano', 'Mes', 'Estacao', 'Crescimento']);



inverno2020 = pd.DataFrame([
    #ano  mes estacao  crescimento
    # Junho  2020
    [2020, 6, 'Inverno',      120],
    [2020, 6, 'Inverno',      109],
    [2020, 6, 'Inverno',      110],
    [2020, 6, 'Inverno',      107],
    [2020, 6, 'Inverno',      109],
    [2020, 6, 'Inverno',      120],
    [2020, 6, 'Inverno',      122],
    [2020, 6, 'Inverno',      125],
    [2020, 6, 'Inverno',      115],
    [2020, 6, 'Inverno',      119],
    [2020, 6, 'Inverno',      118],
    [2020, 6, 'Inverno',      112],
    [2020, 6, 'Inverno',      111],
    [2020, 6, 'Inverno',      113],
    [2020, 6, 'Inverno',      115],
    [2020, 6, 'Inverno',      120],
    [2020, 6, 'Inverno',      119],
    [2020, 6, 'Inverno',      111],
    [2020, 6, 'Inverno',      119],
    [2020, 6, 'Inverno',      120],
    # Julho  2020
    [2020, 7, 'Inverno',      125],
    [2020, 7, 'Inverno',      115],
    [2020, 7, 'Inverno',      115],
    [2020, 7, 'Inverno',      115],
    [2020, 7, 'Inverno',      118],
    [2020, 7, 'Inverno',      125],
    [2020, 7, 'Inverno',      118],
    [2020, 7, 'Inverno',      119],
    [2020, 7, 'Inverno',      119],
    [2020, 7, 'Inverno',      120],
    [2020, 7, 'Inverno',      125],
    [2020, 7, 'Inverno',      125],
    [2020, 4, 'Inverno',      125],
    [2020, 7, 'Inverno',      125],
    [2020, 7, 'Inverno',      115],
    [2020, 7, 'Inverno',      115],
    [2020, 7, 'Inverno',      118],
    [2020, 7, 'Inverno',      117],
    [2020, 7, 'Inverno',      122],
    [2020, 7, 'Inverno',      125],
    # Agosto  2020
    [2020, 8, 'Inverno',      140],
    [2020, 8, 'Inverno',      135],
    [2020, 8, 'Inverno',      135],
    [2020, 8, 'Inverno',      132],
    [2020, 8, 'Inverno',      138],
    [2020, 8, 'Inverno',      137],
    [2020, 8, 'Inverno',      140],
    [2020, 8, 'Inverno',      138],
    [2020, 8, 'Inverno',      132],
    [2020, 8, 'Inverno',      134],
    [2020, 8, 'Inverno',      131],
    [2020, 8, 'Inverno',      134],
    [2020, 8, 'Inverno',      136],
    [2020, 8, 'Inverno',      137],
    [2020, 8, 'Inverno',      138],
    [2020, 8, 'Inverno',      139],
    [2020, 8, 'Inverno',      132],
    [2020, 8, 'Inverno',      134],
    [2020, 8, 'Inverno',      140],
    [2020, 8, 'Inverno',      140],
    # Setembro 2020
    [2020, 9, 'Inverno',      140],
    [2020, 9, 'Inverno',      135],
    [2020, 9, 'Inverno',      135],
    [2020, 9, 'Inverno',      132],
    [2020, 9, 'Inverno',      138],
    [2020, 9, 'Inverno',      137],
    [2020, 9, 'Inverno',      140],
    [2020, 9, 'Inverno',      95],
    [2020, 9, 'Inverno',      95],
    [2020, 9, 'Inverno',      95],
    [2020, 9, 'Inverno',      95],
    [2020, 9, 'Inverno',      95],
    [2020, 9, 'Inverno',      95],
    [2020, 9, 'Inverno',      95],
    [2020, 9, 'Inverno',      95],
    [2020, 9, 'Inverno',      95],
    [2020, 9, 'Inverno',      95],
    [2020, 9, 'Inverno',      95],
    [2020, 9, 'Inverno',      95],
    [2020, 9, 'Inverno',      95]

], columns=['Ano', 'Mes', 'Estacao', 'Crescimento']);



primavera2020 = pd.DataFrame([
    #ano  mes estacao  crescimento
    # Setembro 2020
    [2020, 9, 'Primavera',    46],
    [2020, 9, 'Primavera',    48],
    [2020, 9, 'Primavera',    45],
    [2020, 9, 'Primavera',    44],
    [2020, 9, 'Primavera',    44],
    [2020, 9, 'Primavera',    45],
    [2020, 9, 'Primavera',    44],
    [2020, 9, 'Primavera',    43],
    [2020, 9, 'Primavera',    44],
    [2020, 9, 'Primavera',    43],
    [2020, 9, 'Primavera',    44],
    [2020, 9, 'Primavera',    42],
    [2020, 9, 'Primavera',    41],
    [2020, 9, 'Primavera',    41],
    [2020, 9, 'Primavera',    41],
    [2020, 9, 'Primavera',    41],
    [2020, 9, 'Primavera',    41],
    [2020, 9, 'Primavera',    41],
    [2020, 9, 'Primavera',    41],
    [2020, 9, 'Primavera',    41],
    # Outubro 2020
    [2020, 10, 'Primavera',    40],
    [2020, 10, 'Primavera',    43],
    [2020, 10, 'Primavera',    40],
    [2020, 10, 'Primavera',    41],
    [2020, 10, 'Primavera',    40],
    [2020, 10, 'Primavera',    40],
    [2020, 10, 'Primavera',    40],
    [2020, 10, 'Primavera',    40],
    [2020, 10, 'Primavera',    40],
    [2020, 10, 'Primavera',    40],
    [2020, 10, 'Primavera',    40],
    [2020, 10, 'Primavera',    40],
    [2020, 10, 'Primavera',    40],
    [2020, 10, 'Primavera',    40],
    [2020, 10, 'Primavera',    40],
    [2020, 10, 'Primavera',    40],
    [2020, 10, 'Primavera',    40],
    [2020, 10, 'Primavera',    40],
    [2020, 10, 'Primavera',    40],
    [2020, 10, 'Primavera',    40],
    # Novembro 2020
    [2020, 11, 'Primavera',    40],
    [2020, 11, 'Primavera',    43],
    [2020, 11, 'Primavera',    40],
    [2020, 11, 'Primavera',    41],
    [2020, 11, 'Primavera',    40],
    [2020, 11, 'Primavera',    40],
    [2020, 11, 'Primavera',    40],
    [2020, 11, 'Primavera',    40],
    [2020, 11, 'Primavera',    40],
    [2020, 11, 'Primavera',    40],
    [2020, 11, 'Primavera',    40],
    [2020, 11, 'Primavera',    40],
    [2020, 11, 'Primavera',    40],
    [2020, 11, 'Primavera',    40],
    [2020, 11, 'Primavera',    40],
    [2020, 11, 'Primavera',    40],
    [2020, 11, 'Primavera',    40],
    [2020, 11, 'Primavera',    40],
    [2020, 11, 'Primavera',    40],
    [2020, 11, 'Primavera',    40],
    # Dezembro 2020
    [2020, 12, 'Primavera',    45],
    [2020, 12, 'Primavera',    47],
    [2020, 12, 'Primavera',    44],
    [2020, 12, 'Primavera',    45],
    [2020, 12, 'Primavera',    44],
    [2020, 12, 'Primavera',    42],
    [2020, 12, 'Primavera',    45],
    [2020, 12, 'Primavera',    45],
    [2020, 12, 'Primavera',    44],
    [2020, 12, 'Primavera',    45],
    [2020, 12, 'Primavera',    44],
    [2020, 12, 'Primavera',    43],
    [2020, 12, 'Primavera',    44],
    [2020, 12, 'Primavera',    45],
    [2020, 12, 'Primavera',    44],
    [2020, 12, 'Primavera',    46],
    [2020, 12, 'Primavera',    43],
    [2020, 12, 'Primavera',    44],
    [2020, 12, 'Primavera',    43],
    [2020, 12, 'Primavera',    42]

], columns=['Ano', 'Mes', 'Estacao', 'Crescimento']);


# Juntando os datasets das estações de 2020 para ter um dataset completo

# Lista contendo os quatro DataFrames
datasets_juntar = [verao2020, outono2020, inverno2020, primavera2020]

# Concatenando os DataFrames na vertical (mesmo número de colunas)
dataset2020 = pd.concat(datasets_juntar, ignore_index=True)

dataset2020.to_csv('datasets/soja2020.csv', sep=';', index=False)

# Conferindo o padrão pra ver se ta ficando do jeito que eu quero
import matplotlib.pyplot as plt
import pandas as pd

#dataset2020['Crescimento'] = dataset2020['Crescimento'] - 20;

print( dataset2020.describe() )

# Filtrando os dados de 2020
dados_2020 = dataset2020[dataset2020['Ano'] == 2020]

# Agora vamos agrupar os dados por mês e somar o Crescimento
crescimento_mensal = dados_2020.groupby('Mes')['Crescimento'].mean()

# Criando o gráfico
plt.figure(figsize=(10, 6))
plt.plot(crescimento_mensal.index, crescimento_mensal.values, marker='o', color='b', linestyle='-', linewidth=2, markersize=6)

# Adicionando título e rótulos
plt.title('Evolução do Crescimento - 2020', fontsize=14)
plt.ylim(0, 150)  
plt.xlabel('Mês', fontsize=12)
plt.ylabel('Crescimento', fontsize=12)
plt.xticks(crescimento_mensal.index, ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'])
plt.grid(True)
plt.tight_layout()

# Exibindo o gráfico
plt.show()
