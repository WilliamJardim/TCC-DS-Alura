import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dataset = pd.read_csv('../criando-dataset-crescimento/datasets/crescimento-soja.csv', sep=';')

print( dataset.describe() )
print( dataset.shape )

# vendo se tem valores negativos
print( dataset[ dataset['Crescimento'] < 0 ].count()['Crescimento'].sum() )

# Ver se tem valores NaN e contar quantos são, por coluna
quantidade_nan_por_coluna = dataset.isna().sum()
print(quantidade_nan_por_coluna)

# Ver se tem Outliers(valores extremos)
# Criar um boxplot para uma variável específica
sns.boxplot(x=dataset['Crescimento'])
plt.title('Boxplot de Crescimento')
plt.show()

import numpy as np

# Calcular o IQR (Intervalo Interquartil)
Q1 = dataset['Crescimento'].quantile(0.25)
Q3 = dataset['Crescimento'].quantile(0.75)
IQR = Q3 - Q1

# Definir limites para outliers
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

# Filtrar os outliers
outliers = dataset[(dataset['Crescimento'] < limite_inferior) | 
                   (dataset['Crescimento'] > limite_superior)]

print("Outliers encontrados:\n", outliers)


from scipy.stats import zscore

# Calcular Z-score para a coluna
dataset['Z_Score'] = zscore(dataset['Crescimento'])

# Filtrar os outliers
outliers_z = dataset[(dataset['Z_Score'] > 3) | (dataset['Z_Score'] < -3)]
print("Outliers pelo Z-Score:\n", outliers_z)

"""
Como voce pode ver no gráfico do matplotlib, existem amostras que tem o Crescimento muito alto!, valores extremos que fogem do padrão. 
E isso é um exemplo de outlier que precisa ser tratado.

Esses não são os unicos tipos que podem existir.
Podem haver outros tipos de Outliers também, mais todos eles vão ter algo em comum: Vão ser valores extremos.
"""