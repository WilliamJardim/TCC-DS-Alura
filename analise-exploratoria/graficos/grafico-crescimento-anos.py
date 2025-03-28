import pandas as pd;
import numpy as np;
import seaborn as sns
import matplotlib.pyplot as plt

dataset_completo = pd.read_csv('../../criando-dataset/datasets/crescimento-soja.csv', sep=';');

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