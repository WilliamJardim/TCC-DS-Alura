import pandas as pd
import matplotlib.pyplot as plt

# Carregar o dataset balanceado
df = pd.read_csv('../csv/dataset-agricultura-v5-v4balanceado.csv', sep=";")

# Verificar as primeiras linhas para garantir que o dataset está correto
print("Primeiras linhas do dataset:")
print(df.head())

# 1. **Verificar Variedade de Plantas (Tipos de Planta)**
print("\nVariedade de Plantas:")
print(df['Tipo_Planta'].value_counts())

# 2. **Verificar Tipos de Solo**
print("\nVariedade de Tipos de Solo:")
print(df['Tipo_Solo'].value_counts())

# 3. **Verificar Tipos de Clima (Estação)**
print("\nVariedade de Estações/Ano (Clima):")
print(df['Estacao_Ano'].value_counts())

# 4. **Verificar a Distribuição de Saúde das Plantas (Doente vs Saudável)**
print("\nDistribuição de Saúde das Plantas:")
print(df['Saude'].value_counts())

# 5. **Verificar a Distribuição de Saúde das Plantas por Estação (Doente vs Saudável por Estação)**
contagem_por_estacao = df.groupby(['Estacao_Ano', 'Saude']).size().unstack(fill_value=0)
print("\nPlantas doentes vs Saudáveis Por Estação:")
print(contagem_por_estacao)

# 6. **Verificar a Proporção de Doentes vs Saudáveis por Estação**
proporcao_por_estacao = contagem_por_estacao.div(contagem_por_estacao.sum(axis=1), axis=0)
print("\nProporção de Plantas Doentes vs Saudáveis Por Estação:")
print(proporcao_por_estacao)

# 7. **Verificar a Diversidade de Variáveis Importantes (Tempo de Crescimento, Custo de Cultivo, Preço de Venda)**
print("\nEstatísticas do Tempo de Crescimento (Horas):")
print(df['Tempo_Crescimento_horas'].describe())

print("\nEstatísticas do Custo de Cultivo:")
print(df['Custo_Cultivo'].describe())

print("\nEstatísticas do Preço de Venda:")
print(df['Preco_Venda'].describe())

# 8. **Verificar a Distribuição dos Tipos de Solo por Estação**
distribuicao_solo_por_estacao = df.groupby(['Estacao_Ano', 'Tipo_Solo']).size().unstack(fill_value=0)
print("\nDistribuição dos Tipos de Solo por Estação:")
print(distribuicao_solo_por_estacao)

# 9. **Verificar a Proporção de Tipos de Solo por Estação**
proporcao_solo_por_estacao = distribuicao_solo_por_estacao.div(distribuicao_solo_por_estacao.sum(axis=1), axis=0)
print("\nProporção de Tipos de Solo por Estação:")
print(proporcao_solo_por_estacao)

# 10. **Verificar amostras por Estação para garantir balanceamento adequado**
amostras_por_estacao = df['Estacao_Ano'].value_counts()
print("\nNúmero de Amostras por Estação:")
print(amostras_por_estacao)

# 11. **Visualizar a Distribuição de Doentes vs Saudáveis por Estação em um Gráfico de Barras**
proporcao_por_estacao.plot(kind='bar', stacked=True, color=['red', 'green'], figsize=(10, 6))
plt.title('Proporção de Plantas Doentes vs Saudáveis por Estação')
plt.xlabel('Estação')
plt.ylabel('Proporção')
plt.xticks(rotation=45)
plt.legend(['Doente', 'Saudável'])
plt.show()

# 12. **Visualizar a Distribuição dos Tipos de Solo por Estação em um Gráfico de Barras**
proporcao_solo_por_estacao.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Proporção de Tipos de Solo por Estação')
plt.xlabel('Estação')
plt.ylabel('Proporção')
plt.xticks(rotation=45)
plt.show()

# 13. **Verificar se o total de doentes está adequado (826 no total, distribuído de forma equilibrada)**
doentes_totais = df[df['Saude'] == 'Doente'].shape[0]
print(f"\nTotal de Plantas Doentes: {doentes_totais}")