import pandas as pd
import numpy as np

# Ler os datasets
dataset2020 = pd.read_csv('datasets/soja2020.csv', sep=';')
dataset2021 = pd.read_csv('datasets/soja2021.csv', sep=';')
dataset2022 = pd.read_csv('datasets/soja2022.csv', sep=';')
dataset2023 = pd.read_csv('datasets/soja2023.csv', sep=';')
dataset2024 = pd.read_csv('datasets/soja2024.csv', sep=';')
dataset2025 = pd.read_csv('datasets/soja2025.csv', sep=';')

# Lista contendo tudo
datasets_juntar = [dataset2020, dataset2021, dataset2022, dataset2023, dataset2024, dataset2025]

dataset_completo = pd.concat(datasets_juntar, ignore_index=True)

dataset_completo.to_csv('datasets/crescimento-soja.csv', sep=';', index=False)

print( dataset_completo.describe() )

# Conferindo o padrão pra ver se ta ficando do jeito que eu quero
import matplotlib.pyplot as plt
import pandas as pd

"""
Média do Crescimento em Geral de 2020 a 2025, de Janeiro a Dezembro

# Agora vamos agrupar os dados por mês e somar o Crescimento
crescimento_mensal = dataset_completo.groupby('Mes')['Crescimento'].mean()

# Criando o gráfico
plt.figure(figsize=(10, 6))
plt.plot(crescimento_mensal.index, crescimento_mensal.values, marker='o', color='b', linestyle='-', linewidth=2, markersize=6)

# Adicionando título e rótulos
plt.title('Evolução do Crescimento - 2020 a 2025', fontsize=14)
plt.xlabel('Mês', fontsize=12)
plt.ylabel('Crescimento', fontsize=12)
plt.xticks(crescimento_mensal.index, ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'])
plt.grid(True)
plt.tight_layout()

# Exibindo o gráfico
plt.show()"
"""

# Lista contendo todos os datasets
datasets_juntar = [dataset2020, dataset2021, dataset2022, dataset2023, dataset2024, dataset2025]

# Concatenar todos os datasets
dataset_completo = pd.concat(datasets_juntar, ignore_index=True)

# Criando uma nova coluna de Data (Ano-Mês)
dataset_completo['Data'] = pd.to_datetime(dataset_completo['Ano'].astype(str) + '-' + dataset_completo['Mes'].astype(str), format='%Y-%m')

# Agrupar os dados por data (Ano-Mês) e calcular a média do Crescimento
crescimento_temporal = dataset_completo.groupby('Data')['Crescimento'].mean()

# Criar o gráfico de linha
plt.figure(figsize=(12, 6))
plt.plot(crescimento_temporal.index, crescimento_temporal.values, marker='o', color='b', linestyle='-', linewidth=2, markersize=6)

# Adicionar título e rótulos
plt.title('Evolução da Média Crescimento da Soja (2020 a 2025)', fontsize=14)
plt.xlabel('Ano-Mês', fontsize=12)
plt.ylabel('Média Crescimento', fontsize=12)
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Exibir o gráfico
plt.show()