import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar os dados
dataset_completo = pd.read_csv('../../criando-dataset/datasets/crescimento-soja.csv', sep=';')

# Criar coluna de Data (Ano-Mês)
dataset_completo['Data'] = pd.to_datetime(dataset_completo['Ano'].astype(str) + '-' + dataset_completo['Mes'].astype(str), format='%Y-%m')

# Calcular a média do crescimento por data
crescimento_temporal = dataset_completo.groupby('Data')['Crescimento'].mean()

# Calcular a média móvel (janela de 3 meses)
crescimento_temporal_mm = crescimento_temporal.rolling(window=3, min_periods=1).mean()

# Criar o gráfico de linha
plt.figure(figsize=(12, 6))

# Linha original
plt.plot(crescimento_temporal.index, crescimento_temporal.values, marker='o', color='b', linestyle='-', linewidth=1, markersize=4, label='Crescimento Médio')

# Linha de Média Móvel
plt.plot(crescimento_temporal_mm.index, crescimento_temporal_mm.values, color='red', linestyle='-', linewidth=2, label='Média Móvel (3 meses)')

# Adicionar título e rótulos
plt.title('Evolução da Média do Crescimento da Soja (2020 a 2025)', fontsize=14)
plt.xlabel('Ano-Mês', fontsize=12)
plt.ylabel('Crescimento Médio', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(rotation=45)
plt.tight_layout()

# Exibir o gráfico
plt.show()
