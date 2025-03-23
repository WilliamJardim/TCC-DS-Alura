import pandas as pd
import numpy as np

"""
Tempos de Crescimento Comuns para plantas:

  - Trigo: Pode levar de 90 a 120 dias para crescer totalmente, o que equivale a cerca de 2.160 a 2.880 horas.

  - Tomate: Normalmente leva entre 50 a 85 dias para amadurecer, ou seja, de 1.200 a 2.040 horas.

  - Milho: O milho geralmente cresce em torno de 60 a 100 dias, o que equivale a 1.440 a 2.400 horas.

  - Cenoura: Leva entre 70 a 80 dias para crescer, ou seja, de 1.680 a 1.920 horas.

  - Soja: O tempo de crescimento varia, mas pode ser de 100 a 150 dias, o que dá entre 2.400 a 3.600 horas.

"""

dataset = pd.read_csv('./datasets/dataset-agricultura-v5-balanceado.csv', sep=';');

print('DATASET ANTES DE MUDAR A ESCALA DO TEMPO CRESCIMENTO:')
print(dataset.head()['Tempo_Crescimento_horas'])

dataset['Tempo_Crescimento_horas'] = dataset['Tempo_Crescimento_horas'] / 999

print('DATASET DEPOIS DE MUDAR A ESCALA DO TEMPO CRESCIMENTO')
print(dataset.head()['Tempo_Crescimento_horas'])


print('DATASET ANTES DE MUDAR A ESCALA:')
print(dataset.head())

# Reduzindo a escala das outras colunas
dataset['Litros_Agua_Semana'] = dataset['Litros_Agua_Semana'] / 999
dataset['Custo_Cultivo'] = dataset['Custo_Cultivo'] / 999
dataset['Preco_Venda'] = dataset['Preco_Venda'] / 999999
dataset['Tempo_Vida_dias'] = dataset['Tempo_Vida_dias'] / 999

print('DATASET DEPOIS DE MUDAR A ESCALA')
print(dataset.head())

"""
# ver a coluna Altura_cm
print('DATASET ANTES DE MUDAR A ESCALA DA ALTURA CM:')
print(dataset.head()['Altura_cm'])

dataset['Altura_cm'] = dataset['Altura_cm'] / 100

print('DATASET DEPOIS DE MUDAR A ESCALA DA ALTURA CM:')
print(dataset.head()['Altura_cm'])"
"""