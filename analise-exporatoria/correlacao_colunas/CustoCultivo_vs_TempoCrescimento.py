import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import statsmodels

dataset = pd.read_csv('../datasets/dataset-agricultura-v5-balanceado.csv', sep=';');

# Removendo features que não vão ser usadas
dataset = dataset.drop('Data', axis=1);
dataset = dataset.drop('Estacao_Ano', axis=1);
dataset = dataset.drop('Tipo_Planta', axis=1);
dataset = dataset.drop('Tipo_Solo', axis=1);
dataset = dataset.drop('Saude', axis=1);

xColuna = 'Custo_Cultivo';
yColuna = 'Tempo_Crescimento_horas'

x = dataset[xColuna];
y = dataset[yColuna];

# Criando o gráfico de dispersão
plt.scatter(x, y, color='blue', alpha=0.5, label='Dados')

# Adicionando rótulos e título
plt.xlabel(xColuna)
plt.ylabel(yColuna)
plt.title('Gráfico de Dispersão')
plt.legend()

# Exibindo o gráfico
plt.show()

correlacao = np.corrcoef(x, y)[0, 1]
print(f"Correlação de Pearson: {correlacao:.2f}")

# Correlação de Spearman
spearman_corr = dataset.corr(method="spearman")
print(f"Correlação de Spearman: {spearman_corr.iloc[0,1]:.2f}")

# Correlação de Kendall
kendall_corr = dataset.corr(method="kendall")
print(f"Correlação de Kendall: {kendall_corr.iloc[0,1]:.2f}")

# Outro gráfico para ajudar a entender
sns.regplot(x=x, y=y, 
            scatter_kws={"alpha": 0.5}, lowess=True, line_kws={"color": "red"})
plt.show()