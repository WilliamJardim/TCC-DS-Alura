import pandas as pd;
import numpy as np;
import seaborn as sns
import matplotlib.pyplot as plt

dataset_completo = pd.read_csv('../../criando-dataset/datasets/crescimento-soja.csv', sep=';');

# Converter a coluna 'Mes' para string (caso esteja numérica)
dataset_completo['Mes'] = dataset_completo['Mes'].astype(str)

dataset_2020 = dataset_completo[ dataset_completo['Ano'] == 2020 ]

# Agrupar por mês e calcular a média de crescimento
crescimento_por_mes = dataset_2020.groupby('Mes')['Crescimento'].mean().reset_index()

# Ordenar os meses numericamente (caso estejam desordenados)
crescimento_por_mes = crescimento_por_mes.sort_values(by='Mes')

# Criar o gráfico de barras
plt.figure(figsize=(10, 5))
sns.barplot(x='Mes', y='Crescimento', data=crescimento_por_mes, palette='viridis')

# Personalizar o gráfico
plt.xlabel('Mês')
plt.ylabel('Crescimento Médio')
plt.title('Crescimento Médio da Soja por Mês de 2020 apenas')
plt.xticks(rotation=45)  # Rotaciona os nomes dos meses, se necessário
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Exibir o gráfico
plt.show()