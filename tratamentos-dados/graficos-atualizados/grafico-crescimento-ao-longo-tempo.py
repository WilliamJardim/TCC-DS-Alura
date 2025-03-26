import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv('./datasets/dataset-tratado-normalizado-sem-outliers.csv', sep=';');

# Converter a coluna de data para o formato datetime
dataset['Data'] = pd.to_datetime(dataset['Data'])

import matplotlib.pyplot as plt

# Ordenar o dataset pela data (caso não esteja ordenado)
dataset = dataset.sort_values(by='Data')

# Criar o gráfico de linha
plt.figure(figsize=(10, 5))
plt.plot(dataset['Data'], dataset['Tempo_Crescimento_horas'], marker='o', linestyle='-')

# Personalizar o gráfico
plt.xlabel("Data")
plt.ylabel("Tempo de Crescimento (horas)")
plt.title("Evolução do Tempo de Crescimento ao Longo da Data")
plt.xticks(rotation=45)  # Rotacionar datas para melhor visualização
plt.grid(True)
plt.show()


# VER GRAFICO USANDO MEDIAS MOVEIS
# Definir a janela da média móvel (ex: 7 dias)
janela = 7
dataset['Média_Móvel'] = dataset['Tempo_Crescimento_horas'].rolling(window=janela).mean()

# Criar o gráfico
plt.figure(figsize=(10, 5))
sns.lineplot(x=dataset['Data'], y=dataset['Tempo_Crescimento_horas'], label="Original", alpha=0.5)
sns.lineplot(x=dataset['Data'], y=dataset['Média_Móvel'], label=f"Média Móvel {janela} dias", color="red")

# Personalizar o gráfico
plt.xlabel("Data")
plt.ylabel("Tempo de Crescimento (horas)")
plt.title(f"Média Móvel ({janela} dias) do Tempo de Crescimento")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.show()