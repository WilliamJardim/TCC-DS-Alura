import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dataset = pd.read_csv('../criando-dataset/datasets/crescimento-soja.csv', sep=';')

# Convetendo cada estação para um número
"""
Convetendo cada estação para um número
"""
mapeamento = {'Verão': 1, 'Outono': 2, 'Inverno': 3, 'Primavera': 4}
dataset['Estacao_Numero'] = dataset['Estacao'].map(mapeamento)


# Convertendo o número do mes para o nome do mes
"""
Convertendo o número do mes para o nome do mes
"""
meses = {
    1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio',
    6: 'Junho', 7: 'Julho', 8: 'Agosto', 9: 'Setembro', 10: 'Outubro',
    11: 'Novembro', 12: 'Dezembro'
}

# Usando o dicionário para mapear os números para nomes
dataset['Nome_Mes'] = dataset['Mes'].map(meses)

"""
Com isso, eu criei duas novas colunas ao meu dataset: Estacao_Numero e Nome_Mes
"""

print( dataset.describe() )
print( dataset.head() );


"""
Agora vou remover os dois Outliers que eu coloquei propositalmente na etapa de criação do dataset

Pra simplificar a explicação, como eu já sei que os Outliers tem valores maiores que 300, eu posso remover isso já!
"""

print( 'QTDE AMOSTRAS COM CRESCIMENTO ACIMA DO MAXIMO', dataset[ dataset['Crescimento'] > 300 ]['Crescimento'].count() );

# Agora basta eu remover
outliers = dataset.loc[ dataset['Crescimento'] > 300 ]

# Remover essas linhas do dataset
dataset.drop( outliers.index, inplace=True );

print( 'QTDE AMOSTRAS COM CRESCIMENTO ACIMA DO MAXIMO', dataset[ dataset['Crescimento'] > 300 ]['Crescimento'].count() );