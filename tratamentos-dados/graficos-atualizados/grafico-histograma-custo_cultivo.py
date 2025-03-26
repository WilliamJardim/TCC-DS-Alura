import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dataset = pd.read_csv('../datasets/dataset-tratado-normalizado-sem-outliers.csv', sep=';');

# Removendo features que não vão ser usadas
dataset = dataset.drop('Data', axis=1);
dataset = dataset.drop('Estacao_Ano', axis=1);
dataset = dataset.drop('Tipo_Planta', axis=1);
dataset = dataset.drop('Tipo_Solo', axis=1);
dataset = dataset.drop('Saude', axis=1);

# Histograma usando Seaborn
sns.histplot(dataset['Custo_Cultivo'], bins=400, kde=True, color='blue', alpha=0.7, edgecolor='black')
plt.title('Distribuição do Custo_Cultivo das plantas')
plt.xlabel('Custo_Cultivo')
plt.ylabel('Frequência')
plt.show()