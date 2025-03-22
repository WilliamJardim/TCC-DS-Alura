import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o dataset
dataset = pd.read_csv('../datasets/dataset-agricultura-v5-balanceado.csv', sep=';')

# Calcular a média de custo de cultivo por estação
data_media_custo_cultivo = dataset.groupby('Estacao_Ano')['Custo_Cultivo'].mean()
print(data_media_custo_cultivo)

plt.figure(figsize=(8, 6))
data_media_custo_cultivo.plot(kind='bar', color='blue')
plt.xlabel('Estação')
plt.ylabel('Média Custo Cultivo (R$)')
plt.title('Média de Custo Cultivo das Plantas por Estação')
plt.xticks(rotation=0)
plt.show()

# Calcular a média de custo de cultivo por saúde das plantas
media_custo_por_saude = dataset.groupby('Saude')['Custo_Cultivo'].mean()
print(media_custo_por_saude)

plt.figure(figsize=(8, 6))
media_custo_por_saude.plot(kind='bar', color=['red', 'green'])
plt.xlabel('Saúde')
plt.ylabel('Média Custo Cultivo (R$)')
plt.title('Média de Custo Cultivo: Plantas Doentes vs Saudáveis')
plt.xticks(rotation=0)
plt.show()