import pandas as pd;
import numpy as np;
import seaborn as sns
import matplotlib.pyplot as plt

dataset_completo = pd.read_csv('../../criando-dataset-crescimento/datasets/crescimento-soja.csv', sep=';');

# Histograma usando Seaborn
sns.histplot(dataset_completo['Crescimento'], bins=400, kde=True, color='green', alpha=0.7, edgecolor='black')
plt.title('Distribuição do Crescimento das plantas')
plt.xlim(0, 250)
plt.xlabel('Crescimento')
plt.ylabel('Frequência')
plt.show()