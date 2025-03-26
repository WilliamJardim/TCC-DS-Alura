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
sns.histplot(dataset['Tempo_Vida_dias'], bins=400, kde=True, color='green', alpha=0.7, edgecolor='black')
plt.title('Distribuição do Tempo_Vida_dias das plantas')
plt.xlabel('Tempo_Vida_dias')
plt.ylabel('Frequência')
plt.show()

"""
# Criando histogramas e visualizando frequências
plt.figure(figsize=(12, 6))
counts, edges, _ = plt.hist(dataset['Tempo_Vida_dias'], bins=400, color='green', alpha=0.7, edgecolor='black')
plt.xticks(rotation=45)
plt.title('Histograma')
plt.xlabel("Valores")
plt.ylabel("Frequência")
for j in range(len(counts)):
    plt.text(edges[j], counts[j] + 2, str(int(counts[j])), ha='center', fontsize=9, color='black')
plt.tight_layout()
plt.show()
"""
