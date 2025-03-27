import pandas as pd
import numpy as np

# Escolho a Soja
# Cresce mais rápido na estação: Primavera / Verão

# 20 amostras por mes

verao2025 = pd.DataFrame([
    #ano  mes estacao  crescimento
    #Janeiro 2025
    [2025, 1, 'Verão',      30],
    [2025, 1, 'Verão',      30],
    [2025, 1, 'Verão',      30],
    [2025, 1, 'Verão',      30],
    [2025, 1, 'Verão',      30],
    [2025, 1, 'Verão',      30],
    [2025, 1, 'Verão',      31],
    [2025, 1, 'Verão',      31],
    [2025, 1, 'Verão',      31],
    [2025, 1, 'Verão',      31],
    [2025, 1, 'Verão',      31],
    [2025, 1, 'Verão',      31],
    [2025, 1, 'Verão',      31],
    [2025, 1, 'Verão',      31],
    [2025, 1, 'Verão',      31],
    [2025, 1, 'Verão',      31],
    [2025, 1, 'Verão',      31],
    [2025, 1, 'Verão',      31],
    [2025, 1, 'Verão',      31],
    [2025, 1, 'Verão',      31],
    #Fevereiro 2025
    [2025, 2, 'Verão',      31],
    [2025, 2, 'Verão',      31],
    [2025, 2, 'Verão',      31],
    [2025, 2, 'Verão',      31],
    [2025, 2, 'Verão',      31],
    [2025, 2, 'Verão',      31],
    [2025, 2, 'Verão',      31],
    [2025, 2, 'Verão',      31],
    [2025, 2, 'Verão',      31],
    [2025, 2, 'Verão',      31],
    [2025, 2, 'Verão',      31],
    [2025, 2, 'Verão',      31],
    [2025, 2, 'Verão',      31],
    [2025, 2, 'Verão',      31],
    [2025, 2, 'Verão',      31],
    [2025, 2, 'Verão',      31],
    [2025, 2, 'Verão',      31],
    [2025, 2, 'Verão',      31],
    [2025, 2, 'Verão',      31],
    [2025, 2, 'Verão',      31],
    #Março 2025
    [2025, 3, 'Verão',      31],
    [2025, 3, 'Verão',      31],
    [2025, 3, 'Verão',      31],
    [2025, 3, 'Verão',      31],
    [2025, 3, 'Verão',      31],
    [2025, 3, 'Verão',      32],
    [2025, 3, 'Verão',      32],
    [2025, 3, 'Verão',      32],
    [2025, 3, 'Verão',      32],
    [2025, 3, 'Verão',      32],
    [2025, 3, 'Verão',      32],
    [2025, 3, 'Verão',      32],
    [2025, 3, 'Verão',      32],
    [2025, 3, 'Verão',      32],
    [2025, 3, 'Verão',      32],
    [2025, 3, 'Verão',      32],
    [2025, 3, 'Verão',      32],
    [2025, 3, 'Verão',      32],
    [2025, 3, 'Verão',      32],
    [2025, 3, 'Verão',      32]


], columns=['Ano', 'Mes', 'Estacao', 'Crescimento']);


outono2025 = pd.DataFrame([
    #ano  mes estacao  crescimento
    # Março 2025
    [2025, 3, 'Outono',      33],
    [2025, 3, 'Outono',      33],
    [2025, 3, 'Outono',      33],
    [2025, 3, 'Outono',      33],
    [2025, 3, 'Outono',      33],
    [2025, 3, 'Outono',      33],
    [2025, 3, 'Outono',      33],
    [2025, 3, 'Outono',      33],
    [2025, 3, 'Outono',      33],
    [2025, 3, 'Outono',      33],
    [2025, 3, 'Outono',      33],
    [2025, 3, 'Outono',      33],
    [2025, 3, 'Outono',      33],
    [2025, 3, 'Outono',      33],
    [2025, 3, 'Outono',      33],
    [2025, 3, 'Outono',      33],
    [2025, 3, 'Outono',      33],
    [2025, 3, 'Outono',      33],
    [2025, 3, 'Outono',      33],
    [2025, 3, 'Outono',      33],
    # Abril 2025
    [2025, 4, 'Outono',      33],
    [2025, 4, 'Outono',      33],
    [2025, 4, 'Outono',      33],
    [2025, 4, 'Outono',      33],
    [2025, 4, 'Outono',      34],
    [2025, 4, 'Outono',      34],
    [2025, 4, 'Outono',      34],
    [2025, 4, 'Outono',      34],
    [2025, 4, 'Outono',      34],
    [2025, 4, 'Outono',      34],
    [2025, 4, 'Outono',      34],
    [2025, 4, 'Outono',      34],
    [2025, 4, 'Outono',      34],
    [2025, 4, 'Outono',      34],
    [2025, 4, 'Outono',      34],
    [2025, 4, 'Outono',      34],
    [2025, 4, 'Outono',      35],
    [2025, 4, 'Outono',      35],
    [2025, 4, 'Outono',      35],
    [2025, 4, 'Outono',      35],
    # Maio 2025
    [2025, 5, 'Outono',      35],
    [2025, 5, 'Outono',      35],
    [2025, 5, 'Outono',      35],
    [2025, 5, 'Outono',      35],
    [2025, 5, 'Outono',      35],
    [2025, 5, 'Outono',      35],
    [2025, 5, 'Outono',      35],
    [2025, 5, 'Outono',      35],
    [2025, 5, 'Outono',      35],
    [2025, 5, 'Outono',      35],
    [2025, 5, 'Outono',      35],
    [2025, 5, 'Outono',      35],
    [2025, 5, 'Outono',      35],
    [2025, 5, 'Outono',      35],
    [2025, 5, 'Outono',      35],
    [2025, 5, 'Outono',      35],
    [2025, 5, 'Outono',      35],
    [2025, 5, 'Outono',      35],
    [2025, 5, 'Outono',      35],
    [2025, 5, 'Outono',      36],
    # Junho  2025
    [2025, 6, 'Outono',      50],
    [2025, 6, 'Outono',      51],
    [2025, 6, 'Outono',      51],
    [2025, 6, 'Outono',      51],
    [2025, 6, 'Outono',      51],
    [2025, 6, 'Outono',      52],
    [2025, 6, 'Outono',      52],
    [2025, 6, 'Outono',      52],
    [2025, 6, 'Outono',      52],
    [2025, 6, 'Outono',      52],
    [2025, 6, 'Outono',      52],
    [2025, 6, 'Outono',      52],
    [2025, 6, 'Outono',      52],
    [2025, 6, 'Outono',      52],
    [2025, 6, 'Outono',      52],
    [2025, 6, 'Outono',      52],
    [2025, 6, 'Outono',      52],
    [2025, 6, 'Outono',      52],
    [2025, 6, 'Outono',      52],
    [2025, 6, 'Outono',      52]

], columns=['Ano', 'Mes', 'Estacao', 'Crescimento']);



inverno2025 = pd.DataFrame([
    #ano  mes estacao  crescimento
    # Junho  2025
    [2025, 6, 'Inverno',      88],
    [2025, 6, 'Inverno',      87],
    [2025, 6, 'Inverno',      86],
    [2025, 6, 'Inverno',      90],
    [2025, 6, 'Inverno',      90],
    [2025, 6, 'Inverno',      90],
    [2025, 6, 'Inverno',      88],
    [2025, 6, 'Inverno',      90],
    [2025, 6, 'Inverno',      90],
    [2025, 6, 'Inverno',      90],
    [2025, 6, 'Inverno',      90],
    [2025, 6, 'Inverno',      89],
    [2025, 6, 'Inverno',      88],
    [2025, 6, 'Inverno',      90],
    [2025, 6, 'Inverno',      90],
    [2025, 6, 'Inverno',      90],
    [2025, 6, 'Inverno',      90],
    [2025, 6, 'Inverno',      90],
    [2025, 6, 'Inverno',      90],
    [2025, 6, 'Inverno',      90],
    # Julho  2025
    [2025, 7, 'Inverno',      95],
    [2025, 7, 'Inverno',      95],
    [2025, 7, 'Inverno',      95],
    [2025, 7, 'Inverno',      95],
    [2025, 7, 'Inverno',      95],
    [2025, 7, 'Inverno',      95],
    [2025, 7, 'Inverno',      95],
    [2025, 7, 'Inverno',      95],
    [2025, 7, 'Inverno',      95],
    [2025, 7, 'Inverno',      95],
    [2025, 7, 'Inverno',      95],
    [2025, 7, 'Inverno',      95],
    [2025, 7, 'Inverno',      95],
    [2025, 7, 'Inverno',      95],
    [2025, 7, 'Inverno',      95],
    [2025, 7, 'Inverno',      95],
    [2025, 7, 'Inverno',      95],
    [2025, 7, 'Inverno',      95],
    [2025, 7, 'Inverno',      95],
    [2025, 7, 'Inverno',      95],
    # Agosto  2025
    [2025, 8, 'Inverno',      98],
    [2025, 8, 'Inverno',      98],
    [2025, 8, 'Inverno',      98],
    [2025, 8, 'Inverno',      98],
    [2025, 8, 'Inverno',      98],
    [2025, 8, 'Inverno',      98],
    [2025, 8, 'Inverno',      98],
    [2025, 8, 'Inverno',      98],
    [2025, 8, 'Inverno',      98],
    [2025, 8, 'Inverno',      98],
    [2025, 8, 'Inverno',      98],
    [2025, 8, 'Inverno',      98],
    [2025, 8, 'Inverno',      98],
    [2025, 8, 'Inverno',      98],
    [2025, 8, 'Inverno',      98],
    [2025, 8, 'Inverno',      98],
    [2025, 8, 'Inverno',      98],
    [2025, 8, 'Inverno',      98],
    [2025, 8, 'Inverno',      98],
    [2025, 8, 'Inverno',      98],
    # Setembro 2025
    [2025, 9, 'Inverno',      98],
    [2025, 9, 'Inverno',      98],
    [2025, 9, 'Inverno',      98],
    [2025, 9, 'Inverno',      98],
    [2025, 9, 'Inverno',      98],
    [2025, 9, 'Inverno',      98],
    [2025, 9, 'Inverno',      98],
    [2025, 9, 'Inverno',      95],
    [2025, 9, 'Inverno',      55],
    [2025, 9, 'Inverno',      55],
    [2025, 9, 'Inverno',      55],
    [2025, 9, 'Inverno',      55],
    [2025, 9, 'Inverno',      55],
    [2025, 9, 'Inverno',      55],
    [2025, 9, 'Inverno',      55],
    [2025, 9, 'Inverno',      55],
    [2025, 9, 'Inverno',      55],
    [2025, 9, 'Inverno',      55],
    [2025, 9, 'Inverno',      55],
    [2025, 9, 'Inverno',      55]

], columns=['Ano', 'Mes', 'Estacao', 'Crescimento']);



primavera2025 = pd.DataFrame([
    #ano  mes estacao  crescimento
    # Setembro 2025
    [2025, 9, 'Primavera',    30],
    [2025, 9, 'Primavera',    30],
    [2025, 9, 'Primavera',    30],
    [2025, 9, 'Primavera',    30],
    [2025, 9, 'Primavera',    30],
    [2025, 9, 'Primavera',    31],
    [2025, 9, 'Primavera',    31],
    [2025, 9, 'Primavera',    31],
    [2025, 9, 'Primavera',    31],
    [2025, 9, 'Primavera',    31],
    [2025, 9, 'Primavera',    31],
    [2025, 9, 'Primavera',    31],
    [2025, 9, 'Primavera',    31],
    [2025, 9, 'Primavera',    31],
    [2025, 9, 'Primavera',    31],
    [2025, 9, 'Primavera',    31],
    [2025, 9, 'Primavera',    31],
    [2025, 9, 'Primavera',    31],
    [2025, 9, 'Primavera',    31],
    [2025, 9, 'Primavera',    31],
    # Outubro 2025
    [2025, 10, 'Primavera',    31],
    [2025, 10, 'Primavera',    31],
    [2025, 10, 'Primavera',    31],
    [2025, 10, 'Primavera',    31],
    [2025, 10, 'Primavera',    31],
    [2025, 10, 'Primavera',    31],
    [2025, 10, 'Primavera',    31],
    [2025, 10, 'Primavera',    31],
    [2025, 10, 'Primavera',    31],
    [2025, 10, 'Primavera',    31],
    [2025, 10, 'Primavera',    32],
    [2025, 10, 'Primavera',    32],
    [2025, 10, 'Primavera',    32],
    [2025, 10, 'Primavera',    32],
    [2025, 10, 'Primavera',    32],
    [2025, 10, 'Primavera',    32],
    [2025, 10, 'Primavera',    32],
    [2025, 10, 'Primavera',    32],
    [2025, 10, 'Primavera',    32],
    [2025, 10, 'Primavera',    32],
    # Novembro 2025
    [2025, 11, 'Primavera',    32],
    [2025, 11, 'Primavera',    32],
    [2025, 11, 'Primavera',    32],
    [2025, 11, 'Primavera',    32],
    [2025, 11, 'Primavera',    32],
    [2025, 11, 'Primavera',    32],
    [2025, 11, 'Primavera',    32],
    [2025, 11, 'Primavera',    32],
    [2025, 11, 'Primavera',    32],
    [2025, 11, 'Primavera',    32],
    [2025, 11, 'Primavera',    32],
    [2025, 11, 'Primavera',    33],
    [2025, 11, 'Primavera',    33],
    [2025, 11, 'Primavera',    33],
    [2025, 11, 'Primavera',    33],
    [2025, 11, 'Primavera',    33],
    [2025, 11, 'Primavera',    33],
    [2025, 11, 'Primavera',    33],
    [2025, 11, 'Primavera',    33],
    [2025, 11, 'Primavera',    33],
    # Dezembro 2025
    [2025, 12, 'Primavera',    33],
    [2025, 12, 'Primavera',    33],
    [2025, 12, 'Primavera',    33],
    [2025, 12, 'Primavera',    33],
    [2025, 12, 'Primavera',    34],
    [2025, 12, 'Primavera',    34],
    [2025, 12, 'Primavera',    34],
    [2025, 12, 'Primavera',    34],
    [2025, 12, 'Primavera',    34],
    [2025, 12, 'Primavera',    34],
    [2025, 12, 'Primavera',    34],
    [2025, 12, 'Primavera',    34],
    [2025, 12, 'Primavera',    34],
    [2025, 12, 'Primavera',    34],
    [2025, 12, 'Primavera',    34],
    [2025, 12, 'Primavera',    34],
    [2025, 12, 'Primavera',    34],
    [2025, 12, 'Primavera',    34],
    [2025, 12, 'Primavera',    34],
    [2025, 12, 'Primavera',    34]

], columns=['Ano', 'Mes', 'Estacao', 'Crescimento']);


# Juntando os datasets das estações de 2025 para ter um dataset completo

# Lista contendo os quatro DataFrames
datasets_juntar = [verao2025, outono2025, inverno2025, primavera2025]

# Concatenando os DataFrames na vertical (mesmo número de colunas)
dataset2025 = pd.concat(datasets_juntar, ignore_index=True)


# Conferindo o padrão pra ver se ta ficando do jeito que eu quero
import matplotlib.pyplot as plt
import pandas as pd

#dataset2025['Crescimento'] = dataset2025['Crescimento'] - 20;

print( dataset2025.describe() )

# Filtrando os dados de 2020
dados_2025 = dataset2025[dataset2025['Ano'] == 2025]

dataset2025.to_csv('datasets/soja2025.csv', sep=';', index=False)

# Agora vamos agrupar os dados por mês e somar o Crescimento
crescimento_mensal = dados_2025.groupby('Mes')['Crescimento'].mean()

# Criando o gráfico
plt.figure(figsize=(10, 6))
plt.plot(crescimento_mensal.index, crescimento_mensal.values, marker='o', color='b', linestyle='-', linewidth=2, markersize=6)

# Adicionando título e rótulos
plt.title('Evolução do Crescimento - 2025', fontsize=14)
plt.ylim(0, 150)  
plt.xlabel('Mês', fontsize=12)
plt.ylabel('Crescimento', fontsize=12)
plt.xticks(crescimento_mensal.index, ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'])
plt.grid(True)
plt.tight_layout()

# Exibindo o gráfico
plt.show()