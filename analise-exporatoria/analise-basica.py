import pandas as pd
import numpy as np

dataset = pd.read_csv('./datasets/dataset-agricultura-v5-v4balanceado.csv', sep=';');

print('\nCABECALHO:')
print(dataset.head())

print('\nDESCREVER O DATASET:')
print( dataset.describe() )

print('\nAMOSTRAS')
print( dataset.shape ) # 1650 amostras com 24 colunas

# Quantidade de valores nulos
print( '\n QTDE VALORES NULOS POR COLUNA' )
print( dataset.isnull().sum() )

print('\n QTDE AMOSTRAS DUPLICADAS')
print( dataset.duplicated().sum() )