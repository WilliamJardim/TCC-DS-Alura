import pandas as pd

df = pd.read_csv('../csv/dataset-agricultura-v4.csv', sep=";")

doentes = df[df['Saude'] == 'Doente']
saudaveis = df[df['Saude'] == 'Saudável']

total_doentes = 826

# Deixar apenas 826 plantas doentes ao todo,.. mais distribuido uniformemente por estação, pra ficar balanceado
undersampled_doentes = []

for estacao in doentes['Estacao_Ano'].unique():
    doentes_estacao = doentes[doentes['Estacao_Ano'] == estacao]
    
    num_doentes_estacao = int(len(doentes_estacao) / len(doentes) * total_doentes)
    
    doentes_limitados_estacao = doentes_estacao.head(num_doentes_estacao)
    
    undersampled_doentes.append(doentes_limitados_estacao)

doentes_undersampled = pd.concat(undersampled_doentes)

novo_dataset = pd.concat([doentes_undersampled, saudaveis])

# Embaralhar o dataset final para garantir aleatoriedade
#novo_dataset = novo_dataset.sample(frac=1, random_state=42).reset_index(drop=True)

dataset_selecionado = novo_dataset[['Tipo_Planta', 'Estacao_Ano', 'Custo_Cultivo', 'Litros_Agua_Semana', 
                                    'Tempo_Crescimento_horas', 'Preco_Venda', 'Saude', 'Tempo_Vida_dias']]

print(dataset_selecionado.head(52))

print('\n\nPlantas doentes vs Saudáveis')
print(dataset_selecionado['Saude'].value_counts())

contagem_por_estacao = dataset_selecionado.groupby(['Estacao_Ano', 'Saude']).size().unstack(fill_value=0)

print('\n\nPlantas doentes vs Saudáveis Por Estação')
print(contagem_por_estacao)

print('\n\nPlantas doentes vs Saudáveis Proporção Por Estação')

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

novo_dataset.to_csv('../csv/dataset-agricultura-v4-balanceado.csv', index=False, sep=';');