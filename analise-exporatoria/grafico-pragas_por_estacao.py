import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('datasets/dataset-agricultura-v5-balanceado.csv', sep=";");

print( dataset.head(52) )

print('Exploração:')
print(dataset.describe())

dataset_selecionado = dataset[['Tipo_Planta', 'Estacao_Ano', 'Custo_Cultivo', 'Litros_Agua_Semana', 'Tempo_Crescimento_horas', 'Preco_Venda', 'Saude', 'Tempo_Vida_dias', 'Num_Praga']];

# CONTANDO POR ESTAÇÂO

agrupar_por_estacao = dataset_selecionado.groupby(['Estacao_Ano'])

medias_pragas_por_estacao = agrupar_por_estacao['Num_Praga'].mean()

# Criar o gráfico de barras
plt.figure(figsize=(8, 5))
medias_pragas_por_estacao.plot(kind='bar', color='skyblue', edgecolor='black')

# Personalizar o gráfico
plt.title('Média de Pragas por Estação do Ano')
plt.xlabel('Estação do Ano')
plt.ylabel('Média de Pragas')
plt.xticks(rotation=45)  # Rotacionar os rótulos do eixo X para melhor leitura
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Exibir o gráfico
plt.show()

"O verão é o periodo que mais tem pragas. A primavera tambem tem mais do que inverno e outono, só fica abaixo do Verão"