import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dataset = pd.read_csv('../datasets/dataset-tratado-normalizado-sem-outliers.csv', sep=';');

# Removendo features que não vão ser usadas
dataset = dataset.drop('Data', axis=1);
dataset = dataset.drop('Estacao_Ano', axis=1);
dataset = dataset.drop('Tipo_Planta', axis=1);

# Calcular a matriz de correlação
corr = dataset.corr()

# Criar o heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)

# Configurações do gráfico
plt.title("Mapa de Calor das Correlações")
plt.show()
