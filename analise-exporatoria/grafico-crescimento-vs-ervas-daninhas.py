import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv('./datasets/dataset-agricultura-v5-balanceado.csv', sep=';');

# Criar gráfico de dispersão
plt.figure(figsize=(8, 5))
sns.scatterplot(x=dataset['Ervas_Daninhas'], y=dataset['Tempo_Crescimento_horas'])

# Configurações do gráfico
plt.xlabel("Ervas Daninhas")
plt.ylabel("Tempo de Crescimento (horas)")
plt.title("Relação entre Tempo de Crescimento e Ervas Daninhas")
plt.grid(True)
plt.show()
