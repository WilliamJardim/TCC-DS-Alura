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

"""
Pronto,
porém, falta eu verificar os valores minimos, maximos e media, para ver se faz sentido em cada estação do ano
"""
# qual a média da Horas_Sol_Dia na primavera
print( 'MIN Horas_Sol_Dia PRIMAVERA', dataset[ dataset['Estacao_Ano'] == 'Primavera' ]['Horas_Sol_Dia'].min() ) 
print( 'MEDIA Horas_Sol_Dia PRIMAVERA', dataset[ dataset['Estacao_Ano'] == 'Primavera' ]['Horas_Sol_Dia'].mean() ) 
print( 'MAX Horas_Sol_Dia PRIMAVERA', dataset[ dataset['Estacao_Ano'] == 'Primavera' ]['Horas_Sol_Dia'].max() ) 

print('')

# qual a média de Horas_Sol_Dia no verao
print( 'MIN Horas_Sol_Dia VERAO', dataset[ dataset['Estacao_Ano'] == 'Verão' ]['Horas_Sol_Dia'].min() ) 
print( 'MEDIA Horas_Sol_Dia VERAO', dataset[ dataset['Estacao_Ano'] == 'Verão' ]['Horas_Sol_Dia'].mean() ) 
print( 'MAX Horas_Sol_Dia VERAO', dataset[ dataset['Estacao_Ano'] == 'Verão' ]['Horas_Sol_Dia'].max() ) 

print('')

# qual a média de Horas_Sol_Dia no outono
print( 'MIN Horas_Sol_Dia OUTONO', dataset[ dataset['Estacao_Ano'] == 'Outono' ]['Horas_Sol_Dia'].min() ) 
print( 'MEDIA Horas_Sol_Dia OUTONO', dataset[ dataset['Estacao_Ano'] == 'Outono' ]['Horas_Sol_Dia'].mean() ) 
print( 'MAX Horas_Sol_Dia OUTONO', dataset[ dataset['Estacao_Ano'] == 'Outono' ]['Horas_Sol_Dia'].max() ) 

print('')

# qual a média de Horas_Sol_Dia no inverno
print( 'MIN Horas_Sol_Dia INVERNO', dataset[ dataset['Estacao_Ano'] == 'Inverno' ]['Horas_Sol_Dia'].min() ) 
print( 'MEDIA Horas_Sol_Dia INVERNO', dataset[ dataset['Estacao_Ano'] == 'Inverno' ]['Horas_Sol_Dia'].mean() ) 
print( 'MAX Horas_Sol_Dia INVERNO', dataset[ dataset['Estacao_Ano'] == 'Inverno' ]['Horas_Sol_Dia'].max() ) 

print('')

"""
Porém, analisando esses valores, percebi algo que ainda não faz sentido

MIN Horas_Sol_Dia OUTONO 1.5005594747373239
MEDIA Horas_Sol_Dia OUTONO 1.9640365241393454
MAX Horas_Sol_Dia OUTONO 3.982275102560518

MIN Horas_Sol_Dia INVERNO 1.500324724712552
MEDIA Horas_Sol_Dia INVERNO 1.7620781195197066
MAX Horas_Sol_Dia INVERNO 1.9990466102917446

Preciso aumentar um pouco mais o valor do outono, pra não ter uma diferença tão grotesca

Note tambem que o maximo de horas de sol no inverno é maior que no outono. As horas de sol no inverno deveriam ser menores que no outono

Pra isso, uma estrategia que eu pensei foi: aumentar outono e inverno na mesma proporção, e depois, reduzir só no inverno

"""

# Aumentando nos dois
dataset.loc[dataset['Estacao_Ano'] == 'Outono', 'Horas_Sol_Dia'] += 7
dataset.loc[dataset['Estacao_Ano'] == 'Inverno', 'Horas_Sol_Dia'] += 7

# Reduzindo só no inverno
dataset.loc[dataset['Estacao_Ano'] == 'Inverno', 'Horas_Sol_Dia'] -= 6.5

print('\nAPÒS AJUSTAR HORAS DO SOL');
# qual a média da Horas_Sol_Dia na primavera
print( 'MIN Horas_Sol_Dia PRIMAVERA', dataset[ dataset['Estacao_Ano'] == 'Primavera' ]['Horas_Sol_Dia'].min() ) 
print( 'MEDIA Horas_Sol_Dia PRIMAVERA', dataset[ dataset['Estacao_Ano'] == 'Primavera' ]['Horas_Sol_Dia'].mean() ) 
print( 'MAX Horas_Sol_Dia PRIMAVERA', dataset[ dataset['Estacao_Ano'] == 'Primavera' ]['Horas_Sol_Dia'].max() ) 

print('')

# qual a média de Horas_Sol_Dia no verao
print( 'MIN Horas_Sol_Dia VERAO', dataset[ dataset['Estacao_Ano'] == 'Verão' ]['Horas_Sol_Dia'].min() ) 
print( 'MEDIA Horas_Sol_Dia VERAO', dataset[ dataset['Estacao_Ano'] == 'Verão' ]['Horas_Sol_Dia'].mean() ) 
print( 'MAX Horas_Sol_Dia VERAO', dataset[ dataset['Estacao_Ano'] == 'Verão' ]['Horas_Sol_Dia'].max() ) 

print('')

# qual a média de Horas_Sol_Dia no outono
print( 'MIN Horas_Sol_Dia OUTONO', dataset[ dataset['Estacao_Ano'] == 'Outono' ]['Horas_Sol_Dia'].min() ) 
print( 'MEDIA Horas_Sol_Dia OUTONO', dataset[ dataset['Estacao_Ano'] == 'Outono' ]['Horas_Sol_Dia'].mean() ) 
print( 'MAX Horas_Sol_Dia OUTONO', dataset[ dataset['Estacao_Ano'] == 'Outono' ]['Horas_Sol_Dia'].max() ) 

print('')

# qual a média de Horas_Sol_Dia no inverno
print( 'MIN Horas_Sol_Dia INVERNO', dataset[ dataset['Estacao_Ano'] == 'Inverno' ]['Horas_Sol_Dia'].min() ) 
print( 'MEDIA Horas_Sol_Dia INVERNO', dataset[ dataset['Estacao_Ano'] == 'Inverno' ]['Horas_Sol_Dia'].mean() ) 
print( 'MAX Horas_Sol_Dia INVERNO', dataset[ dataset['Estacao_Ano'] == 'Inverno' ]['Horas_Sol_Dia'].max() ) 

print('')

"""
Ficou melhor,
porém, note:

APÒS AJUSTAR HORAS DO SOL
MIN Horas_Sol_Dia PRIMAVERA 3.001926996142932
MEDIA Horas_Sol_Dia PRIMAVERA 6.972479765927623
MAX Horas_Sol_Dia PRIMAVERA 10.996041517668132

MIN Horas_Sol_Dia VERAO 6.001261956624454
MEDIA Horas_Sol_Dia VERAO 10.115704342170375
MAX Horas_Sol_Dia VERAO 13.994680982648925

MIN Horas_Sol_Dia OUTONO 8.500559474737324
MEDIA Horas_Sol_Dia OUTONO 8.964036524139345
MAX Horas_Sol_Dia OUTONO 10.982275102560518

MIN Horas_Sol_Dia INVERNO 2.000324724712552
MEDIA Horas_Sol_Dia INVERNO 2.262078119519707
MAX Horas_Sol_Dia INVERNO 2.499046610291744

o valor do outono ainda é maior que no verão, mais na verdade, o verão é um pico, e o outono precisa seguir essa tendencia do verão porém reduzindo mais, para começar a entrar no ritmo de inverno

Na minha opinião, a média e valor máximo do outono está ótimo
só o valor minimo que ainda não está muito bom, pois preciso reduzir um pouco mais, pra se assemelhar ao verão
na minha opinião, poderia ser 5
"""

# Ajustei isso
media_horassol_primavera = dataset.loc[dataset['Estacao_Ano'] == 'Outono', 'Horas_Sol_Dia'].mean()
dataset.loc[(dataset['Estacao_Ano'] == 'Outono') & (dataset['Horas_Sol_Dia'] <= media_horassol_primavera), 'Horas_Sol_Dia'] -= 3

print('\nAPÒS AJUSTAR HORAS DO SOL');
# qual a média da Horas_Sol_Dia na primavera
print( 'MIN Horas_Sol_Dia PRIMAVERA', dataset[ dataset['Estacao_Ano'] == 'Primavera' ]['Horas_Sol_Dia'].min() ) 
print( 'MEDIA Horas_Sol_Dia PRIMAVERA', dataset[ dataset['Estacao_Ano'] == 'Primavera' ]['Horas_Sol_Dia'].mean() ) 
print( 'MAX Horas_Sol_Dia PRIMAVERA', dataset[ dataset['Estacao_Ano'] == 'Primavera' ]['Horas_Sol_Dia'].max() ) 

print('')

# qual a média de Horas_Sol_Dia no verao
print( 'MIN Horas_Sol_Dia VERAO', dataset[ dataset['Estacao_Ano'] == 'Verão' ]['Horas_Sol_Dia'].min() ) 
print( 'MEDIA Horas_Sol_Dia VERAO', dataset[ dataset['Estacao_Ano'] == 'Verão' ]['Horas_Sol_Dia'].mean() ) 
print( 'MAX Horas_Sol_Dia VERAO', dataset[ dataset['Estacao_Ano'] == 'Verão' ]['Horas_Sol_Dia'].max() ) 

print('')

# qual a média de Horas_Sol_Dia no outono
print( 'MIN Horas_Sol_Dia OUTONO', dataset[ dataset['Estacao_Ano'] == 'Outono' ]['Horas_Sol_Dia'].min() ) 
print( 'MEDIA Horas_Sol_Dia OUTONO', dataset[ dataset['Estacao_Ano'] == 'Outono' ]['Horas_Sol_Dia'].mean() ) 
print( 'MAX Horas_Sol_Dia OUTONO', dataset[ dataset['Estacao_Ano'] == 'Outono' ]['Horas_Sol_Dia'].max() ) 

print('')

# qual a média de Horas_Sol_Dia no inverno
print( 'MIN Horas_Sol_Dia INVERNO', dataset[ dataset['Estacao_Ano'] == 'Inverno' ]['Horas_Sol_Dia'].min() ) 
print( 'MEDIA Horas_Sol_Dia INVERNO', dataset[ dataset['Estacao_Ano'] == 'Inverno' ]['Horas_Sol_Dia'].mean() ) 
print( 'MAX Horas_Sol_Dia INVERNO', dataset[ dataset['Estacao_Ano'] == 'Inverno' ]['Horas_Sol_Dia'].max() ) 

print('')

"""
Ficou assim:
APÒS AJUSTAR HORAS DO SOL
MIN Horas_Sol_Dia PRIMAVERA 3.001926996142932
MEDIA Horas_Sol_Dia PRIMAVERA 6.972479765927623
MAX Horas_Sol_Dia PRIMAVERA 10.996041517668132

MIN Horas_Sol_Dia VERAO 6.001261956624454
MEDIA Horas_Sol_Dia VERAO 10.115704342170375
MAX Horas_Sol_Dia VERAO 13.994680982648925

MIN Horas_Sol_Dia OUTONO 5.500559474737324
MEDIA Horas_Sol_Dia OUTONO 6.540959601062422
MAX Horas_Sol_Dia OUTONO 10.982275102560518

MIN Horas_Sol_Dia INVERNO 2.000324724712552
MEDIA Horas_Sol_Dia INVERNO 2.262078119519707
MAX Horas_Sol_Dia INVERNO 2.499046610291744

Na minha opinião, duas mudanças ainda podem ser feitas aqui nessa coluna:

  (1) - Fazer as horas sol ser um pouquinho maior na primavera

  (2) - Aplicar um crescimento geral em todos eles na mesma proporção

  
Primeiro vou aumentar um pouquinho as horas de sol na primavera 
"""
dataset.loc[dataset['Estacao_Ano'] == 'Primavera', 'Horas_Sol_Dia'] += 0.4

print('\nAPÒS AJUSTAR HORAS DO SOL');
# qual a média da Horas_Sol_Dia na primavera
print( 'MIN Horas_Sol_Dia PRIMAVERA', dataset[ dataset['Estacao_Ano'] == 'Primavera' ]['Horas_Sol_Dia'].min() ) 
print( 'MEDIA Horas_Sol_Dia PRIMAVERA', dataset[ dataset['Estacao_Ano'] == 'Primavera' ]['Horas_Sol_Dia'].mean() ) 
print( 'MAX Horas_Sol_Dia PRIMAVERA', dataset[ dataset['Estacao_Ano'] == 'Primavera' ]['Horas_Sol_Dia'].max() ) 

print('')

# qual a média de Horas_Sol_Dia no verao
print( 'MIN Horas_Sol_Dia VERAO', dataset[ dataset['Estacao_Ano'] == 'Verão' ]['Horas_Sol_Dia'].min() ) 
print( 'MEDIA Horas_Sol_Dia VERAO', dataset[ dataset['Estacao_Ano'] == 'Verão' ]['Horas_Sol_Dia'].mean() ) 
print( 'MAX Horas_Sol_Dia VERAO', dataset[ dataset['Estacao_Ano'] == 'Verão' ]['Horas_Sol_Dia'].max() ) 

print('')

# qual a média de Horas_Sol_Dia no outono
print( 'MIN Horas_Sol_Dia OUTONO', dataset[ dataset['Estacao_Ano'] == 'Outono' ]['Horas_Sol_Dia'].min() ) 
print( 'MEDIA Horas_Sol_Dia OUTONO', dataset[ dataset['Estacao_Ano'] == 'Outono' ]['Horas_Sol_Dia'].mean() ) 
print( 'MAX Horas_Sol_Dia OUTONO', dataset[ dataset['Estacao_Ano'] == 'Outono' ]['Horas_Sol_Dia'].max() ) 

print('')

# qual a média de Horas_Sol_Dia no inverno
print( 'MIN Horas_Sol_Dia INVERNO', dataset[ dataset['Estacao_Ano'] == 'Inverno' ]['Horas_Sol_Dia'].min() ) 
print( 'MEDIA Horas_Sol_Dia INVERNO', dataset[ dataset['Estacao_Ano'] == 'Inverno' ]['Horas_Sol_Dia'].mean() ) 
print( 'MAX Horas_Sol_Dia INVERNO', dataset[ dataset['Estacao_Ano'] == 'Inverno' ]['Horas_Sol_Dia'].max() ) 

print('')

"""

APÒS AJUSTAR HORAS DO SOL
MIN Horas_Sol_Dia PRIMAVERA 3.4019269961429317
MEDIA Horas_Sol_Dia PRIMAVERA 7.372479765927625
MAX Horas_Sol_Dia PRIMAVERA 11.396041517668133

MIN Horas_Sol_Dia VERAO 6.001261956624454
MEDIA Horas_Sol_Dia VERAO 10.115704342170375
MAX Horas_Sol_Dia VERAO 13.994680982648925

MIN Horas_Sol_Dia OUTONO 5.500559474737324
MEDIA Horas_Sol_Dia OUTONO 6.540959601062422
MAX Horas_Sol_Dia OUTONO 10.982275102560518

MIN Horas_Sol_Dia INVERNO 2.000324724712552
MEDIA Horas_Sol_Dia INVERNO 2.262078119519707
MAX Horas_Sol_Dia INVERNO 2.499046610291744

agora sim faz muito mais sentido
mais os valores ainda estão muito baixos,

Agora posso aplicar minha segunda ideia de aumentar a proporção de todos PORÈM SEM REDUZIR MUITO O IMPACTO DO INVERNO E DO OUTONO
"""

# Tratei isso
dataset.loc[dataset['Estacao_Ano'] == 'Primavera', 'Horas_Sol_Dia'] += 12;
dataset.loc[dataset['Estacao_Ano'] == 'Verão', 'Horas_Sol_Dia'] += 15.8;
dataset.loc[dataset['Estacao_Ano'] == 'Outono', 'Horas_Sol_Dia'] += 10.8;
dataset.loc[dataset['Estacao_Ano'] == 'Inverno', 'Horas_Sol_Dia'] += 6;

print('\nAPÒS AJUSTAR HORAS DO SOL');
# qual a média da Horas_Sol_Dia na primavera
print( 'MIN Horas_Sol_Dia PRIMAVERA', dataset[ dataset['Estacao_Ano'] == 'Primavera' ]['Horas_Sol_Dia'].min() ) 
print( 'MEDIA Horas_Sol_Dia PRIMAVERA', dataset[ dataset['Estacao_Ano'] == 'Primavera' ]['Horas_Sol_Dia'].mean() ) 
print( 'MAX Horas_Sol_Dia PRIMAVERA', dataset[ dataset['Estacao_Ano'] == 'Primavera' ]['Horas_Sol_Dia'].max() ) 

print('')

# qual a média de Horas_Sol_Dia no verao
print( 'MIN Horas_Sol_Dia VERAO', dataset[ dataset['Estacao_Ano'] == 'Verão' ]['Horas_Sol_Dia'].min() ) 
print( 'MEDIA Horas_Sol_Dia VERAO', dataset[ dataset['Estacao_Ano'] == 'Verão' ]['Horas_Sol_Dia'].mean() ) 
print( 'MAX Horas_Sol_Dia VERAO', dataset[ dataset['Estacao_Ano'] == 'Verão' ]['Horas_Sol_Dia'].max() ) 

print('')

# qual a média de Horas_Sol_Dia no outono
print( 'MIN Horas_Sol_Dia OUTONO', dataset[ dataset['Estacao_Ano'] == 'Outono' ]['Horas_Sol_Dia'].min() ) 
print( 'MEDIA Horas_Sol_Dia OUTONO', dataset[ dataset['Estacao_Ano'] == 'Outono' ]['Horas_Sol_Dia'].mean() ) 
print( 'MAX Horas_Sol_Dia OUTONO', dataset[ dataset['Estacao_Ano'] == 'Outono' ]['Horas_Sol_Dia'].max() ) 

print('')

# qual a média de Horas_Sol_Dia no inverno
print( 'MIN Horas_Sol_Dia INVERNO', dataset[ dataset['Estacao_Ano'] == 'Inverno' ]['Horas_Sol_Dia'].min() ) 
print( 'MEDIA Horas_Sol_Dia INVERNO', dataset[ dataset['Estacao_Ano'] == 'Inverno' ]['Horas_Sol_Dia'].mean() ) 
print( 'MAX Horas_Sol_Dia INVERNO', dataset[ dataset['Estacao_Ano'] == 'Inverno' ]['Horas_Sol_Dia'].max() ) 

print('')

"""
Agora fez muito mais sentido
"""


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
Fez mais sentido,
porém ainda preciso verificar as médias, valores minimos e valores maximos para garantir que a faixa dos valores façam sentido
"""
# qual a média da Frequencia_Podas na primavera
print( 'MIN Frequencia_Podas PRIMAVERA', dataset[ dataset['Estacao_Ano'] == 'Primavera' ]['Frequencia_Podas'].min() ) 
print( 'MEDIA Frequencia_Podas PRIMAVERA', dataset[ dataset['Estacao_Ano'] == 'Primavera' ]['Frequencia_Podas'].mean() ) 
print( 'MAX Frequencia_Podas PRIMAVERA', dataset[ dataset['Estacao_Ano'] == 'Primavera' ]['Frequencia_Podas'].max() ) 

print('')

# qual a média de Frequencia_Podas no verao
print( 'MIN Frequencia_Podas VERAO', dataset[ dataset['Estacao_Ano'] == 'Verão' ]['Frequencia_Podas'].min() ) 
print( 'MEDIA Frequencia_Podas VERAO', dataset[ dataset['Estacao_Ano'] == 'Verão' ]['Frequencia_Podas'].mean() ) 
print( 'MAX Frequencia_Podas VERAO', dataset[ dataset['Estacao_Ano'] == 'Verão' ]['Frequencia_Podas'].max() ) 

print('')

# qual a média de Frequencia_Podas no outono
print( 'MIN Frequencia_Podas OUTONO', dataset[ dataset['Estacao_Ano'] == 'Outono' ]['Frequencia_Podas'].min() ) 
print( 'MEDIA Frequencia_Podas OUTONO', dataset[ dataset['Estacao_Ano'] == 'Outono' ]['Frequencia_Podas'].mean() ) 
print( 'MAX Frequencia_Podas OUTONO', dataset[ dataset['Estacao_Ano'] == 'Outono' ]['Frequencia_Podas'].max() ) 

print('')

# qual a média de Frequencia_Podas no inverno
print( 'MIN Frequencia_Podas INVERNO', dataset[ dataset['Estacao_Ano'] == 'Inverno' ]['Frequencia_Podas'].min() ) 
print( 'MEDIA Frequencia_Podas INVERNO', dataset[ dataset['Estacao_Ano'] == 'Inverno' ]['Frequencia_Podas'].mean() ) 
print( 'MAX Frequencia_Podas INVERNO', dataset[ dataset['Estacao_Ano'] == 'Inverno' ]['Frequencia_Podas'].max() ) 

print('')

"""
Na minha opinião não preciso mexer mais nisso, já está bom
Não tem muito a ver com o tempo, mais mesmo assim, o padrão de no outono e inverno ficar menor foi aplicado
"""

"""
Porém veja:

MIN Frequencia_Podas PRIMAVERA 1.0
MEDIA Frequencia_Podas PRIMAVERA 5.559681697612732
MAX Frequencia_Podas PRIMAVERA 10.0

MIN Frequencia_Podas VERAO 1.0
MEDIA Frequencia_Podas VERAO 5.430706521739131
MAX Frequencia_Podas VERAO 10.0

MIN Frequencia_Podas OUTONO 0.5
MEDIA Frequencia_Podas OUTONO 2.1416925178976043
MAX Frequencia_Podas OUTONO 5.5

MIN Frequencia_Podas INVERNO 0.5002815696779608
MEDIA Frequencia_Podas INVERNO 0.7523202206862205
MAX Frequencia_Podas INVERNO 0.9979648323438057

Eu acho que não deveriam existir valores como 0.5, 0.7, deveria ser no minimo 1
"""

# Tratei isso
dataset['Frequencia_Podas'] = dataset['Frequencia_Podas'] + 1;

print('\nAPOS TRATAR O FREQUENCIA PODAS')
# qual a média da Frequencia_Podas na primavera
print( 'MIN Frequencia_Podas PRIMAVERA', dataset[ dataset['Estacao_Ano'] == 'Primavera' ]['Frequencia_Podas'].min() ) 
print( 'MEDIA Frequencia_Podas PRIMAVERA', dataset[ dataset['Estacao_Ano'] == 'Primavera' ]['Frequencia_Podas'].mean() ) 
print( 'MAX Frequencia_Podas PRIMAVERA', dataset[ dataset['Estacao_Ano'] == 'Primavera' ]['Frequencia_Podas'].max() ) 

print('')

# qual a média de Frequencia_Podas no verao
print( 'MIN Frequencia_Podas VERAO', dataset[ dataset['Estacao_Ano'] == 'Verão' ]['Frequencia_Podas'].min() ) 
print( 'MEDIA Frequencia_Podas VERAO', dataset[ dataset['Estacao_Ano'] == 'Verão' ]['Frequencia_Podas'].mean() ) 
print( 'MAX Frequencia_Podas VERAO', dataset[ dataset['Estacao_Ano'] == 'Verão' ]['Frequencia_Podas'].max() ) 

print('')

# qual a média de Frequencia_Podas no outono
print( 'MIN Frequencia_Podas OUTONO', dataset[ dataset['Estacao_Ano'] == 'Outono' ]['Frequencia_Podas'].min() ) 
print( 'MEDIA Frequencia_Podas OUTONO', dataset[ dataset['Estacao_Ano'] == 'Outono' ]['Frequencia_Podas'].mean() ) 
print( 'MAX Frequencia_Podas OUTONO', dataset[ dataset['Estacao_Ano'] == 'Outono' ]['Frequencia_Podas'].max() ) 

print('')

# qual a média de Frequencia_Podas no inverno
print( 'MIN Frequencia_Podas INVERNO', dataset[ dataset['Estacao_Ano'] == 'Inverno' ]['Frequencia_Podas'].min() ) 
print( 'MEDIA Frequencia_Podas INVERNO', dataset[ dataset['Estacao_Ano'] == 'Inverno' ]['Frequencia_Podas'].mean() ) 
print( 'MAX Frequencia_Podas INVERNO', dataset[ dataset['Estacao_Ano'] == 'Inverno' ]['Frequencia_Podas'].max() ) 

print('')

"""
Na minha opinião ficou muito melhor 
"""


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
Porém, ainda dá pra verificar se as médias, valores minimos e máximos estão adequados
"""
# qual a média da Temperatura_C na primavera
print( 'MIN Temperatura_C PRIMAVERA', dataset[ dataset['Estacao_Ano'] == 'Primavera' ]['Temperatura_C'].min() ) 
print( 'MEDIA Temperatura_C PRIMAVERA', dataset[ dataset['Estacao_Ano'] == 'Primavera' ]['Temperatura_C'].mean() ) 
print( 'MAX Temperatura_C PRIMAVERA', dataset[ dataset['Estacao_Ano'] == 'Primavera' ]['Temperatura_C'].max() ) 

print('')

# qual a média de Temperatura_C no verao
print( 'MIN Temperatura_C VERAO', dataset[ dataset['Estacao_Ano'] == 'Verão' ]['Temperatura_C'].min() ) 
print( 'MEDIA Temperatura_C VERAO', dataset[ dataset['Estacao_Ano'] == 'Verão' ]['Temperatura_C'].mean() ) 
print( 'MAX Temperatura_C VERAO', dataset[ dataset['Estacao_Ano'] == 'Verão' ]['Temperatura_C'].max() ) 

print('')

# qual a média de Temperatura_C no outono
print( 'MIN Temperatura_C OUTONO', dataset[ dataset['Estacao_Ano'] == 'Outono' ]['Temperatura_C'].min() ) 
print( 'MEDIA Temperatura_C OUTONO', dataset[ dataset['Estacao_Ano'] == 'Outono' ]['Temperatura_C'].mean() ) 
print( 'MAX Temperatura_C OUTONO', dataset[ dataset['Estacao_Ano'] == 'Outono' ]['Temperatura_C'].max() ) 

print('')

# qual a média de Temperatura_C no inverno
print( 'MIN Temperatura_C INVERNO', dataset[ dataset['Estacao_Ano'] == 'Inverno' ]['Temperatura_C'].min() ) 
print( 'MEDIA Temperatura_C INVERNO', dataset[ dataset['Estacao_Ano'] == 'Inverno' ]['Temperatura_C'].mean() ) 
print( 'MAX Temperatura_C INVERNO', dataset[ dataset['Estacao_Ano'] == 'Inverno' ]['Temperatura_C'].max() ) 

print('')

"""
Na minha opinião, o valor minino na primavera poderia ser um só um pouquinho maior, pra ficar um pouco mais calor que no inverno
"""

media_temperatura_primavera = dataset.loc[dataset['Estacao_Ano'] == 'Primavera', 'Temperatura_C'].mean()
dataset.loc[(dataset['Estacao_Ano'] == 'Primavera') & (dataset['Temperatura_C'] <= media_temperatura_primavera), 'Temperatura_C'] += 3

print('\nAPÒS AJUSTAR A TEMPERATURA MINIMA NA PRIMAVERA')
# qual a média da Temperatura_C na primavera
print( 'MIN Temperatura_C PRIMAVERA', dataset[ dataset['Estacao_Ano'] == 'Primavera' ]['Temperatura_C'].min() ) 
print( 'MEDIA Temperatura_C PRIMAVERA', dataset[ dataset['Estacao_Ano'] == 'Primavera' ]['Temperatura_C'].mean() ) 
print( 'MAX Temperatura_C PRIMAVERA', dataset[ dataset['Estacao_Ano'] == 'Primavera' ]['Temperatura_C'].max() ) 

print('')

# qual a média de Temperatura_C no verao
print( 'MIN Temperatura_C VERAO', dataset[ dataset['Estacao_Ano'] == 'Verão' ]['Temperatura_C'].min() ) 
print( 'MEDIA Temperatura_C VERAO', dataset[ dataset['Estacao_Ano'] == 'Verão' ]['Temperatura_C'].mean() ) 
print( 'MAX Temperatura_C VERAO', dataset[ dataset['Estacao_Ano'] == 'Verão' ]['Temperatura_C'].max() ) 

print('')

# qual a média de Temperatura_C no outono
print( 'MIN Temperatura_C OUTONO', dataset[ dataset['Estacao_Ano'] == 'Outono' ]['Temperatura_C'].min() ) 
print( 'MEDIA Temperatura_C OUTONO', dataset[ dataset['Estacao_Ano'] == 'Outono' ]['Temperatura_C'].mean() ) 
print( 'MAX Temperatura_C OUTONO', dataset[ dataset['Estacao_Ano'] == 'Outono' ]['Temperatura_C'].max() ) 

print('')

# qual a média de Temperatura_C no inverno
print( 'MIN Temperatura_C INVERNO', dataset[ dataset['Estacao_Ano'] == 'Inverno' ]['Temperatura_C'].min() ) 
print( 'MEDIA Temperatura_C INVERNO', dataset[ dataset['Estacao_Ano'] == 'Inverno' ]['Temperatura_C'].mean() ) 
print( 'MAX Temperatura_C INVERNO', dataset[ dataset['Estacao_Ano'] == 'Inverno' ]['Temperatura_C'].max() ) 

print('\n')

"""
APÒS AJUSTAR A TEMPERATURA MINIMA NA PRIMAVERA:

MIN Temperatura_C PRIMAVERA 8.006811146547665
MEDIA Temperatura_C PRIMAVERA 21.309430574536954
MAX Temperatura_C PRIMAVERA 34.98382043179019

MIN Temperatura_C VERAO 20.01793816504386
MEDIA Temperatura_C VERAO 34.547941191212715
MAX Temperatura_C VERAO 49.98673109751316

MIN Temperatura_C OUTONO 6.000921565361473
MEDIA Temperatura_C OUTONO 20.680503386573164
MAX Temperatura_C OUTONO 35.930167897939775

MIN Temperatura_C INVERNO 2.0072182893117967
MEDIA Temperatura_C INVERNO 2.96505561731765
MAX Temperatura_C INVERNO 4.006060728518891

Agora fez muito mais sentido
"""

"""
Porém, eu notei isso:

APÒS AJUSTAR A TEMPERATURA MINIMA NA PRIMAVERA
MIN Temperatura_C PRIMAVERA 8.006811146547665
MEDIA Temperatura_C PRIMAVERA 21.309430574536954
MAX Temperatura_C PRIMAVERA 34.98382043179019

MIN Temperatura_C VERAO 20.01793816504386
MEDIA Temperatura_C VERAO 34.547941191212715
MAX Temperatura_C VERAO 49.98673109751316

MIN Temperatura_C OUTONO 6.000921565361473
MEDIA Temperatura_C OUTONO 20.680503386573164
MAX Temperatura_C OUTONO 35.930167897939775

MIN Temperatura_C INVERNO 2.0072182893117967
MEDIA Temperatura_C INVERNO 2.96505561731765
MAX Temperatura_C INVERNO 4.006060728518891

Note que, o minino do outono é 6.000921565361473, e o minimo do verão é 20.01793816504386, são valores muito distantes, uma mudança muita brusca repetina
eu preciso suavilizar um pouco mais essa transição,

e manter o padrão do inverno muito abaixo

"""

# Tratei o outono
media_temperatura_outono = dataset.loc[dataset['Estacao_Ano'] == 'Outono', 'Temperatura_C'].mean()
dataset.loc[(dataset['Estacao_Ano'] == 'Outono') & (dataset['Temperatura_C'] <= media_temperatura_outono), 'Temperatura_C'] += 2.6

# Aumentei só um pouquino mais o outono em geral tambem
dataset.loc[dataset['Estacao_Ano'] == 'Outono', 'Temperatura_C'] += 1.2

# Aumentei só um pouquino mais o inverno tambem
dataset.loc[dataset['Estacao_Ano'] == 'Inverno', 'Temperatura_C'] += 1.8

print('\nAPÒS AJUSTAR A TEMPERATURA MINIMA NA PRIMAVERA')
# qual a média da Temperatura_C na primavera
print( 'MIN Temperatura_C PRIMAVERA', dataset[ dataset['Estacao_Ano'] == 'Primavera' ]['Temperatura_C'].min() ) 
print( 'MEDIA Temperatura_C PRIMAVERA', dataset[ dataset['Estacao_Ano'] == 'Primavera' ]['Temperatura_C'].mean() ) 
print( 'MAX Temperatura_C PRIMAVERA', dataset[ dataset['Estacao_Ano'] == 'Primavera' ]['Temperatura_C'].max() ) 

print('')

# qual a média de Temperatura_C no verao
print( 'MIN Temperatura_C VERAO', dataset[ dataset['Estacao_Ano'] == 'Verão' ]['Temperatura_C'].min() ) 
print( 'MEDIA Temperatura_C VERAO', dataset[ dataset['Estacao_Ano'] == 'Verão' ]['Temperatura_C'].mean() ) 
print( 'MAX Temperatura_C VERAO', dataset[ dataset['Estacao_Ano'] == 'Verão' ]['Temperatura_C'].max() ) 

print('')

# qual a média de Temperatura_C no outono
print( 'MIN Temperatura_C OUTONO', dataset[ dataset['Estacao_Ano'] == 'Outono' ]['Temperatura_C'].min() ) 
print( 'MEDIA Temperatura_C OUTONO', dataset[ dataset['Estacao_Ano'] == 'Outono' ]['Temperatura_C'].mean() ) 
print( 'MAX Temperatura_C OUTONO', dataset[ dataset['Estacao_Ano'] == 'Outono' ]['Temperatura_C'].max() ) 

print('')

# qual a média de Temperatura_C no inverno
print( 'MIN Temperatura_C INVERNO', dataset[ dataset['Estacao_Ano'] == 'Inverno' ]['Temperatura_C'].min() ) 
print( 'MEDIA Temperatura_C INVERNO', dataset[ dataset['Estacao_Ano'] == 'Inverno' ]['Temperatura_C'].mean() ) 
print( 'MAX Temperatura_C INVERNO', dataset[ dataset['Estacao_Ano'] == 'Inverno' ]['Temperatura_C'].max() ) 

print('\n')

"""
Ficou um pouco melhor agora:

APÒS AJUSTAR A TEMPERATURA MINIMA NA PRIMAVERA
MIN Temperatura_C PRIMAVERA 8.006811146547665
MEDIA Temperatura_C PRIMAVERA 21.309430574536954
MAX Temperatura_C PRIMAVERA 34.98382043179019

MIN Temperatura_C VERAO 20.01793816504386
MEDIA Temperatura_C VERAO 34.547941191212715
MAX Temperatura_C VERAO 49.98673109751316

MIN Temperatura_C OUTONO 9.800921565361472
MEDIA Temperatura_C OUTONO 23.19836052943031
MAX Temperatura_C OUTONO 37.13016789793978

MIN Temperatura_C INVERNO 3.8072182893117965
MEDIA Temperatura_C INVERNO 4.76505561731765
MAX Temperatura_C INVERNO 5.806060728518891

Faz muito mais sentido
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

"""
Vou ver a coluna Chuva_mm
"""

print( 'ESTACOES COM VALORES DE Chuva_mm NEGATIVOS', dataset[ dataset['Chuva_mm'] <= 0 ]['Estacao_Ano'].unique() )

"""
o código acima não dá pra tratar dessa forma por que a primavera tem valores negativos tambem
eu posso tentar fazer o teste do +1, ou tentar aquela outra ideia minha: aumentar a escala pra todos os valores ficarem maior que zero, ai eu idenficar o valor que posso usar pra separar, e reduzir a escala denovo
"""

print('MIN/ME/MAX Chuva_mm antes de somar', dataset[ dataset['Chuva_mm'] > 0]['Chuva_mm'].min(), dataset[ dataset['Chuva_mm'] > 0]['Chuva_mm'].median(), dataset[ dataset['Chuva_mm'] > 0]['Chuva_mm'].max())

dataset['Chuva_mm'] = dataset['Chuva_mm'] + 25;

print( 'ESTACOES COM VALORES DE FREQUENCIA PODAS NEGATIVOS', dataset[ dataset['Chuva_mm'] <= 0 ]['Estacao_Ano'].unique() )

"""
Eu fiz varios testes somando valores, somei 22, 24, e todos davam primavera tambem
agora eu somei por ultimo +25,.. e ai a primavera sumiu

isso significa que ao somar 25, o valor negativo ficou zero, provavelmente por que poderia ser -25,....., ai deixou de existir valores menores do que zero na primavera, isolando totalmente o inverno com os valores negativos ficando apenas no inverno
não existe nenhum valor em outras estações nessa faixa

Então somar 25 é um bom limiar pra eu me basear para tratar o Chuva_mm
"""

print('MIN/ME/MAX Chuva_mm depois de somar', dataset[ dataset['Chuva_mm'] > 0]['Chuva_mm'].min(), dataset[ dataset['Chuva_mm'] > 0]['Chuva_mm'].median(), dataset[ dataset['Chuva_mm'] > 0]['Chuva_mm'].max())

"""
Dos valores da coluna Chuva_mm que são maiores que zero somente:

  Min: 0.01056538645935845 
  Median: 123.3116100646548 
  Max: 274.1604735559837

Dá pra ver que, 
"""

# Quais as estações do ano que tem amostras que cuja Chuva_mm seja menor que o minimo dos positivos
print( dataset[ dataset['Chuva_mm'] < 0.01056538645935845 ]['Estacao_Ano'].unique() ) 

# Quantas amostras que cuja Chuva_mm seja menor que o minimo dos positivos
print( dataset[ dataset['Chuva_mm'] < 0.01056538645935845 ]['Estacao_Ano'].count() )

# Quantas amostras que cuja Chuva_mm seja menor OU IGUAL que o minimo dos positivos
print( dataset[ dataset['Chuva_mm'] <= 0.01056538645935845 ]['Estacao_Ano'].count() )


# qual a média de chuvas no inverno
print( 'MIN CHUVAS INVERNO', dataset[ dataset['Estacao_Ano'] == 'Inverno' ]['Chuva_mm'].min() ) 
print( 'MEDIA CHUVAS INVERNO', dataset[ dataset['Estacao_Ano'] == 'Inverno' ]['Chuva_mm'].mean() ) 
print( 'MAX CHUVAS INVERNO', dataset[ dataset['Estacao_Ano'] == 'Inverno' ]['Chuva_mm'].max() ) 

print('')

# qual a média da chuva na primavera
print( 'MIN CHUVAS PRIMAVERA', dataset[ dataset['Estacao_Ano'] == 'Primavera' ]['Chuva_mm'].min() ) 
print( 'MEDIA CHUVAS PRIMAVERA', dataset[ dataset['Estacao_Ano'] == 'Primavera' ]['Chuva_mm'].mean() ) 
print( 'MAX CHUVAS PRIMAVERA', dataset[ dataset['Estacao_Ano'] == 'Primavera' ]['Chuva_mm'].max() ) 

print('')

# qual a média de chuvas no outono
print( 'MIN CHUVAS OUTONO', dataset[ dataset['Estacao_Ano'] == 'Outono' ]['Chuva_mm'].min() ) 
print( 'MEDIA CHUVAS OUTONO', dataset[ dataset['Estacao_Ano'] == 'Outono' ]['Chuva_mm'].mean() ) 
print( 'MAX CHUVAS OUTONO', dataset[ dataset['Estacao_Ano'] == 'Outono' ]['Chuva_mm'].max() ) 

print('')

# qual a média de chuvas no verao
print( 'MIN CHUVAS VERAO', dataset[ dataset['Estacao_Ano'] == 'Verão' ]['Chuva_mm'].min() ) 
print( 'MEDIA CHUVAS VERAO', dataset[ dataset['Estacao_Ano'] == 'Verão' ]['Chuva_mm'].mean() ) 
print( 'MAX CHUVAS VERAO', dataset[ dataset['Estacao_Ano'] == 'Verão' ]['Chuva_mm'].max() ) 

print('')

"""
Eu posso mudar o maximo de chuvas no inverno pra ser mais baixo
"""

# Quais as estações do ano que tem amostras que cuja Chuva_mm seja menor que o maximo
print( dataset[ dataset['Chuva_mm'] < 94.72346383287694 ]['Estacao_Ano'].unique() ) 

# tratei isso
import random
random.seed(45);

# Soma 50 aos valores negativos no inverno
dataset.loc[(dataset['Estacao_Ano'] == 'Inverno') & (dataset['Chuva_mm'] < 0), 'Chuva_mm'] += 150

# O .apply(lambda x: min(x, 60)) garante que nenhum valor de inverno Chuvas_mm ultrapasse 60, pra criar uma distinção clara.
#dataset.loc[dataset['Estacao_Ano'] == 'Inverno', 'Chuva_mm'] = dataset.loc[dataset['Estacao_Ano'] == 'Inverno', 'Chuva_mm'].apply(lambda x: min(x, random.randint(50, 65) ))
dataset.loc[(dataset['Estacao_Ano'] == 'Inverno') & (dataset['Chuva_mm'] > 0), 'Chuva_mm'] = dataset.loc[(dataset['Estacao_Ano'] == 'Inverno') & (dataset['Chuva_mm'] > 0), 'Chuva_mm'].apply(lambda x: min(x, random.randint(1, 5)))


"""
Agora posso ver como ficou
"""
print('\nAPÒS TRATAR Chuva_mm:')

# qual a média da chuva na primavera
print( 'MIN CHUVAS PRIMAVERA', dataset[ dataset['Estacao_Ano'] == 'Primavera' ]['Chuva_mm'].min() ) 
print( 'MEDIA CHUVAS PRIMAVERA', dataset[ dataset['Estacao_Ano'] == 'Primavera' ]['Chuva_mm'].mean() ) 
print( 'MAX CHUVAS PRIMAVERA', dataset[ dataset['Estacao_Ano'] == 'Primavera' ]['Chuva_mm'].max() ) 

print('')

# qual a média de chuvas no verao
print( 'MIN CHUVAS VERAO', dataset[ dataset['Estacao_Ano'] == 'Verão' ]['Chuva_mm'].min() ) 
print( 'MEDIA CHUVAS VERAO', dataset[ dataset['Estacao_Ano'] == 'Verão' ]['Chuva_mm'].mean() ) 
print( 'MAX CHUVAS VERAO', dataset[ dataset['Estacao_Ano'] == 'Verão' ]['Chuva_mm'].max() ) 

print('')

# qual a média de chuvas no outono
print( 'MIN CHUVAS OUTONO', dataset[ dataset['Estacao_Ano'] == 'Outono' ]['Chuva_mm'].min() ) 
print( 'MEDIA CHUVAS OUTONO', dataset[ dataset['Estacao_Ano'] == 'Outono' ]['Chuva_mm'].mean() ) 
print( 'MAX CHUVAS OUTONO', dataset[ dataset['Estacao_Ano'] == 'Outono' ]['Chuva_mm'].max() ) 

print('')

# qual a média de chuvas no inverno
print( 'MIN CHUVAS INVERNO', dataset[ dataset['Estacao_Ano'] == 'Inverno' ]['Chuva_mm'].min() ) 
print( 'MEDIA CHUVAS INVERNO', dataset[ dataset['Estacao_Ano'] == 'Inverno' ]['Chuva_mm'].mean() ) 
print( 'MAX CHUVAS INVERNO', dataset[ dataset['Estacao_Ano'] == 'Inverno' ]['Chuva_mm'].max() ) 

print('')


"""
APÒS TRATAR Chuva_mm:
MIN CHUVAS PRIMAVERA 0.01056538645935845
MEDIA CHUVAS PRIMAVERA 98.45893415159796
MAX CHUVAS PRIMAVERA 199.33665558693593

MIN CHUVAS VERAO 75.0482009370269
MEDIA CHUVAS VERAO 171.54992011055597
MAX CHUVAS VERAO 274.1604735559837

MIN CHUVAS OUTONO 45.78566861583535
MEDIA CHUVAS OUTONO 145.23948704815433
MAX CHUVAS OUTONO 245.34145978868816

MIN CHUVAS INVERNO 0.0863996619284535
MEDIA CHUVAS INVERNO 3.010665260206797
MAX CHUVAS INVERNO 5.0

Agora fez muito mais sentido!, não existe mais chuva negativa, e no inverno é bem menor
"""

"""
Só fiz mais um ajuste para que o minino no inverno não seja 0
"""

media_chuvas_inverno = dataset.loc[dataset['Estacao_Ano'] == 'Inverno', 'Chuva_mm'].mean()
dataset.loc[(dataset['Estacao_Ano'] == 'Inverno') & (dataset['Chuva_mm'] <= media_chuvas_inverno), 'Chuva_mm'] += 2


"""
Porém, o valor de chuvas minimo da primavera foi menor que a do inverno, e isso não faz sentido
o valor minimo de chuvas da primavera precisa ser maior que o minimo do inverno

Vou ajustar isso:
"""

media_chuvas_primavera = dataset.loc[dataset['Estacao_Ano'] == 'Primavera', 'Chuva_mm'].mean()
dataset.loc[(dataset['Estacao_Ano'] == 'Primavera') & (dataset['Chuva_mm'] <= media_chuvas_primavera), 'Chuva_mm'] += 30

print('\nAPÒS TRATAR Chuva_mm:')

# qual a média da chuva na primavera
print( 'MIN CHUVAS PRIMAVERA', dataset[ dataset['Estacao_Ano'] == 'Primavera' ]['Chuva_mm'].min() ) 
print( 'MEDIA CHUVAS PRIMAVERA', dataset[ dataset['Estacao_Ano'] == 'Primavera' ]['Chuva_mm'].mean() ) 
print( 'MAX CHUVAS PRIMAVERA', dataset[ dataset['Estacao_Ano'] == 'Primavera' ]['Chuva_mm'].max() ) 

print('')

# qual a média de chuvas no verao
print( 'MIN CHUVAS VERAO', dataset[ dataset['Estacao_Ano'] == 'Verão' ]['Chuva_mm'].min() ) 
print( 'MEDIA CHUVAS VERAO', dataset[ dataset['Estacao_Ano'] == 'Verão' ]['Chuva_mm'].mean() ) 
print( 'MAX CHUVAS VERAO', dataset[ dataset['Estacao_Ano'] == 'Verão' ]['Chuva_mm'].max() ) 

print('')

# qual a média de chuvas no outono
print( 'MIN CHUVAS OUTONO', dataset[ dataset['Estacao_Ano'] == 'Outono' ]['Chuva_mm'].min() ) 
print( 'MEDIA CHUVAS OUTONO', dataset[ dataset['Estacao_Ano'] == 'Outono' ]['Chuva_mm'].mean() ) 
print( 'MAX CHUVAS OUTONO', dataset[ dataset['Estacao_Ano'] == 'Outono' ]['Chuva_mm'].max() ) 

print('')

# qual a média de chuvas no inverno
print( 'MIN CHUVAS INVERNO', dataset[ dataset['Estacao_Ano'] == 'Inverno' ]['Chuva_mm'].min() ) 
print( 'MEDIA CHUVAS INVERNO', dataset[ dataset['Estacao_Ano'] == 'Inverno' ]['Chuva_mm'].mean() ) 
print( 'MAX CHUVAS INVERNO', dataset[ dataset['Estacao_Ano'] == 'Inverno' ]['Chuva_mm'].max() ) 

print('')

"""
Agora ficou muito melhor

Porém, o outono é um periodo que antecede o inverno, então na minha opinião eu preciso ele precisa ser menor um pouquinho menor
"""
dataset.loc[dataset['Estacao_Ano'] == 'Outono', 'Chuva_mm'] -= 6

print('\nAPÒS TRATAR Chuva_mm:')

# qual a média da chuva na primavera
print( 'MIN CHUVAS PRIMAVERA', dataset[ dataset['Estacao_Ano'] == 'Primavera' ]['Chuva_mm'].min() ) 
print( 'MEDIA CHUVAS PRIMAVERA', dataset[ dataset['Estacao_Ano'] == 'Primavera' ]['Chuva_mm'].mean() ) 
print( 'MAX CHUVAS PRIMAVERA', dataset[ dataset['Estacao_Ano'] == 'Primavera' ]['Chuva_mm'].max() ) 

print('')

# qual a média de chuvas no verao
print( 'MIN CHUVAS VERAO', dataset[ dataset['Estacao_Ano'] == 'Verão' ]['Chuva_mm'].min() ) 
print( 'MEDIA CHUVAS VERAO', dataset[ dataset['Estacao_Ano'] == 'Verão' ]['Chuva_mm'].mean() ) 
print( 'MAX CHUVAS VERAO', dataset[ dataset['Estacao_Ano'] == 'Verão' ]['Chuva_mm'].max() ) 

print('')

# qual a média de chuvas no outono
print( 'MIN CHUVAS OUTONO', dataset[ dataset['Estacao_Ano'] == 'Outono' ]['Chuva_mm'].min() ) 
print( 'MEDIA CHUVAS OUTONO', dataset[ dataset['Estacao_Ano'] == 'Outono' ]['Chuva_mm'].mean() ) 
print( 'MAX CHUVAS OUTONO', dataset[ dataset['Estacao_Ano'] == 'Outono' ]['Chuva_mm'].max() ) 

print('')

# qual a média de chuvas no inverno
print( 'MIN CHUVAS INVERNO', dataset[ dataset['Estacao_Ano'] == 'Inverno' ]['Chuva_mm'].min() ) 
print( 'MEDIA CHUVAS INVERNO', dataset[ dataset['Estacao_Ano'] == 'Inverno' ]['Chuva_mm'].mean() ) 
print( 'MAX CHUVAS INVERNO', dataset[ dataset['Estacao_Ano'] == 'Inverno' ]['Chuva_mm'].max() ) 

print('')

"""
Agora faz mais sentido
"""
