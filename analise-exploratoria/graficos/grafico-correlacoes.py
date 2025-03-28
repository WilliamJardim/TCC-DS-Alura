import pandas as pd;
import numpy as np;
import seaborn as sns
import matplotlib.pyplot as plt

dataset_completo = pd.read_csv('../../criando-dataset/datasets/crescimento-soja.csv', sep=';');

# Removendo features que não vão ser usadas
dataset_completo = dataset_completo.drop('Estacao', axis=1);

# Calcular a matriz de correlação
corr = dataset_completo.corr()

# Criar o heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)

# Configurações do gráfico
plt.title("Mapa de Calor das Correlações")
plt.show()