import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o dataset
dataset = pd.read_csv('../datasets/dataset-agricultura-v5-balanceado.csv', sep=';')

# Calcular a média de vida por estação
media_vida = dataset.groupby('Estacao_Ano')['Tempo_Vida_dias'].mean()
print(media_vida)

# Criar gráfico de barras para a média de vida por estação
plt.figure(figsize=(8, 6))
media_vida.plot(kind='bar', color='blue')
plt.xlabel('Estação')
plt.ylabel('Média de Vida (dias)')
plt.title('Média de Vida das Plantas por Estação')
plt.xticks(rotation=0)
plt.show()
