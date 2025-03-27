import pandas as pd
import numpy as np

# Escolho a Soja
# Cresce mais rápido na estação: Primavera / Verão

# 20 amostras por mes

verao2021 = pd.DataFrame([
    #ano  mes estacao  crescimento
    #Janeiro 2021
    [2021, 1, 'Verão',      30],
    [2021, 1, 'Verão',      32],
    [2021, 1, 'Verão',      32],
    [2021, 1, 'Verão',      32],
    [2021, 1, 'Verão',      30],
    [2021, 1, 'Verão',      30],
    [2021, 1, 'Verão',      31],
    [2021, 1, 'Verão',      31],
    [2021, 1, 'Verão',      30],
    [2021, 1, 'Verão',      30],
    [2021, 1, 'Verão',      31],
    [2021, 1, 'Verão',      32],
    [2021, 1, 'Verão',      31],
    [2021, 1, 'Verão',      31],
    [2021, 1, 'Verão',      31],
    [2021, 1, 'Verão',      30],
    [2021, 1, 'Verão',      32],
    [2021, 1, 'Verão',      31],
    [2021, 1, 'Verão',      32],
    [2021, 1, 'Verão',      31],
    #Fevereiro 2021
    [2021, 2, 'Verão',      33],
    [2021, 2, 'Verão',      33],
    [2021, 2, 'Verão',      33],
    [2021, 2, 'Verão',      32],
    [2021, 2, 'Verão',      33],
    [2021, 2, 'Verão',      33],
    [2021, 2, 'Verão',      31],
    [2021, 2, 'Verão',      31],
    [2021, 2, 'Verão',      32],
    [2021, 2, 'Verão',      30],
    [2021, 2, 'Verão',      31],
    [2021, 2, 'Verão',      33],
    [2021, 2, 'Verão',      32],
    [2021, 2, 'Verão',      31],
    [2021, 2, 'Verão',      31],
    [2021, 2, 'Verão',      30],
    [2021, 2, 'Verão',      33],
    [2021, 2, 'Verão',      31],
    [2021, 2, 'Verão',      33],
    [2021, 2, 'Verão',      31],
    #Março 2021
    [2021, 3, 'Verão',      34],
    [2021, 3, 'Verão',      32],
    [2021, 3, 'Verão',      35],
    [2021, 3, 'Verão',      32],
    [2021, 3, 'Verão',      32],
    [2021, 3, 'Verão',      34],
    [2021, 3, 'Verão',      32],
    [2021, 3, 'Verão',      31],
    [2021, 3, 'Verão',      34],
    [2021, 3, 'Verão',      31],
    [2021, 3, 'Verão',      37],
    [2021, 3, 'Verão',      37],
    [2021, 3, 'Verão',      38],
    [2021, 3, 'Verão',      37],
    [2021, 3, 'Verão',      35],
    [2021, 3, 'Verão',      37],
    [2021, 3, 'Verão',      37],
    [2021, 3, 'Verão',      35],
    [2021, 3, 'Verão',      37],
    [2021, 3, 'Verão',      38]


], columns=['Ano', 'Mes', 'Estacao', 'Crescimento']);


outono2021 = pd.DataFrame([
    #ano  mes estacao  crescimento
    # Março 2021
    [2021, 3, 'Outono',      38],
    [2021, 3, 'Outono',      36],
    [2021, 3, 'Outono',      35],
    [2021, 3, 'Outono',      35],
    [2021, 3, 'Outono',      35],
    [2021, 3, 'Outono',      35],
    [2021, 3, 'Outono',      34],
    [2021, 3, 'Outono',      35],
    [2021, 3, 'Outono',      36],
    [2021, 3, 'Outono',      34],
    [2021, 3, 'Outono',      35],
    [2021, 3, 'Outono',      34],
    [2021, 3, 'Outono',      35],
    [2021, 3, 'Outono',      35],
    [2021, 3, 'Outono',      35],
    [2021, 3, 'Outono',      35],
    [2021, 3, 'Outono',      34],
    [2021, 3, 'Outono',      36],
    [2021, 3, 'Outono',      34],
    [2021, 3, 'Outono',      36],
    # Abril 2021
    [2021, 4, 'Outono',      38],
    [2021, 4, 'Outono',      38],
    [2021, 4, 'Outono',      36],
    [2021, 4, 'Outono',      38],
    [2021, 4, 'Outono',      35],
    [2021, 4, 'Outono',      37],
    [2021, 4, 'Outono',      39],
    [2021, 4, 'Outono',      38],
    [2021, 4, 'Outono',      37],
    [2021, 4, 'Outono',      38],
    [2021, 4, 'Outono',      39],
    [2021, 4, 'Outono',      38],
    [2021, 4, 'Outono',      37],
    [2021, 4, 'Outono',      36],
    [2021, 4, 'Outono',      36],
    [2021, 4, 'Outono',      39],
    [2021, 4, 'Outono',      35],
    [2021, 4, 'Outono',      39],
    [2021, 4, 'Outono',      37],
    [2021, 4, 'Outono',      36],
    # Maio 2021
    [2021, 5, 'Outono',      38],
    [2021, 5, 'Outono',      38],
    [2021, 5, 'Outono',      36],
    [2021, 5, 'Outono',      38],
    [2021, 5, 'Outono',      35],
    [2021, 5, 'Outono',      37],
    [2021, 5, 'Outono',      39],
    [2021, 5, 'Outono',      38],
    [2021, 5, 'Outono',      37],
    [2021, 5, 'Outono',      38],
    [2021, 5, 'Outono',      39],
    [2021, 5, 'Outono',      38],
    [2021, 5, 'Outono',      37],
    [2021, 5, 'Outono',      36],
    [2021, 5, 'Outono',      36],
    [2021, 5, 'Outono',      39],
    [2021, 5, 'Outono',      35],
    [2021, 5, 'Outono',      39],
    [2021, 5, 'Outono',      37],
    [2021, 5, 'Outono',      36],
    # Junho  2021
    [2021, 6, 'Outono',      55],
    [2021, 6, 'Outono',      58],
    [2021, 6, 'Outono',      57],
    [2021, 6, 'Outono',      58],
    [2021, 6, 'Outono',      57],
    [2021, 6, 'Outono',      59],
    [2021, 6, 'Outono',      55],
    [2021, 6, 'Outono',      55],
    [2021, 6, 'Outono',      55],
    [2021, 6, 'Outono',      55],
    [2021, 6, 'Outono',      55],
    [2021, 6, 'Outono',      55],
    [2021, 6, 'Outono',      55],
    [2021, 6, 'Outono',      55],
    [2021, 6, 'Outono',      55],
    [2021, 6, 'Outono',      55],
    [2021, 6, 'Outono',      55],
    [2021, 6, 'Outono',      55],
    [2021, 6, 'Outono',      55],
    [2021, 6, 'Outono',      55]

], columns=['Ano', 'Mes', 'Estacao', 'Crescimento']);



inverno2021 = pd.DataFrame([
    #ano  mes estacao  crescimento
    # Junho  2021
    [2021, 6, 'Inverno',      88],
    [2021, 6, 'Inverno',      87],
    [2021, 6, 'Inverno',      86],
    [2021, 6, 'Inverno',      90],
    [2021, 6, 'Inverno',      90],
    [2021, 6, 'Inverno',      90],
    [2021, 6, 'Inverno',      88],
    [2021, 6, 'Inverno',      90],
    [2021, 6, 'Inverno',      90],
    [2021, 6, 'Inverno',      90],
    [2021, 6, 'Inverno',      90],
    [2021, 6, 'Inverno',      89],
    [2021, 6, 'Inverno',      88],
    [2021, 6, 'Inverno',      90],
    [2021, 6, 'Inverno',      90],
    [2021, 6, 'Inverno',      90],
    [2021, 6, 'Inverno',      90],
    [2021, 6, 'Inverno',      90],
    [2021, 6, 'Inverno',      90],
    [2021, 6, 'Inverno',      90],
    # Julho  2021
    [2021, 7, 'Inverno',      95],
    [2021, 7, 'Inverno',      95],
    [2021, 7, 'Inverno',      95],
    [2021, 7, 'Inverno',      95],
    [2021, 7, 'Inverno',      95],
    [2021, 7, 'Inverno',      95],
    [2021, 7, 'Inverno',      95],
    [2021, 7, 'Inverno',      95],
    [2021, 7, 'Inverno',      95],
    [2021, 7, 'Inverno',      95],
    [2021, 7, 'Inverno',      95],
    [2021, 7, 'Inverno',      95],
    [2021, 7, 'Inverno',      95],
    [2021, 7, 'Inverno',      95],
    [2021, 7, 'Inverno',      95],
    [2021, 7, 'Inverno',      95],
    [2021, 7, 'Inverno',      95],
    [2021, 7, 'Inverno',      95],
    [2021, 7, 'Inverno',      95],
    [2021, 7, 'Inverno',      95],
    # Agosto  2021
    [2021, 8, 'Inverno',      98],
    [2021, 8, 'Inverno',      98],
    [2021, 8, 'Inverno',      98],
    [2021, 8, 'Inverno',      98],
    [2021, 8, 'Inverno',      98],
    [2021, 8, 'Inverno',      98],
    [2021, 8, 'Inverno',      98],
    [2021, 8, 'Inverno',      98],
    [2021, 8, 'Inverno',      98],
    [2021, 8, 'Inverno',      98],
    [2021, 8, 'Inverno',      98],
    [2021, 8, 'Inverno',      98],
    [2021, 8, 'Inverno',      98],
    [2021, 8, 'Inverno',      98],
    [2021, 8, 'Inverno',      98],
    [2021, 8, 'Inverno',      98],
    [2021, 8, 'Inverno',      98],
    [2021, 8, 'Inverno',      98],
    [2021, 8, 'Inverno',      98],
    [2021, 8, 'Inverno',      98],
    # Setembro 2021
    [2021, 9, 'Inverno',      98],
    [2021, 9, 'Inverno',      98],
    [2021, 9, 'Inverno',      98],
    [2021, 9, 'Inverno',      98],
    [2021, 9, 'Inverno',      98],
    [2021, 9, 'Inverno',      98],
    [2021, 9, 'Inverno',      98],
    [2021, 9, 'Inverno',      95],
    [2021, 9, 'Inverno',      55],
    [2021, 9, 'Inverno',      55],
    [2021, 9, 'Inverno',      55],
    [2021, 9, 'Inverno',      55],
    [2021, 9, 'Inverno',      55],
    [2021, 9, 'Inverno',      55],
    [2021, 9, 'Inverno',      55],
    [2021, 9, 'Inverno',      55],
    [2021, 9, 'Inverno',      55],
    [2021, 9, 'Inverno',      55],
    [2021, 9, 'Inverno',      55],
    [2021, 9, 'Inverno',      55]

], columns=['Ano', 'Mes', 'Estacao', 'Crescimento']);



primavera2021 = pd.DataFrame([
    #ano  mes estacao  crescimento
    # Setembro 2021
    [2021, 9, 'Primavera',    36],
    [2021, 9, 'Primavera',    35],
    [2021, 9, 'Primavera',    35],
    [2021, 9, 'Primavera',    35],
    [2021, 9, 'Primavera',    34],
    [2021, 9, 'Primavera',    35],
    [2021, 9, 'Primavera',    36],
    [2021, 9, 'Primavera',    37],
    [2021, 9, 'Primavera',    35],
    [2021, 9, 'Primavera',    36],
    [2021, 9, 'Primavera',    37],
    [2021, 9, 'Primavera',    35],
    [2021, 9, 'Primavera',    35],
    [2021, 9, 'Primavera',    30],
    [2021, 9, 'Primavera',    35],
    [2021, 9, 'Primavera',    32],
    [2021, 9, 'Primavera',    31],
    [2021, 9, 'Primavera',    33],
    [2021, 9, 'Primavera',    32],
    [2021, 9, 'Primavera',    30],
    # Outubro 2021
    [2021, 10, 'Primavera',    30],
    [2021, 10, 'Primavera',    31],
    [2021, 10, 'Primavera',    32],
    [2021, 10, 'Primavera',    33],
    [2021, 10, 'Primavera',    32],
    [2021, 10, 'Primavera',    32],
    [2021, 10, 'Primavera',    31],
    [2021, 10, 'Primavera',    33],
    [2021, 10, 'Primavera',    32],
    [2021, 10, 'Primavera',    33],
    [2021, 10, 'Primavera',    33],
    [2021, 10, 'Primavera',    33],
    [2021, 10, 'Primavera',    32],
    [2021, 10, 'Primavera',    31],
    [2021, 10, 'Primavera',    32],
    [2021, 10, 'Primavera',    32],
    [2021, 10, 'Primavera',    32],
    [2021, 10, 'Primavera',    32],
    [2021, 10, 'Primavera',    31],
    [2021, 10, 'Primavera',    35],
    # Novembro 2021
    [2021, 11, 'Primavera',    35],
    [2021, 11, 'Primavera',    35],
    [2021, 11, 'Primavera',    35],
    [2021, 11, 'Primavera',    35],
    [2021, 11, 'Primavera',    35],
    [2021, 11, 'Primavera',    35],
    [2021, 11, 'Primavera',    35],
    [2021, 11, 'Primavera',    35],
    [2021, 11, 'Primavera',    35],
    [2021, 11, 'Primavera',    35],
    [2021, 11, 'Primavera',    35],
    [2021, 11, 'Primavera',    35],
    [2021, 11, 'Primavera',    35],
    [2021, 11, 'Primavera',    35],
    [2021, 11, 'Primavera',    35],
    [2021, 11, 'Primavera',    35],
    [2021, 11, 'Primavera',    35],
    [2021, 11, 'Primavera',    35],
    [2021, 11, 'Primavera',    35],
    [2021, 11, 'Primavera',    35],
    # Dezembro 2021
    [2021, 12, 'Primavera',    35],
    [2021, 12, 'Primavera',    35],
    [2021, 12, 'Primavera',    35],
    [2021, 12, 'Primavera',    35],
    [2021, 12, 'Primavera',    35],
    [2021, 12, 'Primavera',    35],
    [2021, 12, 'Primavera',    35],
    [2021, 12, 'Primavera',    35],
    [2021, 12, 'Primavera',    35],
    [2021, 12, 'Primavera',    35],
    [2021, 12, 'Primavera',    35],
    [2021, 12, 'Primavera',    35],
    [2021, 12, 'Primavera',    35],
    [2021, 12, 'Primavera',    35],
    [2021, 12, 'Primavera',    35],
    [2021, 12, 'Primavera',    35],
    [2021, 12, 'Primavera',    35],
    [2021, 12, 'Primavera',    35],
    [2021, 12, 'Primavera',    35],
    [2021, 12, 'Primavera',    35]

], columns=['Ano', 'Mes', 'Estacao', 'Crescimento']);


# Juntando os datasets das estações de 2021 para ter um dataset completo

# Lista contendo os quatro DataFrames
datasets_juntar = [verao2021, outono2021, inverno2021, primavera2021]

# Concatenando os DataFrames na vertical (mesmo número de colunas)
dataset2021 = pd.concat(datasets_juntar, ignore_index=True)

# Conferindo o padrão pra ver se ta ficando do jeito que eu quero
import matplotlib.pyplot as plt
import pandas as pd

#dataset2021['Crescimento'] = dataset2021['Crescimento'] - 20;

print( dataset2021.describe() )

# Filtrando os dados de 2020
dados_2021 = dataset2021[dataset2021['Ano'] == 2021]

dataset2021.to_csv('datasets/soja2021.csv', sep=';', index=False)

# Agora vamos agrupar os dados por mês e somar o Crescimento
crescimento_mensal = dados_2021.groupby('Mes')['Crescimento'].mean()

# Criando o gráfico
plt.figure(figsize=(10, 6))
plt.plot(crescimento_mensal.index, crescimento_mensal.values, marker='o', color='b', linestyle='-', linewidth=2, markersize=6)

# Adicionando título e rótulos
plt.title('Evolução do Crescimento - 2021', fontsize=14)
plt.ylim(0, 150) 
plt.xlabel('Mês', fontsize=12)
plt.ylabel('Crescimento', fontsize=12)
plt.xticks(crescimento_mensal.index, ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'])
plt.grid(True)
plt.tight_layout()

# Exibindo o gráfico
plt.show()