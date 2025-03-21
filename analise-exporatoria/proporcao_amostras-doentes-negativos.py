import pandas as pd
import numpy as np

dataset = pd.read_csv('./datasets/dataset-agricultura-v5-balanceado.csv', sep=';');

dataset_selecionado = dataset[dataset['Litros_Agua_Semana'] < 0]

print('DADOS FILTRADOS', dataset_selecionado['Litros_Agua_Semana'].head(5))

contagem_por_saude = dataset_selecionado.groupby(['Saude', 'Litros_Agua_Semana']).size().unstack(fill_value=0)

print('\n\nConsumo de agua plantas Doentes vs Saudaveis')

print(contagem_por_saude.sum(axis=1))

"""
Com as melhoras não tem mais nenhuma amostra que se encaixa nessa situação
"""