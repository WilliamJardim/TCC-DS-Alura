import pandas as pd

dataset = pd.read_csv('../csv/dataset-agricultura-v5.csv', sep=";");

print( dataset.head(52) )

print('Exploração:')
print(dataset.describe())

dataset_selecionado = dataset[['Tipo_Planta', 'Estacao_Ano', 'Custo_Cultivo', 'Litros_Agua_Semana', 'Tempo_Crescimento_horas', 'Preco_Venda', 'Saude', 'Tempo_Vida_dias']];

print( dataset_selecionado.head(52) )

print('\n\nPlantas doentes vs Saudaveis')

print( dataset_selecionado['Saude'].value_counts() )

# CONTANDO POR ESTAÇÂO

contagem_por_estacao = dataset_selecionado.groupby(['Estacao_Ano', 'Saude']).size().unstack(fill_value=0)

print('\n\nPlantas doentes vs Saudaveis Por Estação')

print(contagem_por_estacao)

print('\n\nPlantas doentes vs Saudaveis Proporção Por Estação')

proporcao_por_estacao = contagem_por_estacao.div(contagem_por_estacao.sum(axis=1), axis=0)

print(proporcao_por_estacao)


import matplotlib.pyplot as plt

proporcao_por_estacao.plot(kind='bar', stacked=True, color=['red', 'green'], figsize=(10, 6))
plt.title('Proporção de Plantas Doentes vs Saudáveis por Estação')
plt.xlabel('Estação')
plt.ylabel('Proporção')
plt.xticks(rotation=45)
plt.legend(['Doente', 'Saudável'])
plt.show()