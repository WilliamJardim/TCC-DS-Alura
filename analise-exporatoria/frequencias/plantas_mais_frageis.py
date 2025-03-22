import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o dataset
dataset = pd.read_csv('../datasets/dataset-agricultura-v5-balanceado.csv', sep=';')

# Identificar os tipos de plantas mais frágeis (maior número de doentes) por estação
fragilidade_por_estacao = dataset[dataset['Saude'] == 'Doente'].groupby(['Estacao_Ano', 'Tipo_Planta']).size().unstack(fill_value=0)
print(fragilidade_por_estacao)

# Criar gráfico
plt.figure(figsize=(10, 6))
fragilidade_por_estacao.plot(kind='bar', stacked=True, colormap='viridis', figsize=(10, 6))
plt.xlabel('Estação')
plt.ylabel('Quantidade de Plantas Doentes')
plt.title('Tipos de Plantas Mais Frágeis por Estação')
plt.xticks(rotation=0)
plt.legend(title='Tipo de Planta', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

# Criar gráfico de barras horizontais para melhor visualização
plt.figure(figsize=(12, 8))
sns.heatmap(fragilidade_por_estacao, annot=True, cmap='OrRd', linewidths=0.5, fmt='d')
plt.xlabel('Tipo de Planta')
plt.ylabel('Estação')
plt.title('Tipos de Plantas Mais Frágeis por Estação')
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.show()


# Criar subplots para melhor visualização
fig, axes = plt.subplots(1, 2, figsize=(18, 8))

# Gráfico de barras empilhadas
fragilidade_por_estacao.plot(kind='bar', stacked=True, colormap='viridis', ax=axes[0])
axes[0].set_xlabel('Estação')
axes[0].set_ylabel('Quantidade de Plantas Doentes')
axes[0].set_title('Tipos de Plantas Mais Frágeis por Estação')
axes[0].tick_params(axis='x', rotation=0)
axes[0].legend(title='Tipo de Planta', bbox_to_anchor=(1.05, 1), loc='upper left')

# Heatmap para melhor visualização
sns.heatmap(fragilidade_por_estacao, annot=True, cmap='OrRd', linewidths=0.5, fmt='d', ax=axes[1])
axes[1].set_xlabel('Tipo de Planta')
axes[1].set_ylabel('Estação')
axes[1].set_title('Tipos de Plantas Mais Frágeis por Estação')
axes[1].tick_params(axis='x', rotation=45, labelrotation=45)
axes[1].tick_params(axis='y', rotation=0)

plt.tight_layout()
plt.show()
