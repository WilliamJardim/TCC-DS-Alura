import pandas as pd;
import numpy as np;
import seaborn as sns
import matplotlib.pyplot as plt

dataset_completo = pd.read_csv('../../criando-dataset-crescimento/datasets/crescimento-soja.csv', sep=';');

# Criar gráfico de barras com seaborn
plt.figure(figsize=(10, 6))
sns.barplot(x='Estacao', y='Crescimento', data=dataset_completo, estimator=np.mean, ci=None)

# Personalizar o gráfico
plt.xlabel('Estação do Ano')
plt.ylabel('Temmpo de Crescimento Total')
plt.title('Tempo de Crescimento da Soja por Estação do Ano')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Exibir o gráfico
plt.show()