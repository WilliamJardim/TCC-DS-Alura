import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o dataset
dataset = pd.read_csv('../datasets/dataset-tratado-normalizado-sem-outliers.csv', sep=';')

media_pragas = dataset.groupby('Estacao_Ano')['Num_Praga'].mean()
print(media_pragas)

plt.figure(figsize=(8, 6))
media_pragas.plot(kind='bar', color='blue')
plt.xlabel('Estação')
plt.ylabel('Média Pragas')
plt.title('Média de Pragas das Plantas por Estação')
plt.xticks(rotation=0)
plt.show()
