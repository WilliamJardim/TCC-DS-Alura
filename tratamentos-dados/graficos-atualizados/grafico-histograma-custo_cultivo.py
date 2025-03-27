import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dataset = pd.read_csv('../datasets/dataset-tratado-normalizado-sem-outliers.csv', sep=';');

# Histograma usando Seaborn
sns.histplot(dataset['Custo_Cultivo'], bins=400, kde=True, color='blue', alpha=0.7, edgecolor='black')
plt.title('Distribuição do Custo_Cultivo das plantas')
plt.xlabel('Custo_Cultivo')
plt.ylabel('Frequência')
plt.show()