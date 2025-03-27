import pandas as pd
import numpy as np

# Escolho a Soja
# Cresce mais rápido na estação: Primavera / Verão

# 20 amostras por mes

verao2024 = pd.DataFrame([
    #ano  mes estacao  crescimento
    #Janeiro 2024
    [2024, 1, 'Verão',      42],
    [2024, 1, 'Verão',      42],
    [2024, 1, 'Verão',      42],
    [2024, 1, 'Verão',      42],
    [2024, 1, 'Verão',      42],
    [2024, 1, 'Verão',      42],
    [2024, 1, 'Verão',      42],
    [2024, 1, 'Verão',      42],
    [2024, 1, 'Verão',      42],
    [2024, 1, 'Verão',      43],
    [2024, 1, 'Verão',      43],
    [2024, 1, 'Verão',      43],
    [2024, 1, 'Verão',      43],
    [2024, 1, 'Verão',      43],
    [2024, 1, 'Verão',      43],
    [2024, 1, 'Verão',      43],
    [2024, 1, 'Verão',      43],
    [2024, 1, 'Verão',      43],
    [2024, 1, 'Verão',      43],
    [2024, 1, 'Verão',      43],
    #Fevereiro 2024
    [2024, 2, 'Verão',      43],
    [2024, 2, 'Verão',      43],
    [2024, 2, 'Verão',      43],
    [2024, 2, 'Verão',      43],
    [2024, 2, 'Verão',      43],
    [2024, 2, 'Verão',      43],
    [2024, 2, 'Verão',      43],
    [2024, 2, 'Verão',      43],
    [2024, 2, 'Verão',      43],
    [2024, 2, 'Verão',      43],
    [2024, 2, 'Verão',      43],
    [2024, 2, 'Verão',      43],
    [2024, 2, 'Verão',      43],
    [2024, 2, 'Verão',      43],
    [2024, 2, 'Verão',      43],
    [2024, 2, 'Verão',      43],
    [2024, 2, 'Verão',      43],
    [2024, 2, 'Verão',      43],
    [2024, 2, 'Verão',      43],
    [2024, 2, 'Verão',      43],
    #Março 2024
    [2024, 3, 'Verão',      45],
    [2024, 3, 'Verão',      45],
    [2024, 3, 'Verão',      45],
    [2024, 3, 'Verão',      45],
    [2024, 3, 'Verão',      45],
    [2024, 3, 'Verão',      45],
    [2024, 3, 'Verão',      45],
    [2024, 3, 'Verão',      45],
    [2024, 3, 'Verão',      45],
    [2024, 3, 'Verão',      45],
    [2024, 3, 'Verão',      45],
    [2024, 3, 'Verão',      45],
    [2024, 3, 'Verão',      45],
    [2024, 3, 'Verão',      45],
    [2024, 3, 'Verão',      45],
    [2024, 3, 'Verão',      45],
    [2024, 3, 'Verão',      45],
    [2024, 3, 'Verão',      45],
    [2024, 3, 'Verão',      45],
    [2024, 3, 'Verão',      45]


], columns=['Ano', 'Mes', 'Estacao', 'Crescimento']);


outono2024 = pd.DataFrame([
    #ano  mes estacao  crescimento
    # Março 2024
    [2024, 3, 'Outono',      45],
    [2024, 3, 'Outono',      45],
    [2024, 3, 'Outono',      45],
    [2024, 3, 'Outono',      45],
    [2024, 3, 'Outono',      45],
    [2024, 3, 'Outono',      45],
    [2024, 3, 'Outono',      45],
    [2024, 3, 'Outono',      45],
    [2024, 3, 'Outono',      45],
    [2024, 3, 'Outono',      45],
    [2024, 3, 'Outono',      45],
    [2024, 3, 'Outono',      45],
    [2024, 3, 'Outono',      45],
    [2024, 3, 'Outono',      45],
    [2024, 3, 'Outono',      45],
    [2024, 3, 'Outono',      45],
    [2024, 3, 'Outono',      45],
    [2024, 3, 'Outono',      46],
    [2024, 3, 'Outono',      46],
    [2024, 3, 'Outono',      46],
    # Abril 2024
    [2024, 4, 'Outono',      46],
    [2024, 4, 'Outono',      46],
    [2024, 4, 'Outono',      46],
    [2024, 4, 'Outono',      46],
    [2024, 4, 'Outono',      46],
    [2024, 4, 'Outono',      46],
    [2024, 4, 'Outono',      46],
    [2024, 4, 'Outono',      46],
    [2024, 4, 'Outono',      46],
    [2024, 4, 'Outono',      46],
    [2024, 4, 'Outono',      46],
    [2024, 4, 'Outono',      46],
    [2024, 4, 'Outono',      46],
    [2024, 4, 'Outono',      46],
    [2024, 4, 'Outono',      46],
    [2024, 4, 'Outono',      46],
    [2024, 4, 'Outono',      46],
    [2024, 4, 'Outono',      46],
    [2024, 4, 'Outono',      46],
    [2024, 4, 'Outono',      46],
    # Maio 2024
    [2024, 5, 'Outono',      46],
    [2024, 5, 'Outono',      46],
    [2024, 5, 'Outono',      46],
    [2024, 5, 'Outono',      46],
    [2024, 5, 'Outono',      46],
    [2024, 5, 'Outono',      46],
    [2024, 5, 'Outono',      46],
    [2024, 5, 'Outono',      46],
    [2024, 5, 'Outono',      46],
    [2024, 5, 'Outono',      46],
    [2024, 5, 'Outono',      46],
    [2024, 5, 'Outono',      46],
    [2024, 5, 'Outono',      46],
    [2024, 5, 'Outono',      46],
    [2024, 5, 'Outono',      46],
    [2024, 5, 'Outono',      46],
    [2024, 5, 'Outono',      46],
    [2024, 5, 'Outono',      46],
    [2024, 5, 'Outono',      46],
    [2024, 5, 'Outono',      46],
    # Junho  2024
    [2024, 6, 'Outono',      59],
    [2024, 6, 'Outono',      58],
    [2024, 6, 'Outono',      59],
    [2024, 6, 'Outono',      60],
    [2024, 6, 'Outono',      60],
    [2024, 6, 'Outono',      60],
    [2024, 6, 'Outono',      60],
    [2024, 6, 'Outono',      60],
    [2024, 6, 'Outono',      60],
    [2024, 6, 'Outono',      60],
    [2024, 6, 'Outono',      60],
    [2024, 6, 'Outono',      60],
    [2024, 6, 'Outono',      60],
    [2024, 6, 'Outono',      60],
    [2024, 6, 'Outono',      62],
    [2024, 6, 'Outono',      61],
    [2024, 6, 'Outono',      65],
    [2024, 6, 'Outono',      65],
    [2024, 6, 'Outono',      65],
    [2024, 6, 'Outono',      65]

], columns=['Ano', 'Mes', 'Estacao', 'Crescimento']);



inverno2024 = pd.DataFrame([
    #ano  mes estacao  crescimento
    # Junho  2024
    [2024, 6, 'Inverno',      120],
    [2024, 6, 'Inverno',      109],
    [2024, 6, 'Inverno',      110],
    [2024, 6, 'Inverno',      107],
    [2024, 6, 'Inverno',      109],
    [2024, 6, 'Inverno',      120],
    [2024, 6, 'Inverno',      122],
    [2024, 6, 'Inverno',      125],
    [2024, 6, 'Inverno',      115],
    [2024, 6, 'Inverno',      119],
    [2024, 6, 'Inverno',      118],
    [2024, 6, 'Inverno',      112],
    [2024, 6, 'Inverno',      111],
    [2024, 6, 'Inverno',      113],
    [2024, 6, 'Inverno',      115],
    [2024, 6, 'Inverno',      120],
    [2024, 6, 'Inverno',      119],
    [2024, 6, 'Inverno',      111],
    [2024, 6, 'Inverno',      119],
    [2024, 6, 'Inverno',      120],
    # Julho  2024
    [2024, 7, 'Inverno',      125],
    [2024, 7, 'Inverno',      115],
    [2024, 7, 'Inverno',      115],
    [2024, 7, 'Inverno',      115],
    [2024, 7, 'Inverno',      118],
    [2024, 7, 'Inverno',      125],
    [2024, 7, 'Inverno',      118],
    [2024, 7, 'Inverno',      119],
    [2024, 7, 'Inverno',      119],
    [2024, 7, 'Inverno',      120],
    [2024, 7, 'Inverno',      125],
    [2024, 7, 'Inverno',      125],
    [2024, 4, 'Inverno',      125],
    [2024, 7, 'Inverno',      125],
    [2024, 7, 'Inverno',      115],
    [2024, 7, 'Inverno',      115],
    [2024, 7, 'Inverno',      118],
    [2024, 7, 'Inverno',      117],
    [2024, 7, 'Inverno',      122],
    [2024, 7, 'Inverno',      125],
    # Agosto  2024
    [2024, 8, 'Inverno',      140],
    [2024, 8, 'Inverno',      135],
    [2024, 8, 'Inverno',      135],
    [2024, 8, 'Inverno',      132],
    [2024, 8, 'Inverno',      138],
    [2024, 8, 'Inverno',      137],
    [2024, 8, 'Inverno',      140],
    [2024, 8, 'Inverno',      138],
    [2024, 8, 'Inverno',      132],
    [2024, 8, 'Inverno',      134],
    [2024, 8, 'Inverno',      131],
    [2024, 8, 'Inverno',      134],
    [2024, 8, 'Inverno',      136],
    [2024, 8, 'Inverno',      137],
    [2024, 8, 'Inverno',      138],
    [2024, 8, 'Inverno',      139],
    [2024, 8, 'Inverno',      132],
    [2024, 8, 'Inverno',      134],
    [2024, 8, 'Inverno',      140],
    [2024, 8, 'Inverno',      140],
    # Setembro 2024
    [2024, 9, 'Inverno',      140],
    [2024, 9, 'Inverno',      135],
    [2024, 9, 'Inverno',      135],
    [2024, 9, 'Inverno',      132],
    [2024, 9, 'Inverno',      138],
    [2024, 9, 'Inverno',      137],
    [2024, 9, 'Inverno',      140],
    [2024, 9, 'Inverno',      95],
    [2024, 9, 'Inverno',      95],
    [2024, 9, 'Inverno',      95],
    [2024, 9, 'Inverno',      95],
    [2024, 9, 'Inverno',      95],
    [2024, 9, 'Inverno',      95],
    [2024, 9, 'Inverno',      95],
    [2024, 9, 'Inverno',      95],
    [2024, 9, 'Inverno',      95],
    [2024, 9, 'Inverno',      95],
    [2024, 9, 'Inverno',      95],
    [2024, 9, 'Inverno',      95],
    [2024, 9, 'Inverno',      95]

], columns=['Ano', 'Mes', 'Estacao', 'Crescimento']);



primavera2024 = pd.DataFrame([
    #ano  mes estacao  crescimento
    # Setembro 2024
    [2024, 9, 'Primavera',    46],
    [2024, 9, 'Primavera',    48],
    [2024, 9, 'Primavera',    45],
    [2024, 9, 'Primavera',    44],
    [2024, 9, 'Primavera',    44],
    [2024, 9, 'Primavera',    45],
    [2024, 9, 'Primavera',    44],
    [2024, 9, 'Primavera',    43],
    [2024, 9, 'Primavera',    44],
    [2024, 9, 'Primavera',    43],
    [2024, 9, 'Primavera',    44],
    [2024, 9, 'Primavera',    42],
    [2024, 9, 'Primavera',    41],
    [2024, 9, 'Primavera',    41],
    [2024, 9, 'Primavera',    41],
    [2024, 9, 'Primavera',    41],
    [2024, 9, 'Primavera',    41],
    [2024, 9, 'Primavera',    41],
    [2024, 9, 'Primavera',    41],
    [2024, 9, 'Primavera',    41],
    # Outubro 2024
    [2024, 10, 'Primavera',    40],
    [2024, 10, 'Primavera',    43],
    [2024, 10, 'Primavera',    40],
    [2024, 10, 'Primavera',    41],
    [2024, 10, 'Primavera',    40],
    [2024, 10, 'Primavera',    40],
    [2024, 10, 'Primavera',    40],
    [2024, 10, 'Primavera',    40],
    [2024, 10, 'Primavera',    40],
    [2024, 10, 'Primavera',    40],
    [2024, 10, 'Primavera',    40],
    [2024, 10, 'Primavera',    40],
    [2024, 10, 'Primavera',    40],
    [2024, 10, 'Primavera',    40],
    [2024, 10, 'Primavera',    40],
    [2024, 10, 'Primavera',    40],
    [2024, 10, 'Primavera',    40],
    [2024, 10, 'Primavera',    40],
    [2024, 10, 'Primavera',    40],
    [2024, 10, 'Primavera',    40],
    # Novembro 2024
    [2024, 11, 'Primavera',    40],
    [2024, 11, 'Primavera',    43],
    [2024, 11, 'Primavera',    40],
    [2024, 11, 'Primavera',    41],
    [2024, 11, 'Primavera',    40],
    [2024, 11, 'Primavera',    40],
    [2024, 11, 'Primavera',    40],
    [2024, 11, 'Primavera',    40],
    [2024, 11, 'Primavera',    40],
    [2024, 11, 'Primavera',    40],
    [2024, 11, 'Primavera',    40],
    [2024, 11, 'Primavera',    40],
    [2024, 11, 'Primavera',    40],
    [2024, 11, 'Primavera',    40],
    [2024, 11, 'Primavera',    40],
    [2024, 11, 'Primavera',    40],
    [2024, 11, 'Primavera',    40],
    [2024, 11, 'Primavera',    40],
    [2024, 11, 'Primavera',    40],
    [2024, 11, 'Primavera',    40],
    # Dezembro 2024
    [2024, 12, 'Primavera',    45],
    [2024, 12, 'Primavera',    47],
    [2024, 12, 'Primavera',    44],
    [2024, 12, 'Primavera',    45],
    [2024, 12, 'Primavera',    44],
    [2024, 12, 'Primavera',    42],
    [2024, 12, 'Primavera',    45],
    [2024, 12, 'Primavera',    45],
    [2024, 12, 'Primavera',    44],
    [2024, 12, 'Primavera',    45],
    [2024, 12, 'Primavera',    44],
    [2024, 12, 'Primavera',    43],
    [2024, 12, 'Primavera',    44],
    [2024, 12, 'Primavera',    45],
    [2024, 12, 'Primavera',    44],
    [2024, 12, 'Primavera',    46],
    [2024, 12, 'Primavera',    43],
    [2024, 12, 'Primavera',    44],
    [2024, 12, 'Primavera',    43],
    [2024, 12, 'Primavera',    42]

], columns=['Ano', 'Mes', 'Estacao', 'Crescimento']);


# Juntando os datasets das estações de 2024 para ter um dataset completo

# Lista contendo os quatro DataFrames
datasets_juntar = [verao2024, outono2024, inverno2024, primavera2024]

# Concatenando os DataFrames na vertical (mesmo número de colunas)
dataset2024 = pd.concat(datasets_juntar, ignore_index=True)


# Conferindo o padrão pra ver se ta ficando do jeito que eu quero
import matplotlib.pyplot as plt
import pandas as pd

#dataset2024['Crescimento'] = dataset2024['Crescimento'] - 10;

print( dataset2024.describe() )

# Filtrando os dados de 2024
dados_2024 = dataset2024[dataset2024['Ano'] == 2024]

dataset2024.to_csv('datasets/soja2024.csv', sep=';', index=False)

# Agora vamos agrupar os dados por mês e somar o Crescimento
crescimento_mensal = dados_2024.groupby('Mes')['Crescimento'].mean()

# Criando o gráfico
plt.figure(figsize=(10, 6))
plt.plot(crescimento_mensal.index, crescimento_mensal.values, marker='o', color='b', linestyle='-', linewidth=2, markersize=6)

# Adicionando título e rótulos
plt.title('Evolução do Crescimento - 2024', fontsize=14)
plt.ylim(0, 150) 
plt.xlabel('Mês', fontsize=12)
plt.ylabel('Crescimento', fontsize=12)
plt.xticks(crescimento_mensal.index, ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'])
plt.grid(True)
plt.tight_layout()

# Exibindo o gráfico
plt.show()