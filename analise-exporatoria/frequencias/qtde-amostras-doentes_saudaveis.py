import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o dataset
dataset = pd.read_csv('../datasets/dataset-agricultura-v5-balanceado.csv', sep=';')

# Contar amostras por Saude
contagem = dataset['Saude'].value_counts()

print('CONTAGEM Doentes vs Saudáveis', contagem);

# Criar gráfico de barras
plt.figure(figsize=(6, 4))
ax = sns.barplot(x=contagem.index, y=contagem.values, palette=['green', 'red'])

# Adicionar os valores dentro das barras
for i, v in enumerate(contagem.values):
    ax.text(i, v + 2, str(v), ha='center', fontsize=12)

plt.xlabel('Classe')
plt.ylabel('Quantidade de Amostras')
plt.title('Distribuição de Amostras: Doentes vs Saudáveis')
plt.show()
