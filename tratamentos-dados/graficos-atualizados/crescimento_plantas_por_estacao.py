import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o dataset
dataset = pd.read_csv('../datasets/dataset-tratado-normalizado-sem-outliers.csv', sep=';')

# Removendo features que não vão ser usadas
dataset = dataset.drop('Data', axis=1);

media_crescimento_por_estacao = dataset.groupby(['Estacao_Ano', 'Tipo_Planta']).mean()['Tempo_Crescimento_horas']

print(media_crescimento_por_estacao)

# Criar gráfico
plt.figure(figsize=(10, 6))
media_crescimento_por_estacao.plot(kind='bar', stacked=True, colormap='viridis', figsize=(10, 6))
plt.xlabel('Estação')
plt.ylabel('Crescimento')
plt.title('Média crescimento dos Tipos de plantas por Estação')
plt.xticks(rotation=0)
plt.legend(title='Tipo de Planta', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

# Criar subplots para cada estação
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(14, 10))
fig.tight_layout(pad=5.0)

# Gráfico para a estação 'Primavera'
bars = media_crescimento_por_estacao['Primavera'].plot(kind='bar', stacked=True, colormap='viridis', ax=axes[0, 0])
axes[0, 0].set_title('Primavera')
#axes[0, 0].set_xlabel('Tipo de Planta')
axes[0, 0].set_ylabel('Crescimento (Horas)')
axes[0, 0].set_xticks(range(len(media_crescimento_por_estacao['Primavera'])))  # Definir posições no eixo X
axes[0, 0].set_xticklabels(media_crescimento_por_estacao['Primavera'].index, rotation=45)  # Usar os nomes das plantas
for p in bars.patches:
    height = p.get_height()
    axes[0, 0].text(p.get_x() + p.get_width() / 2., height + 1, f'{height:.1f}', ha='center', va='bottom')

# Gráfico para a estação 'Verão'
bars = media_crescimento_por_estacao['Verão'].plot(kind='bar', stacked=True, colormap='plasma', ax=axes[0, 1])
axes[0, 1].set_title('Verão')
#axes[0, 1].set_xlabel('Tipo de Planta')
axes[0, 1].set_ylabel('Crescimento (Horas)')
axes[0, 1].set_xticks(range(len(media_crescimento_por_estacao['Verão'])))  # Definir posições no eixo X
axes[0, 1].set_xticklabels(media_crescimento_por_estacao['Verão'].index, rotation=45)  # Usar os nomes das plantas
for p in bars.patches:
    height = p.get_height()
    axes[0, 1].text(p.get_x() + p.get_width() / 2., height + 1, f'{height:.1f}', ha='center', va='bottom')

# Gráfico para a estação 'Outono'
bars = media_crescimento_por_estacao['Outono'].plot(kind='bar', stacked=True, colormap='inferno', ax=axes[1, 0])
axes[1, 0].set_title('Outono')
#axes[1, 0].set_xlabel('Tipo de Planta')
axes[1, 0].set_ylabel('Crescimento (Horas)')
axes[1, 0].set_xticks(range(len(media_crescimento_por_estacao['Outono'])))  # Definir posições no eixo X
axes[1, 0].set_xticklabels(media_crescimento_por_estacao['Outono'].index, rotation=45)  # Usar os nomes das plantas
for p in bars.patches:
    height = p.get_height()
    axes[1, 0].text(p.get_x() + p.get_width() / 2., height + 1, f'{height:.1f}', ha='center', va='bottom')

# Gráfico para a estação 'Inverno'
bars = media_crescimento_por_estacao['Inverno'].plot(kind='bar', stacked=True, colormap='cividis', ax=axes[1, 1])
axes[1, 1].set_title('Inverno')
#axes[1, 1].set_xlabel('Tipo de Planta')
axes[1, 1].set_ylabel('Crescimento (Horas)')
axes[1, 1].set_xticks(range(len(media_crescimento_por_estacao['Inverno'])))  # Definir posições no eixo X
axes[1, 1].set_xticklabels(media_crescimento_por_estacao['Inverno'].index, rotation=45)  # Usar os nomes das plantas
for p in bars.patches:
    height = p.get_height()
    axes[1, 1].text(p.get_x() + p.get_width() / 2., height + 1, f'{height:.1f}', ha='center', va='bottom')

# Exibir os gráficos
plt.show()