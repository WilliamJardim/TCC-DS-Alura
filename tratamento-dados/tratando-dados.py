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



"""
Agora vou tratar os valores NaN, substituindo eles pela média da coluna
"""

# Eu já sei que a coluna que tem valores NaN é a Crescimento
# Agora eu quero descobrir em quais estações do ano, e em quais anos, pra saber onde exatamente estão esses valores, para que eu possa remover
print( dataset.loc[ dataset['Crescimento'].isna() ] )

# Calculo a média da coluna Crescimento SOMENTE DO ANO DE 2020, NO MES DE ABRIL, NO OUTONO
media_crescimento_ano2020_outono = dataset.loc[ (dataset['Mes'] == 4) & (dataset['Estacao'] == 'Outono') & (dataset['Ano'] == 2020) ]['Crescimento'].mean()

# Eu substitui os valores NaN por essa média
dataset.loc[ (dataset['Crescimento'].isna()) & (dataset['Nome_Mes'] == 'Abril') & (dataset['Estacao'] == 'Outono') & (dataset['Ano'] == 2020), 'Crescimento' ] = media_crescimento_ano2020_outono;

"""
Pronto! Não existem mais valores NaN
"""

# Salva o dataset tratado
dataset.to_csv('crescimento-soja-tratado.csv', sep=';', index=False)