import pandas as pd
import numpy as np
np.random.seed(25)

"""
Tempos de Crescimento Comuns para plantas:

  - Trigo: Pode levar de 90 a 120 dias para crescer totalmente, o que equivale a cerca de 2.160 a 2.880 horas.

  - Tomate: Normalmente leva entre 50 a 85 dias para amadurecer, ou seja, de 1.200 a 2.040 horas.

  - Milho: O milho geralmente cresce em torno de 60 a 100 dias, o que equivale a 1.440 a 2.400 horas.

  - Cenoura: Leva entre 70 a 80 dias para crescer, ou seja, de 1.680 a 1.920 horas.

  - Soja: O tempo de crescimento varia, mas pode ser de 100 a 150 dias, o que dá entre 2.400 a 3.600 horas.

"""

dataset = pd.read_csv('./datasets/dataset-agricultura-v5-balanceado.csv', sep=';');

print('DATASET ANTES DE MUDAR A ESCALA DO TEMPO CRESCIMENTO:')
print(dataset.head()['Tempo_Crescimento_horas'])

dataset['Tempo_Crescimento_horas'] = dataset['Tempo_Crescimento_horas'] / 999

print('DATASET DEPOIS DE MUDAR A ESCALA DO TEMPO CRESCIMENTO')
print(dataset.head()['Tempo_Crescimento_horas'])


print('DATASET ANTES DE MUDAR A ESCALA:')
print(dataset.head())

# Reduzindo a escala das outras colunas
dataset['Litros_Agua_Semana'] = dataset['Litros_Agua_Semana'] / 999
dataset['Custo_Cultivo'] = dataset['Custo_Cultivo'] / 999
dataset['Preco_Venda'] = dataset['Preco_Venda'] / 999999
dataset['Tempo_Vida_dias'] = dataset['Tempo_Vida_dias'] / 999

print('DATASET DEPOIS DE MUDAR A ESCALA')
print(dataset.head())

"""
# ver a coluna Altura_cm
print('DATASET ANTES DE MUDAR A ESCALA DA ALTURA CM:')
print(dataset.head()['Altura_cm'])

dataset['Altura_cm'] = dataset['Altura_cm'] / 100

print('DATASET DEPOIS DE MUDAR A ESCALA DA ALTURA CM:')
print(dataset.head()['Altura_cm'])"
"""

"""
São 3000 amostras, 
DESSAS:

Amostras com chuva negativo:
615

Altura:
668

Frequencia_Podas:
1117

Horas_Sol_Dia:
1157

Temperatura_C:
782
"""

# DESCOBRIR SE OS VALORES NEGATIVOS SE CONCENTRAM EM UMA DETERMINADA ESTACAO
#print( 'ESTACOES COM VALORES DE HORAS SOL NEGATIVOS', dataset[ dataset['Horas_Sol_Dia'] < 3 ]['Estacao_Ano'].unique() )
#print( 'ESTACOES COM VALORES DE HORAS SOL NEGATIVOS', dataset[ dataset['Horas_Sol_Dia'] < 3.5 ]['Estacao_Ano'].unique() )

"""
Com esses dois codigos acima, descobri que curiosamente, elas estão todas no ['Inverno' 'Outono'] apenas
E que nenhuma estação tem valores <= 3, só de 3 pra cima
Então pra tratar esse, eu sei que posso deixar tudo como 3 ou 2
"""

# Tratei isso, removi tudo que era menor que zero para ficar 2 no lugar, eliminando os negativos nessa coluna
dataset.loc[ dataset['Horas_Sol_Dia'] < 3, 'Horas_Sol_Dia' ] = pd.Series(np.random.uniform(1.5, 2, size=len(dataset))); #Preenche com valores aleatorios entre 1.5 e 2, pra nao ficar sempre fixo


# VOU PROCURAR NAS OUTRAS COLUNAS
#print( 'ESTACOES COM VALORES DE FREQUENCIA PODAS NEGATIVOS', dataset[ dataset['Frequencia_Podas'] <= 0 ]['Estacao_Ano'].unique() )

"""
Aqui descobri que já não dá pra tratar, por que em todas as estações temos valores de Frequencia_Podas negativos.
Alias, grande parte deles é negativo

Minha estrategia seria aumentar a escala pra todos os valores ficarem maior que zero, ai eu idenficar o valor que posso usar pra separar, e reduzir a escala denovo
"""

# Primeiro 
dataset['Frequencia_Podas'] = dataset['Frequencia_Podas'] + 1;

print( 'ESTACOES COM VALORES DE FREQUENCIA PODAS NEGATIVOS', dataset[ dataset['Frequencia_Podas'] <= 0 ]['Estacao_Ano'].unique() )

"""
Porém ao fazer isso percebi outro fato interessante
Se com o valor de Frequencia_Podas do jeito que está, em todas as estações do ano tinham valores menores que zero,
MAIS AGORA EU COLOQUEI dataset['Frequencia_Podas'] + 1, ou seja APENAS SOMEEI 1, E SUMIU
Apenas apenas o ['Inverno' 'Outono'] tem valores negativos na coluna Frequencia_Podas

Isso significa que, nas outras, Primavera, Verão, etc... os valores podiam ser -1 ou 0,... mais ao colocar +1, o valor -1 passou a ser zero, e o valor 1 passou a ser 2, o que separou por completo
"""

print(dataset[ dataset['Frequencia_Podas'] <= 0 ]['Frequencia_Podas'])

"""
Analisando isso denovo, agora vejo que, as unicas estações do ano que tem valores negativos é o ['Inverno' 'Outono'], e esses valores são bem abaixo do normal
exemplo -71
agora fica facil de tratar

basta dizer que vai ser zero ou 1
vou escolher 1 para não fugir muito do padrão dos demais que tem frequencia de podas baixa
"""

# tratei isso
dataset.loc[ dataset['Frequencia_Podas'] < 0, 'Frequencia_Podas' ] = pd.Series(np.random.uniform(0.5, 1, size=len(dataset))); # Vou preencher com valores aleatorios entre 0.5 a 1

# AGORA FICOU ASSIM
print(dataset[ dataset['Frequencia_Podas'] <= 3 ]['Frequencia_Podas'])


"""
São 3000 amostras, 
DESSAS AINDA FALTA TRATAR AS COLUNAS:

Amostras com chuva negativo:
615

Altura:
668

Temperatura_C:
782
"""

"""
Primeiro vou verificar o Temperatura_C
"""

#print( 'ESTACOES COM VALORES DE Temperatura_C NEGATIVOS', dataset[ dataset['Temperatura_C'] <= 0 ]['Estacao_Ano'].unique() )

"""
Com o código acima vi que apenas o inverno tem valores negativos na coluna Temperatura_C
ai fica facil

Só no inverno tem valores menores que zero
"""

print(dataset[ dataset['Temperatura_C'] > 0]['Temperatura_C'].min())

"""
E pegando só os maiores que zero, o menor valor positivo é 5.0068111465476655
então eu preciso tratar em torno disso
"""

print( 'ESTACOES COM VALORES DE Temperatura_C NEGATIVOS', dataset[ dataset['Temperatura_C'] < 5.0068111465476655 ]['Estacao_Ano'].unique() )

"""
Confirmando que acima de 5.0068111465476655, começa a ter nas estações primavera,
mais 5.0068111465476655 ou abaixo só tem no inverno

Porém igual a 5.0068111465476655 existe na primavera
só abaixo de 5.0068111465476655 que não existe
então esse é meu limite, eu preciso ser abaixo disso pra nao gerar colisão

Então basta eu tratar
"""

# tratei isso
dataset.loc[ dataset['Temperatura_C'] < 5.0068111465476655, 'Temperatura_C' ] = pd.Series(np.random.uniform(2.0068111465476655, 4.0068111465476655, size=len(dataset))); # Vou preencher com valores aleatorios entre 0.5 a 1

# AGORA FICOU ASSIM
print(dataset[ dataset['Temperatura_C'] <= 0 ]['Temperatura_C'])

"""
Não aparece mais nada, e isso esta otimo
"""

print(dataset[ dataset['Temperatura_C'] <= 5.0068111465476655 ]['Temperatura_C'])

"""
o código acima mostrou oque eu queria que ele mostrasse
"""

"""
São 3000 amostras, 
DESSAS AINDA FALTA TRATAR AS COLUNAS:

Amostras com chuva negativo:
615

Altura:
668


IDEIA FAZER TAMBEM: Tratar o numero de pragas, pra ao invez de ser zero no inverno, ser a metade do valor minimo positivo, pra ficar na mesma proporção

"""


