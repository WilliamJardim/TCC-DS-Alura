import pandas as pd;
import numpy as np;
import seaborn as sns
import matplotlib.pyplot as plt

dataset_completo = pd.read_csv('../../criando-dataset/datasets/crescimento-soja.csv', sep=';');
dataset_completo = dataset_completo[ dataset_completo['Ano'] == 2020 ]

xColuna = 'Ano';
yColuna = 'Crescimento';

x = dataset_completo[xColuna];
y = dataset_completo[yColuna];

# Criando o gráfico de dispersão
plt.scatter(x, y, color='blue', alpha=0.5, label='Dados')

# Adicionando rótulos e título
plt.xlabel(xColuna)
plt.ylabel(yColuna)
plt.ylim(0, 190)
plt.title('Gráfico de Dispersão: ' + str(xColuna) + ' vs ' + str(yColuna) )
plt.legend()

# Exibindo o gráfico
plt.show()
