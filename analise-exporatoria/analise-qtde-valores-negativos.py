import pandas as pd
import numpy as np

dataset = pd.read_csv('./datasets/dataset-agricultura-v5-balanceado.csv', sep=';');

print('\nAmostras com tempo de crescimento negativo:')
crescimentoNegativos = (dataset['Tempo_Crescimento_horas'] < 0).sum()

print(crescimentoNegativos)



print('\nAmostras com tempo de vida negativo:')
tempoVidaNegativo = (dataset['Tempo_Vida_dias'] < 0).sum()

print(tempoVidaNegativo)


print('\nAmostras com custo de cultivo negativo:')
custoCultivoNegativo = (dataset['Custo_Cultivo'] < 0).sum()

print(custoCultivoNegativo)



print('\nAmostras com consumo de agua negativo:')
litrosAguaNegativos = (dataset['Litros_Agua_Semana'] < 0).sum()

print(litrosAguaNegativos)



print('\nAmostras com chuva negativo:')
chuvaNegativo = (dataset['Chuva_mm'] < 0).sum()

print(chuvaNegativo)