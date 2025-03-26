import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o dataset
dataset = pd.read_csv('../datasets/dataset-tratado-normalizado-sem-outliers.csv', sep=';')

media_custo_cultivo = dataset.groupby('Estacao_Ano')['Custo_Cultivo'].mean()
print(media_custo_cultivo)

plt.figure(figsize=(8, 6))
media_custo_cultivo.plot(kind='bar', color='blue')
plt.xlabel('Estação')
plt.ylabel('Média Custo Cultivo (R$)')
plt.title('Média de Custo Cultivo das Plantas por Estação')
plt.xticks(rotation=0)
plt.show()
