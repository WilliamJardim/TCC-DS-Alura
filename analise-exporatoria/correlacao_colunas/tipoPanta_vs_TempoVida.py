import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

xColuna = 'Tipo_Planta';
yColuna = 'Tempo_Vida_dias';

dataset = pd.read_csv('../datasets/dataset-agricultura-v5-balanceado.csv', sep=';');
x = dataset[xColuna];
y = dataset[yColuna];

# Criando o gráfico de dispersão
plt.scatter(x, y, color='blue', alpha=0.5, label='Dados')

# Adicionando rótulos e título
plt.xlabel('Tipo da planta')
plt.ylabel('Tempo de vida')
plt.title('Gráfico de Dispersão: ' + str(xColuna) + ' vs ' + str(yColuna) )
plt.legend()

# Exibindo o gráfico
plt.show()
