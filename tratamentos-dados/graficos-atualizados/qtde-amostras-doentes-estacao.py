import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o dataset
dataset = pd.read_csv('../datasets/dataset-tratado-normalizado-sem-outliers.csv', sep=';')

# Contar amostras por classe e estação
contagem = dataset.groupby(['Estacao_Ano', 'Saude']).size().unstack()

print(contagem)

# Criar gráfico de barras
plt.figure(figsize=(8, 6))
contagem.plot(kind='bar', stacked=True, color=['red', 'green'])

plt.xlabel('Estação')
plt.ylabel('Quantidade de Amostras')
plt.title('Distribuição de Amostras por Estação: Doentes vs Saudáveis')
plt.legend(title='Classe', labels=['Doentes', 'Saudáveis'])
plt.xticks(rotation=0)

# Adicionar os números dentro das barras
for i in range(len(contagem)): 
    saudaveis = contagem.iloc[i, 0] if pd.notna(contagem.iloc[i, 0]) else 0
    doentes = contagem.iloc[i, 1] if pd.notna(contagem.iloc[i, 1]) else 0
    
    plt.text(i, saudaveis / 2, str(int(saudaveis)), ha='center', color='white', fontsize=12)
    plt.text(i, saudaveis + doentes / 2, str(int(doentes)), ha='center', color='white', fontsize=12)

plt.show()
