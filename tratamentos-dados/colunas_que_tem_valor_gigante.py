import pandas as pd
import numpy as np

dataset = pd.read_csv('./datasets/dataset-agricultura-v5-balanceado.csv', sep=';');

# Removendo features que não vão ser usadas
dataset = dataset.drop('Data', axis=1);
dataset = dataset.drop('Estacao_Ano', axis=1);
dataset = dataset.drop('Tipo_Planta', axis=1);
dataset = dataset.drop('Tipo_Solo', axis=1);
dataset = dataset.drop('Saude', axis=1);

# Reduzindo a escala das outras colunas
#dataset['Tempo_Crescimento_horas'] = dataset['Tempo_Crescimento_horas'] / 999
#dataset['Litros_Agua_Semana'] = dataset['Litros_Agua_Semana'] / 999
#dataset['Custo_Cultivo'] = dataset['Custo_Cultivo'] / 999
#dataset['Preco_Venda'] = dataset['Preco_Venda'] / 999999
#dataset['Tempo_Vida_dias'] = dataset['Tempo_Vida_dias'] / 999

#menor_numero = 999999
menor_numero = 1e+3 #1e+4 = 10000, 1e+3 = 1000
colunas = dataset.columns
colunasGrandes = [];

for coluna in colunas:
    for valorColuna in dataset[coluna]:
        if valorColuna >= menor_numero:
            colunasGrandes.append( coluna );
            break;

print('-=-= Colunas com valores em escala cientifica -=-=-');
for coluna in colunasGrandes:
    print(coluna);
