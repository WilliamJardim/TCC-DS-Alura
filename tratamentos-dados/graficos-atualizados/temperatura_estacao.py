import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o dataset
dataset = pd.read_csv('../datasets/dataset-tratado-normalizado-sem-outliers.csv', sep=';')

# Calculando a média de chuva por estação do ano
media_chuva = dataset.groupby("Estacao_Ano")["Temperatura_C"].mean()

# Criando o gráfico
plt.figure(figsize=(8, 5))
media_chuva.plot(kind="bar", color="skyblue", edgecolor="black")

# Configurando rótulos
plt.xlabel("Estação do Ano")
plt.ylabel("Temperatura (C)")
plt.title("Média de Temperatura por Estação do Ano")
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Exibindo o gráfico
plt.show()