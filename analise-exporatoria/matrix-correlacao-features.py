import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

dataset = pd.read_csv('./datasets/dataset-agricultura-v5-v4balanceado.csv', sep=';');

dataset = dataset.drop('Data', axis=1);
dataset = dataset.drop('Estacao_Ano', axis=1);
dataset = dataset.drop('Tipo_Planta', axis=1);
dataset = dataset.drop('Tipo_Solo', axis=1);
dataset = dataset.drop('Saude', axis=1);

print( '\nMATRIZ CORRELAÇÂO:' );
print( dataset.corr() )

print('CORREAÇÂO DA FEATURE Tempo_Crescimento_horas com as demais')
correlations = dataset.corrwith(dataset['Tempo_Crescimento_horas'])

print(correlations)

# Criar um gráfico de barras para visualizar melhor
plt.figure(figsize=(8, 5))
sns.barplot(x=correlations.index, y=correlations.values)
plt.xticks(rotation=90)
plt.title("Correlação de Tempo_Crescimento_horas com as demais features")
plt.show()


print('CORREAÇÂO DA FEATURE Custo_Cultivo com as demais')
correlations = dataset.corrwith(dataset['Custo_Cultivo'])

print(correlations)

# Criar um gráfico de barras para visualizar melhor
plt.figure(figsize=(8, 5))
sns.barplot(x=correlations.index, y=correlations.values)
plt.xticks(rotation=90)
plt.title("Correlação de Custo_Cultivo com as demais features")
plt.show()