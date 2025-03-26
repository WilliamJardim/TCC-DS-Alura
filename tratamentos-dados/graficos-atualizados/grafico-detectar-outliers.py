import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dataset = pd.read_csv('./datasets/dataset-tratado-normalizado-sem-outliers.csv', sep=';');

"""
Para esse exemplo, eu sei que os outliers estão apenas na coluna PRECO VENDA,
pois eu propositalmente criei esse dataset para ter Outliers nessa coluna para ensinar como identificar eles
"""

# OUTLIERS PARA O PRECO VENDA
# Criar um boxplot para uma variável específica
sns.boxplot(x=dataset['Preco_Venda'])
plt.title('Boxplot de Preco_Venda')
plt.show()

import numpy as np

# Calcular o IQR (Intervalo Interquartil)
Q1 = dataset['Preco_Venda'].quantile(0.25)
Q3 = dataset['Preco_Venda'].quantile(0.75)
IQR = Q3 - Q1

# Definir limites para outliers
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

# Filtrar os outliers
outliers = dataset[(dataset['Preco_Venda'] < limite_inferior) | 
                   (dataset['Preco_Venda'] > limite_superior)]

print("Outliers encontrados:\n", outliers)


from scipy.stats import zscore

# Calcular Z-score para a coluna
dataset['Z_Score'] = zscore(dataset['Preco_Venda'])

# Filtrar os outliers
outliers_z = dataset[(dataset['Z_Score'] > 3) | (dataset['Z_Score'] < -3)]
print("Outliers pelo Z-Score:\n", outliers_z)

"""
Como voce pode ver no gráfico do matplotlib, existem amostras que tem o Preco_Venda muito alto!, valores extremos que fogem do padrão. 
E isso é um exemplo de outlier que precisa ser tratado.

Esses não são os unicos tipos que podem existir.
Podem haver outros tipos de Outliers também, mais todos eles vão ter algo em comum: Vão ser valores extremos.

Nos outros dois testes feitos com quartis e com o Z-Score, vemos que existem no mínimo de 8 a 14 outliers, na coluna Preco_Venda.
Ou seja, existem de 8 a 14 amostras que tem valores extremos na coluna Preco_Venda. E precisam ser tratados ou removidos.
"""
