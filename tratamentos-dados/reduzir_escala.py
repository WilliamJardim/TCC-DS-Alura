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
DESSAS FALTA TRATAR:

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

"""
Agora falta tratar a Altura_cm, pois ainda tem valores negativos na altura da planta, o que não faz nenhum sentido
"""

print('\nANALISANDO MINIMO, MAXIMO E MEDIA DA COLUNA ALTURA_CM:')
print( dataset['Altura_cm'].describe() );

"""

ANALISANDO MINIMO, MAXIMO E MEDIA DA COLUNA ALTURA_CM:
count      3000.000000
mean     230260.402328
std      265665.460498
min     -509007.871632
25%       28959.940530
50%      252557.922538
75%      430439.496518
max      822584.493505
Name: Altura_cm, dtype: float64

Dá pra notar que os valores são aburdos, alguns mediriam KM de tamanho se fossem convertidos para kilometros!
"""

# Reduzi essa escala para não ultrapassar METROS
dataset['Altura_cm'] = dataset['Altura_cm'] / 100;

print('\nANALISANDO DENOVO: MINIMO, MAXIMO E MEDIA DA COLUNA ALTURA_CM, APÒS REDUZIR ESCALA:')
print( dataset['Altura_cm'].describe() );

"""
Agora faz muito mais sentido:

ANALISANDO DENOVO: MINIMO, MAXIMO E MEDIA DA COLUNA ALTURA_CM, APÒS REDUZIR ESCALA:
count    3000.000000
mean     2302.604023
std      2656.654605
min     -5090.078716
25%       289.599405
50%      2525.579225
75%      4304.394965
max      8225.844935
Name: Altura_cm, dtype: float64

Agora falta eu calcular a média, valor minimo e máximo de cada estação do ano, pra entender melhor se preciso ajustar algo

"""
print('\nAPÒS TRATAR ESCALA Altura_cm:')

# qual a média da Altura_cm na primavera
print( 'MIN Altura_cm PRIMAVERA', dataset[ dataset['Estacao_Ano'] == 'Primavera' ]['Altura_cm'].min() ) 
print( 'MEDIA Altura_cm PRIMAVERA', dataset[ dataset['Estacao_Ano'] == 'Primavera' ]['Altura_cm'].mean() ) 
print( 'MAX Altura_cm PRIMAVERA', dataset[ dataset['Estacao_Ano'] == 'Primavera' ]['Altura_cm'].max() ) 

print('')

# qual a média de Altura_cm no verao
print( 'MIN Altura_cm VERAO', dataset[ dataset['Estacao_Ano'] == 'Verão' ]['Altura_cm'].min() ) 
print( 'MEDIA Altura_cm VERAO', dataset[ dataset['Estacao_Ano'] == 'Verão' ]['Altura_cm'].mean() ) 
print( 'MAX Altura_cm VERAO', dataset[ dataset['Estacao_Ano'] == 'Verão' ]['Altura_cm'].max() ) 

print('')

# qual a média de Altura_cm no outono
print( 'MIN Altura_cm OUTONO', dataset[ dataset['Estacao_Ano'] == 'Outono' ]['Altura_cm'].min() ) 
print( 'MEDIA Altura_cm OUTONO', dataset[ dataset['Estacao_Ano'] == 'Outono' ]['Altura_cm'].mean() ) 
print( 'MAX Altura_cm OUTONO', dataset[ dataset['Estacao_Ano'] == 'Outono' ]['Altura_cm'].max() ) 

print('')

# qual a Altura_cm de chuvas no inverno
print( 'MIN Altura_cm INVERNO', dataset[ dataset['Estacao_Ano'] == 'Inverno' ]['Altura_cm'].min() ) 
print( 'MEDIA Altura_cm INVERNO', dataset[ dataset['Estacao_Ano'] == 'Inverno' ]['Altura_cm'].mean() ) 
print( 'MAX Altura_cm INVERNO', dataset[ dataset['Estacao_Ano'] == 'Inverno' ]['Altura_cm'].max() ) 

print('')

"""
O resultado foi esse:


APÒS TRATAR ESCALA Altura_cm:
MIN Altura_cm PRIMAVERA -4298.470527155631
MEDIA Altura_cm PRIMAVERA 2417.146688033889
MAX Altura_cm PRIMAVERA 6377.503598282309

MIN Altura_cm VERAO -5090.078716321775
MEDIA Altura_cm VERAO 3939.071890038556
MAX Altura_cm VERAO 8225.844935045006

MIN Altura_cm OUTONO -2138.238076239102
MEDIA Altura_cm OUTONO 3707.298202983684
MAX Altura_cm OUTONO 7346.103161482534

MIN Altura_cm INVERNO -3765.205911099949
MEDIA Altura_cm INVERNO -655.7372580196429
MAX Altura_cm INVERNO 2651.3676537895644

Eu acredito que a média, minimo e maixmo POR ESTAÇÂO da Altura_cm não é uma informação muito relevante para eu tratar isso, 
Pois, Altura_cm não depende exclusivamente da estação do ano

Por exemplo, Chuva, Temperatura, Horas Sol, Frequencia podas(nem tanto mais eu coloquei um pouco), podem até terem uma relação mais forte com a estação do ano,
mais Altura_cm já não depende tanto da estação do ano em si, mais pode estar correlacionado devido a outros fatores correlatos
"""

"""
Eu quero descobrir quantos valores negativos existem
"""

print( 'QTDE ALTURA NEGATIVAS', dataset[ dataset['Altura_cm'] < 0 ]['Altura_cm'].count() );

"""
Tem 668 amostras com valores negativos na coluna Altura_cm

Eu preciso saber em quais estações do ano estão esses valores negativos.
Preciso descobrir se estão mais em determinadas estações, ou em todas
"""

print( 'ESTAÇÔES QUE TEM ALTURA NEGATIVAS', dataset[ dataset['Altura_cm'] < 0 ]['Estacao_Ano'].unique() );

"""
Todas elas tem!
Isso é um problema maior

isso significa que, temos 668 amostras com valores negativos na coluna Altura_cm, 
E tambem que essas amostras não estão concetradas em estações especificas, mais espalhadas, o que torna um pouco mais complexo de tratar sem afetar o dataset
"""

"""
Tive uma idea para tratar isso sem muito esforço

Eu somo um valor bem grande para elimiar os negativos, tornando eles positivos, porem isso poderia aumentar a escala de forma indesejada
Se aumentasse a escala depois eu reduzo a escala divivindo por um valor pra corrigir a escala novamente
"""

# Tratei isso: primeiro eu somo um valor suficiente para elimiar os negativos
dataset['Altura_cm'] = dataset['Altura_cm'] + 5099.078716 + 35

# Vou conferir se o número que eu somei em todos já eliminou os negativos
print( 'QTDE ALTURA NEGATIVAS', dataset[ dataset['Altura_cm'] < 0 ]['Altura_cm'].count() );

"""
Fiz varios testes com diferentes valores para dividir

Agora eu preciso conferir a média, o valor minimo e maximo denovo
"""

print('\nANALISANDO DENOVO: MINIMO, MAXIMO E MEDIA DA COLUNA ALTURA_CM, APÒS TRARAR OS NEGATIVOS:')
print( dataset['Altura_cm'].describe() );

"""
E Ótimo: Os valores negativos foram transformados em positivos, sem afetar o padrão:

ANALISANDO DENOVO: MINIMO, MAXIMO E MEDIA DA COLUNA ALTURA_CM, APÒS TRARAR OS NEGATIVOS:
count     3000.000000
mean     12302.604023
std       2656.654605
min       4909.921284
25%      10289.599405
50%      12525.579225
75%      14304.394965
max      18225.844935
Name: Altura_cm, dtype: float64

Aparentemente, os valores minimos e máximos e média, estão adequados, pois eu sei que o padrão não mudou, só a escala mesmo
O que era grande continuou sendo grande, o que era pequeno continuou sendo pequeno, em relação a escala atual.

A escala mudou, porém o mesmo padrão se manteve, e era exatamente isso que eu queria.

Porém, eu preciso tratar a escala para que ela volte ao normal, sem afetar o padrão, e sem voltar a ter valores negativos.
"""

"""
VOLTANDO A ESCALA AO NORMAL, OU PARA UMA ESCALA QUE FAÇA MAIS SENTIDO

Pra isso, eu posso fazer uma divisão por 10
"""

dataset['Altura_cm'] = dataset['Altura_cm'] / 10

# após tratar isso vou conferir denovo:

# Vou conferir ainda continua sem os negativos
print( 'QTDE ALTURA NEGATIVAS', dataset[ dataset['Altura_cm'] < 0 ]['Altura_cm'].count() );

# Vou analisar denovo a média, valor minimo e maximo
print('\nANALISANDO DENOVO: MINIMO, MAXIMO E MEDIA DA COLUNA ALTURA_CM, APÒS TRARAR OS NEGATIVOS:')
print( dataset['Altura_cm'].describe() );

"""
Na minha opinião está bem tratado a Altura_cm!
"""

"""
AGORA EU AINDA PRECISO TRATAR O NUM_PRAGAS

IDEIA FAZER TAMBEM: Tratar o numero de pragas, pra ao invez de ser zero no inverno, ser a metade do valor minimo positivo, pra ficar na mesma proporção
"""

# Vou analisar as pragas
print('\nANALISANDO MINIMO, MAXIMO E MEDIA DA COLUNA Num_Praga, APÒS TRARAR OS NEGATIVOS:')
print( dataset['Num_Praga'].describe() );

"""
ANALISANDO MINIMO, MAXIMO E MEDIA DA COLUNA Num_Praga, APÒS TRARAR OS NEGATIVOS:
count    3000.000000
mean        4.945500
std        12.359721
min         0.000000
25%         0.000000
50%         0.000000
75%         0.000000
max        73.500000
Name: Num_Praga, dtype: float64

No caso, eu ja tratei na hora de gerar o dataset, criando uma restrição pra ele não ter Num_Praga negativas

MAIS EXISTE UM POSSIVEL PROBLEMA: os quartis 25%, 50% e 75% do Num_Praga é 0, o que indica que a grande maioria das amostras tem praga igual a zero(que antes era negativo pois eu tratei pra ser zero se fosse negativo)
isso com certeza vai impactar na hora que eu for criar meu modelo 

porém, eu ainda posso melhor o padrão com aquela ideia que eu tive: 

IDEIA FAZER TAMBEM: Tratar o numero de pragas, pra ao invez de ser zero no inverno, ser a metade do valor minimo positivo, pra ficar na mesma proporção
"""

"""
Pra tentar corrigir o problema, eu posso fazer o seguinte:
"""

# Identificar quantas amostras tem Num_Praga igual a 0
print( 'QTDE AMOSTRAS COM Num_Praga igual a zero: ', dataset[dataset['Num_Praga'] == 0]['Num_Praga'].count() );

"""
O meu dataset de tem 3000 amostras:

Porém nesse meu dataset, dessas 3000 amostras, as 2386 amostras estão com Num_Praga igual a zero, o que é péssimo,
de fato, o a grande maioria das amostras tem Num_Praga igual a zero

Eu poderia recalcular esses valores, substituindo a coluna, levando em conta alguns fatores, simplificando um pouco meu dataset, mais eu não quero fazer isso.

MAIS ALGUMAS PERGUNTAS SÂO IMPORTANTES EU SABER:

  (1) Quantas amostras tem Num_Praga diferente de zero
  
  (2) Qual a quantidade de Num_Praga por estação do ano

  Com isso vou conseguir saber se tem alguma desproporção ou desbalanceamento, o que tudo indica ser o caso

"""
# Identificar quantas amostras tem Num_Praga diferente de 0
print( 'QTDE AMOSTRAS COM Num_Praga diferente de zero: ', dataset[dataset['Num_Praga'] != 0]['Num_Praga'].count() );

"""
Das 3000 amostras, apenas 614 tem Num_Praga diferente de zero,
o resto é tudo zero!

Eu preciso tratar isso

MAIS ALGUMAS PERGUNTAS SÂO IMPORTANTES EU SABER:

  (2) Qual a quantidade de Num_Praga por estação do ano

"""

print('\n\n')

print( 'QTDE Num_Praga Primavera: ', dataset[dataset['Estacao_Ano'] == 'Primavera']['Num_Praga'].describe() );

print('\n\n')

print( 'QTDE Num_Praga Verão: ', dataset[dataset['Estacao_Ano'] == 'Verão']['Num_Praga'].describe() );

print('\n\n')

print( 'QTDE Num_Praga Outono: ', dataset[dataset['Estacao_Ano'] == 'Outono']['Num_Praga'].describe() );

print('\n\n')

print( 'QTDE Num_Praga Inverno: ', dataset[dataset['Estacao_Ano'] == 'Inverno']['Num_Praga'].describe() );

"""
Antes eu não tinha percebido isso por que o gráfico que eu tinha feito na analise exploratória mostrava a média do Num_Pragas por estação, mais não os valores mesmo
E embora a média e valor minimo e maximo façam sentido, as pragas são meio que "raras" pois, em cada estação, bem poucas amostras tem Num_Pragas maior que zero
"""

"""
Pra confirmar e entender mais isso eu tambem posso calcular a proporção "Num_Pragas maior que zero" e "Num_Pragas igual a zero", de cada estação
"""

"""
A unica solução mais viavel que vejo no momento é remover algumas dessas amostras, mantendo uma certa proporção por estação

Depois na hora de treinar o modelo eu posso até gerar novas amostras de treino em cima dessas 614 que não tem o valor zerado

Eu sei que as Ervas_Daninhas vai ter esse mesmo problema, pois eu gerei e tratei da mesma forma!
Então, eu posso optar por remover a coluna Ervas_Daninhas do dataset e não usar ela
"""

"""
Vou começar a aplicar isso então:
"""

# Vou apagar a coluna Ervas_Daninhas que só vai dificultar
dataset = dataset.drop('Ervas_Daninhas', axis=1);

"""
Agora vou fazer com que o inverno tenha pelo menos 1 a 2 pragas, em vez de ser apenas tudo zero, pra não ser um Outlier em potencial e não atrapalhar em outros processos
"""
pragas_inverno = dataset['Estacao_Ano'] == 'Inverno';
dataset.loc[pragas_inverno, 'Num_Praga'] += np.random.uniform(1,3, pragas_inverno.sum() )

"""
Agora isso já vai impedir alguns problemas que eu pensei: Como por exemplo, não trazer nenhuma amostra para o inverno
"""

# Vou pegar só as amostras que tem Num_Pragas maior que zero
dataset_com_pragas_maiores_que_zero = dataset[dataset['Num_Praga'] > 0];

# Vendo se eu peguei o que eu queria
print(dataset_com_pragas_maiores_que_zero.head())

"""
Agora eu preciso ver por estação, quais são os valores minimo, maximo e média, 
E tambem conferir quantas amostras ficaram em cada, pra ver se existe um balanceamento justo de amostras
"""

print('\n\n')

print( 'QTDE Num_Praga Primavera: ', dataset_com_pragas_maiores_que_zero[dataset_com_pragas_maiores_que_zero['Estacao_Ano'] == 'Primavera']['Num_Praga'].describe() );

print('\n\n')

print( 'QTDE Num_Praga Verão: ', dataset_com_pragas_maiores_que_zero[dataset_com_pragas_maiores_que_zero['Estacao_Ano'] == 'Verão']['Num_Praga'].describe() );

print('\n\n')

print( 'QTDE Num_Praga Outono: ', dataset_com_pragas_maiores_que_zero[dataset_com_pragas_maiores_que_zero['Estacao_Ano'] == 'Outono']['Num_Praga'].describe() );

print('\n\n')

print( 'QTDE Num_Praga Inverno: ', dataset_com_pragas_maiores_que_zero[dataset_com_pragas_maiores_que_zero['Estacao_Ano'] == 'Inverno']['Num_Praga'].describe() );

"""
Os resultados são:

QTDE Num_Praga Primavera:  count    226.000000
mean      21.030973
std       13.794892
min        0.500000
25%        9.500000
50%       18.000000
75%       33.000000
max       49.000000
Name: Num_Praga, dtype: float64



QTDE Num_Praga Verão:  count    211.000000
mean      32.146919
std       19.760283
min        1.500000
25%       15.000000
50%       31.500000
75%       45.000000
max       73.500000
Name: Num_Praga, dtype: float64



QTDE Num_Praga Outono:  count    177.000000
mean      18.646893
std       12.417153
min        0.500000
25%        8.500000
50%       16.500000
75%       28.500000
max       44.500000
Name: Num_Praga, dtype: float64



QTDE Num_Praga Inverno:  count    782.000000
mean       2.002368
std        0.592919
min        1.000470
25%        1.483718
50%        1.976778
75%        2.542618
max        2.999172
Name: Num_Praga, dtype: float64


Note que o Inverno tem 782 amostras

E as demais tem bem menos amostras. Então existe um desbalanceamento muito grande

Eu tenho duas saidas:

  (1) - Remover várias amostras do inverno e tratar algumas coisas

  (2) - Ou compensar colocando mais amostras usando técnicas para gerar novas amostrar a partir das existentes

Pra eu tentar seguir o primeiro caminho, eu preciso entender como estão organizadas as amostras do inverno

"""

# Quero ver todas as 782 uma por uma
#pd.set_option('display.max_rows', None)  # Remove o limite de linhas a ser exibido
print( dataset_com_pragas_maiores_que_zero[dataset_com_pragas_maiores_que_zero['Estacao_Ano'] == 'Inverno'] )

"""
Eu posso fazer um slicing para reduzir a quantidade de amostras
Fazer um slicing significa recortar um trecho do dataset.
Por exemplo se das 782 amostras eu quero pegar somente 300, eu posso fazer um slicing de 0 a 300

Pelos dados dessas amostras, isso não vai prejudicar a qualidade 
"""

# eu preciso filtrar somente as amostras do inverno, para poder aplicar o slicing
dataset_somente_amostras_inverno = dataset_com_pragas_maiores_que_zero[dataset_com_pragas_maiores_que_zero['Estacao_Ano'] == 'Inverno'];

quantas_em_quantas = 3 # Eu escolhi fazer um slicing só que selecionando as amostras de 3 em 3

# Aqui eu faço o slicing
dataset_somente_amostras_inverno_recortado = dataset_somente_amostras_inverno.iloc[0:782:quantas_em_quantas];

# aqui eu limito que só quero no máximo 300 amostras do inverno
dataset_somente_amostras_inverno_recortado_somente_300 = dataset_somente_amostras_inverno_recortado.head(300);

"""
Eu já tenho a minha seleção feita
PORÈM AGORA EU PRECISO COLOCAR ISSO NO DATASET

eu posso fazer isso pegando todas as amostras QUE NÂO SEJAM DO INVERNO, e depois concatenar(ou seja, juntar) com AS AMOSTRAS DO INVERNO
"""

# agora eu preciso pegar as amostras QUE NÂO SEJAM DO INVERNO
dataset_amostras_exceto_inverno = dataset_com_pragas_maiores_que_zero[dataset_com_pragas_maiores_que_zero['Estacao_Ano'] != 'Inverno'];

# agora que eu tenho as duas coisas, eu posso juntar devolta
dataset_balanceado = pd.concat([dataset_amostras_exceto_inverno, dataset_somente_amostras_inverno_recortado_somente_300], ignore_index=True)

"""
Agora eu posso verificar denovo
"""
print('\nVERIFICANDO DENOVO AS PRAGAS POR ESTAÇÂO APÒS O BALANCEAMENTO:\n\n')

print( 'QTDE Num_Praga Primavera: ', dataset_balanceado[dataset_balanceado['Estacao_Ano'] == 'Primavera']['Num_Praga'].describe() );

print('\n\n')

print( 'QTDE Num_Praga Verão: ', dataset_balanceado[dataset_balanceado['Estacao_Ano'] == 'Verão']['Num_Praga'].describe() );

print('\n\n')

print( 'QTDE Num_Praga Outono: ', dataset_balanceado[dataset_balanceado['Estacao_Ano'] == 'Outono']['Num_Praga'].describe() );

print('\n\n')

print( 'QTDE Num_Praga Inverno: ', dataset_balanceado[dataset_balanceado['Estacao_Ano'] == 'Inverno']['Num_Praga'].describe() );

"""
Agora ficou assim a proporção:


VERIFICANDO DENOVO AS PRAGAS POR ESTAÇÂO APÒS O BALANCEAMENTO:


QTDE Num_Praga Primavera:  count    226.000000
mean      21.030973
std       13.794892
min        0.500000
25%        9.500000
50%       18.000000
75%       33.000000
max       49.000000
Name: Num_Praga, dtype: float64



QTDE Num_Praga Verão:  count    211.000000
mean      32.146919
std       19.760283
min        1.500000
25%       15.000000
50%       31.500000
75%       45.000000
max       73.500000
Name: Num_Praga, dtype: float64



QTDE Num_Praga Outono:  count    177.000000
mean      18.646893
std       12.417153
min        0.500000
25%        8.500000
50%       16.500000
75%       28.500000
max       44.500000
Name: Num_Praga, dtype: float64



QTDE Num_Praga Inverno:  count    261.000000
mean       1.992619
std        0.612959
min        1.034715
25%        1.391882
50%        1.989335
75%        2.584597
max        2.989941
Name: Num_Praga, dtype: float64

Ainda não está 100% balanceado
PORÈM, JÁ ESTA MUITO MELHOR

"""

"""
EU AINDA POSSO SEGUIR MINHA IDEIA: Compensar colocando mais amostras usando técnicas para gerar novas amostrar a partir das existentes
"""

"""

Eu quero tratar alguns valores NaN que eu reparei durante a analise

Pra isso eu preciso:
  (1) - Descobrir quais colunas tem valores NaN

  (2) - Escolher um método para tratar: usar média da coluna, regressão, ou preencher com zero ou um 1, ou outra técnica

"""

"""
Vou tratar as colunas que estão com NaN usando a média delas

Pra isso, primeiro preciso descobrir quais colunas tem valores NaN
"""

# Descobrir quais colunas tem valores NaN
colunasQueTemNaN = dataset_balanceado.columns[dataset_balanceado.isna().any()].tolist()

print('Quais colunas tem valores NaN', colunasQueTemNaN)

"""
Quais colunas tem valores NaN: ['Humidade_Solo', 'Custo_Cultivo']
Apenas essas que eu preciso tratar

Seria interessante eu saber quantos valores NaN existem em cada coluna
"""

# Contar os valores NaN nessas colunas: ['Humidade_Solo', 'Custo_Cultivo']
contagem_nan = dataset_balanceado[colunasQueTemNaN].isna().sum()

print('Quantidade NaN por coluna: \n');
print(contagem_nan)

"""
Quantidade NaN por coluna:

Humidade_Solo    8
Custo_Cultivo    2
dtype: int64

Agora eu sei quantos valores NaN existem em cada coluna
E posso calcular a média dessa scolunas
"""

mediaHumidadeSolo = dataset_balanceado['Humidade_Solo'].mean()
print('MEDIA HUMIDADE SOLO: ', mediaHumidadeSolo);

mediaCusto_Cultivo = dataset_balanceado['Custo_Cultivo'].mean()
print('MEDIA Custo_Cultivo: ', mediaCusto_Cultivo);

"""
Eu disse que eu quero usar a média de cada uma dessas colunas pra tratar os valores NaN
Então eu preciso calcular essa media geral da coluna

Porém isso pode ter limitações, e pode distorcer os dados
"""

"""
Uma abordagem melhor que eu pensei seria eu tratar com a média da coluna para cada estação do ano

Pra isso, coisa que vale a pena eu olher é se os valores NaN estão em todas as estações
se estiverem, eu posso aplicar um tratamente diferente para cada estação, o que pode melhorar
"""

# Vendo os valores NaN da coluna Humidade_Solo em cada estação do ano
print('\n')
print('VALORES NAN DA COLUNA Humidade_Solo NA PRIMAVERA: ')
print( dataset_balanceado.loc[ (dataset_balanceado['Estacao_Ano'] == 'Primavera') & (dataset_balanceado['Humidade_Solo'].isna() ) ] )

print('\n')
print('VALORES NAN DA COLUNA Humidade_Solo NO Verão: ')
print( dataset_balanceado.loc[ (dataset_balanceado['Estacao_Ano'] == 'Verão') & (dataset_balanceado['Humidade_Solo'].isna() ) ] )

print('\n')
print('VALORES NAN DA COLUNA Humidade_Solo NO Outono: ')
print( dataset_balanceado.loc[ (dataset_balanceado['Estacao_Ano'] == 'Outono') & (dataset_balanceado['Humidade_Solo'].isna() ) ] )

print('\n')
print('VALORES NAN DA COLUNA Humidade_Solo NO Inverno: ')
print( dataset_balanceado.loc[ (dataset_balanceado['Estacao_Ano'] == 'Inverno') & (dataset_balanceado['Humidade_Solo'].isna() ) ] )

"""
Esses são eles:

VALORES NAN DA COLUNA Humidade_Solo NA PRIMAVERA:
           Data Estacao_Ano Tipo_Planta Tipo_Solo  Temperatura_C    Chuva_mm  ...  Tempo_Crescimento_horas  Litros_Agua_Semana   Saude  Custo_Cultivo    Preco_Venda  Tempo_Vida_dias
150  2022-03-02   Primavera      Batata  Argiloso      12.542969  128.315936  ...               811.429365          762.305321  Doente  281794.199130   43309.802851      3388.847294
245  2023-04-22   Primavera      Tomate    Humoso      21.327720   91.247849  ...              1169.506839          934.074498  Doente  401965.555291  360162.681780      1895.789925

[2 rows x 23 columns]


VALORES NAN DA COLUNA Humidade_Solo NO Verão:
           Data Estacao_Ano Tipo_Planta Tipo_Solo  Temperatura_C    Chuva_mm  ...  Tempo_Crescimento_horas  Litros_Agua_Semana   Saude  Custo_Cultivo    Preco_Venda  Tempo_Vida_dias
280  2023-08-09       Verão       Trigo   Siltoso      43.494843  107.905074  ...              1550.393435          959.961284  Doente  419230.342351  143782.199162       765.143755
346  2024-06-24       Verão       Trigo    Humoso      34.460520  123.436689  ...              2617.414131         1335.694480  Doente  600095.890807  144757.262752     -2086.337256
570  2027-06-26       Verão       Trigo    Humoso      43.185203   79.691804  ...              1863.621981         1096.269272  Doente  511100.157458   89201.456700      -269.066517

[3 rows x 23 columns]


VALORES NAN DA COLUNA Humidade_Solo NO Outono:
           Data Estacao_Ano Tipo_Planta Tipo_Solo  Temperatura_C    Chuva_mm  ...  Tempo_Crescimento_horas  Litros_Agua_Semana   Saude  Custo_Cultivo   Preco_Venda  Tempo_Vida_dias
213  2022-10-24      Outono     Cenoura    Humoso      24.744834  160.837865  ...              1342.921697          857.265372  Doente  320072.610993  38534.342262      1829.257145
519  2026-09-17      Outono     Cenoura    Humoso      17.248624   73.764909  ...               779.748236          750.380789  Doente  292439.675495  59332.073832      3022.859520

[2 rows x 23 columns]


VALORES NAN DA COLUNA Humidade_Solo NO Inverno:
           Data Estacao_Ano Tipo_Planta Tipo_Solo  Temperatura_C  Chuva_mm  ...  Tempo_Crescimento_horas  Litros_Agua_Semana   Saude  Custo_Cultivo  Preco_Venda  Tempo_Vida_dias
739  2024-01-15     Inverno        Soja   Siltoso       4.493585       4.0  ...              1382.780409          956.525993  Doente  357453.124516  108994.7673      1540.857683

[1 rows x 23 columns]

"""

"""
Eu vi que, são bem poucas amostras que tem valores NaN na coluna Humidade_Solo
E tambem sei que em todas as estações tem
"""

"""
Agora eu posso tambem ver a do custo cultivo
"""
# Vendo os valores NaN da coluna Custo_Cultivo em cada estação do ano
print('\n')
print('VALORES NAN DA COLUNA Custo_Cultivo NA PRIMAVERA: ')
print( dataset_balanceado.loc[ (dataset_balanceado['Estacao_Ano'] == 'Primavera') & (dataset_balanceado['Custo_Cultivo'].isna() ) ] )

print('\n')
print('VALORES NAN DA COLUNA Custo_Cultivo NO Verão: ')
print( dataset_balanceado.loc[ (dataset_balanceado['Estacao_Ano'] == 'Verão') & (dataset_balanceado['Custo_Cultivo'].isna() ) ] )

print('\n')
print('VALORES NAN DA COLUNA Custo_Cultivo NO Outono: ')
print( dataset_balanceado.loc[ (dataset_balanceado['Estacao_Ano'] == 'Outono') & (dataset_balanceado['Custo_Cultivo'].isna() ) ] )

print('\n')
print('VALORES NAN DA COLUNA Custo_Cultivo NO Inverno: ')
print( dataset_balanceado.loc[ (dataset_balanceado['Estacao_Ano'] == 'Inverno') & (dataset_balanceado['Custo_Cultivo'].isna() ) ] )

"""
Eu posso aplicar um tratamento para cada uma, assim esse tratamente não vai refletir um padrão genérico demais, e estará refletindo um padrão especifico pra cada estação
Assim, eu posso calcular a média da coluna de Humidade_Solo para cada estação
"""

"""
Eu disse que eu quero usar a média de cada uma dessas colunas pra tratar os valores NaN
E eu tambem disse que vou usar a média da coluna PARA CADA ESTAÇÂO DO ANO PRA MELHORAR O TRATAMENTO

Mais eu posso melhorar esse tratamento ainda mais
Pois eu reparei que todas as amostras que tem valores NaN são amostras de plantas Doentes
Então, para manter a coerencia, não faria nenhum sentido eu incluir no calculo da média amostras Saudaveis, e preencher esses valores NaN

Já que eu vi que são todas amostras doentes que tem a coluna Humidade_Solo com valor NaN, eu posso substituir esses NaN pela média da coluna Humidade_Solo DAS PLANTES DOENTES, E EM CADA ESTAÇÂO
assim eu estaria levando em conta a tendencia o dataset, e os padrões de cada região do dataset.
"""

#Calculando a média da coluna Humidade_Solo apenas das amostras doentes de cada estação:
print('\n')
print('MEDIA DA COLUNA Humidade_Solo DAS AMOSTRAS DOENTES NA PRIMAVERA: ')
print( dataset_balanceado.loc[ (dataset_balanceado['Estacao_Ano'] == 'Primavera' ) & (dataset_balanceado['Saude'] == 'Doente') ]['Humidade_Solo'].mean() )

print('\n')
print('MEDIA DA COLUNA Humidade_Solo DAS AMOSTRAS DOENTES NO Verão: ')
print( dataset_balanceado.loc[ (dataset_balanceado['Estacao_Ano'] == 'Verão' ) & (dataset_balanceado['Saude'] == 'Doente') ]['Humidade_Solo'].mean() )

print('\n')
print('MEDIA DA COLUNA Humidade_Solo DAS AMOSTRAS DOENTES NO Outono: ')
print( dataset_balanceado.loc[ (dataset_balanceado['Estacao_Ano'] == 'Outono' ) & (dataset_balanceado['Saude'] == 'Doente') ]['Humidade_Solo'].mean() )

print('\n')
print('MEDIA DA COLUNA Humidade_Solo DAS AMOSTRAS DOENTES NO Inverno: ')
print( dataset_balanceado.loc[ (dataset_balanceado['Estacao_Ano'] == 'Inverno' ) & (dataset_balanceado['Saude'] == 'Doente') ]['Humidade_Solo'].mean() )

"""

As médias da coluna Humidade_Solo das amostras doentes de cada estação são:

  MEDIA DA COLUNA Humidade_Solo DAS AMOSTRAS DOENTES NA PRIMAVERA:
  48.32694807289242


  MEDIA DA COLUNA Humidade_Solo DAS AMOSTRAS DOENTES NO Verão:
  47.5049442231675


  MEDIA DA COLUNA Humidade_Solo DAS AMOSTRAS DOENTES NO Outono:
  44.284092329230525


  MEDIA DA COLUNA Humidade_Solo DAS AMOSTRAS DOENTES NO Inverno:
  12.363740297806112

Agora preciso calcular as médias do custo cultivo
"""
print('\n')
print('AGORA VOU CALCULAR AS MÈDIAS DO CUSTO DE CULTIVO DE CADA ESTAÇÂO:')


#Calculando a média do Custo_Cultivo apenas das amostras doentes de cada estação:
print('\n')
print('MEDIA DA COLUNA Custo_Cultivo DAS AMOSTRAS DOENTES NA PRIMAVERA: ')
print( dataset_balanceado.loc[ (dataset_balanceado['Estacao_Ano'] == 'Primavera' ) & (dataset_balanceado['Saude'] == 'Doente') ]['Custo_Cultivo'].mean() )

print('\n')
print('MEDIA DA COLUNA Custo_Cultivo DAS AMOSTRAS DOENTES NO Verão: ')
print( dataset_balanceado.loc[ (dataset_balanceado['Estacao_Ano'] == 'Verão' ) & (dataset_balanceado['Saude'] == 'Doente') ]['Custo_Cultivo'].mean() )

print('\n')
print('MEDIA DA COLUNA Custo_Cultivo DAS AMOSTRAS DOENTES NO Outono: ')
print( dataset_balanceado.loc[ (dataset_balanceado['Estacao_Ano'] == 'Outono' ) & (dataset_balanceado['Saude'] == 'Doente') ]['Custo_Cultivo'].mean() )

print('\n')
print('MEDIA DA COLUNA Custo_Cultivo DAS AMOSTRAS DOENTES NO Inverno: ')
print( dataset_balanceado.loc[ (dataset_balanceado['Estacao_Ano'] == 'Inverno' ) & (dataset_balanceado['Saude'] == 'Doente') ]['Custo_Cultivo'].mean() )
print('\n')

"""
As médias da coluna Custo_Cultivo das amostras doentes de cada estação são:

  MEDIA DA COLUNA Custo_Cultivo DAS AMOSTRAS DOENTES NA PRIMAVERA:
  391153.43613509164


  MEDIA DA COLUNA Custo_Cultivo DAS AMOSTRAS DOENTES NO Verão:
  372687.8472476986


  MEDIA DA COLUNA Custo_Cultivo DAS AMOSTRAS DOENTES NO Outono:
  302001.37153015024


  MEDIA DA COLUNA Custo_Cultivo DAS AMOSTRAS DOENTES NO Inverno:
384403.88122289494
"""

"""
Agora eu tenho as médias da Humidade_Solo e Custo_Cultivo das plantas doentes em cada estação

Agora posso tratar essas colunas de uma forma muito legal
"""

# Preenchendo os NaNs de cada estação do ano

# NAN DA PRIMAVERA
mediaHumidadeSolo_primavera = dataset_balanceado.loc[ (dataset_balanceado['Estacao_Ano'] == 'Primavera' ) & (dataset_balanceado['Saude'] == 'Doente') ]['Humidade_Solo'].mean();
dataset_balanceado.loc[(dataset_balanceado['Estacao_Ano'] == 'Primavera') & (dataset_balanceado['Saude'] == 'Doente') & (dataset_balanceado['Humidade_Solo'].isna()), 'Humidade_Solo'] = mediaHumidadeSolo_primavera;

# NAN DO VERÂO
mediaHumidadeSolo_verao = dataset_balanceado.loc[ (dataset_balanceado['Estacao_Ano'] == 'Verão' ) & (dataset_balanceado['Saude'] == 'Doente') ]['Humidade_Solo'].mean();
dataset_balanceado.loc[(dataset_balanceado['Estacao_Ano'] == 'Verão') & (dataset_balanceado['Saude'] == 'Doente') & (dataset_balanceado['Humidade_Solo'].isna()), 'Humidade_Solo'] = mediaHumidadeSolo_verao;

# NAN DO OUTONO
mediaHumidadeSolo_outono = dataset_balanceado.loc[ (dataset_balanceado['Estacao_Ano'] == 'Outono' ) & (dataset_balanceado['Saude'] == 'Doente') ]['Humidade_Solo'].mean();
dataset_balanceado.loc[(dataset_balanceado['Estacao_Ano'] == 'Outono') & (dataset_balanceado['Saude'] == 'Doente') & (dataset_balanceado['Humidade_Solo'].isna()), 'Humidade_Solo'] = mediaHumidadeSolo_outono;

# NAN DO INVERNO
mediaHumidadeSolo_inverno = dataset_balanceado.loc[ (dataset_balanceado['Estacao_Ano'] == 'Inverno' ) & (dataset_balanceado['Saude'] == 'Doente') ]['Humidade_Solo'].mean();
dataset_balanceado.loc[(dataset_balanceado['Estacao_Ano'] == 'Inverno') & (dataset_balanceado['Saude'] == 'Doente') & (dataset_balanceado['Humidade_Solo'].isna()), 'Humidade_Solo'] = mediaHumidadeSolo_inverno;

"""
Posso ver se realmente ele substituiu os NaN na coluna Humidade_Solo
"""
print('\n')
print('VALORES NAN NA COLUNA Humidade_Solo EM CADA ESTAÇÂO DO ANO, APÒS TRATAR OS NAN:')
# Vendo os valores NaN da coluna Humidade_Solo em cada estação do ano
print('\n')
print('VALORES NAN DA COLUNA Humidade_Solo NA PRIMAVERA: ')
print( dataset_balanceado.loc[ (dataset_balanceado['Estacao_Ano'] == 'Primavera') & (dataset_balanceado['Humidade_Solo'].isna() ) ] )

print('\n')
print('VALORES NAN DA COLUNA Humidade_Solo NO Verão: ')
print( dataset_balanceado.loc[ (dataset_balanceado['Estacao_Ano'] == 'Verão') & (dataset_balanceado['Humidade_Solo'].isna() ) ] )

print('\n')
print('VALORES NAN DA COLUNA Humidade_Solo NO Outono: ')
print( dataset_balanceado.loc[ (dataset_balanceado['Estacao_Ano'] == 'Outono') & (dataset_balanceado['Humidade_Solo'].isna() ) ] )

print('\n')
print('VALORES NAN DA COLUNA Humidade_Solo NO Inverno: ')
print( dataset_balanceado.loc[ (dataset_balanceado['Estacao_Ano'] == 'Inverno') & (dataset_balanceado['Humidade_Solo'].isna() ) ] )

"""
Deu certo
"""

"""
Agora preciso fazer a mesma coisa para a coluna Custo_Cultivo
"""
# Preenchendo os NaNs de cada estação do ano

# NAN DA PRIMAVERA
mediaCustoCultivo_primavera = dataset_balanceado.loc[ (dataset_balanceado['Estacao_Ano'] == 'Primavera' ) & (dataset_balanceado['Saude'] == 'Doente') ]['Custo_Cultivo'].mean();
dataset_balanceado.loc[(dataset_balanceado['Estacao_Ano'] == 'Primavera') & (dataset_balanceado['Saude'] == 'Doente') & (dataset_balanceado['Custo_Cultivo'].isna()), 'Custo_Cultivo'] = mediaCustoCultivo_primavera;

# NAN DO VERÂO
mediaCustoCultivo_verao = dataset_balanceado.loc[ (dataset_balanceado['Estacao_Ano'] == 'Verão' ) & (dataset_balanceado['Saude'] == 'Doente') ]['Custo_Cultivo'].mean();
dataset_balanceado.loc[(dataset_balanceado['Estacao_Ano'] == 'Verão') & (dataset_balanceado['Saude'] == 'Doente') & (dataset_balanceado['Custo_Cultivo'].isna()), 'Custo_Cultivo'] = mediaCustoCultivo_verao;

# NAN DO OUTONO
mediaCustoCultivo_outono = dataset_balanceado.loc[ (dataset_balanceado['Estacao_Ano'] == 'Outono' ) & (dataset_balanceado['Saude'] == 'Doente') ]['Custo_Cultivo'].mean();
dataset_balanceado.loc[(dataset_balanceado['Estacao_Ano'] == 'Outono') & (dataset_balanceado['Saude'] == 'Doente') & (dataset_balanceado['Custo_Cultivo'].isna()), 'Custo_Cultivo'] = mediaCustoCultivo_outono;

# NAN DO INVERNO
mediaCustoCultivo_inverno = dataset_balanceado.loc[ (dataset_balanceado['Estacao_Ano'] == 'Inverno' ) & (dataset_balanceado['Saude'] == 'Doente') ]['Custo_Cultivo'].mean();
dataset_balanceado.loc[(dataset_balanceado['Estacao_Ano'] == 'Inverno') & (dataset_balanceado['Saude'] == 'Doente') & (dataset_balanceado['Custo_Cultivo'].isna()), 'Custo_Cultivo'] = mediaCustoCultivo_inverno;

"""
Posso ver se realmente ele substituiu os NaN na coluna Custo_Cultivo
"""
print('\n')
print('VALORES NAN NA COLUNA Custo_Cultivo EM CADA ESTAÇÂO DO ANO, APÒS TRATAR OS NAN:')
# Vendo os valores NaN da coluna Humidade_Solo em cada estação do ano
print('\n')
print('VALORES NAN DA COLUNA Custo_Cultivo NA PRIMAVERA: ')
print( dataset_balanceado.loc[ (dataset_balanceado['Estacao_Ano'] == 'Primavera') & (dataset_balanceado['Custo_Cultivo'].isna() ) ] )

print('\n')
print('VALORES NAN DA COLUNA Custo_Cultivo NO Verão: ')
print( dataset_balanceado.loc[ (dataset_balanceado['Estacao_Ano'] == 'Verão') & (dataset_balanceado['Custo_Cultivo'].isna() ) ] )

print('\n')
print('VALORES NAN DA COLUNA Custo_Cultivo NO Outono: ')
print( dataset_balanceado.loc[ (dataset_balanceado['Estacao_Ano'] == 'Outono') & (dataset_balanceado['Custo_Cultivo'].isna() ) ] )

print('\n')
print('VALORES NAN DA COLUNA Custo_Cultivo NO Inverno: ')
print( dataset_balanceado.loc[ (dataset_balanceado['Estacao_Ano'] == 'Inverno') & (dataset_balanceado['Custo_Cultivo'].isna() ) ] )

"""
Deu certo tambem
"""

"""
Pronto!, agora meu dataset não tem mais valores NaN
"""

"""
Agora eu posso descrever o dataset denovo
"""
print('\nDATASET AGORA DEPOIS DE TODOS ESSES TRATAMENTOS FEITOS:')
print( dataset_balanceado.describe() );


"""
Ainda falta eu tratar uma outra coluna: Tempo_Vida_dias

Como eu vejo em no método describe:

  DATASET AGORA DEPOIS DE TODOS ESSES TRATAMENTOS FEITOS:

        Temperatura_C    Chuva_mm  Horas_Sol_Dia  Humidade_Solo  ...  Litros_Agua_Semana  Custo_Cultivo    Preco_Venda  Tempo_Vida_dias
  count     875.000000  875.000000     875.000000     875.000000  ...          875.000000     875.000000     875.000000       875.000000
  mean       20.037217  100.380397      17.197617      36.660594  ...          883.180572  358621.090376   83843.228167      1559.276327
  std        12.909478   79.870014       6.816875      25.571283  ...          171.685316   99329.390785   59318.221709      1418.514971
  min         3.808148    2.086400       8.004251     -20.161422  ...          377.627814   90531.419479      96.088607     -3498.109989
  25%         5.434947    5.000000       8.415673      18.748046  ...          761.585837  292444.464499   47634.402696       658.908617
  50%        20.983145  101.502666      16.752415      37.830503  ...          880.894554  358387.859829   74233.257085      1573.795971
  75%        29.522825  161.610187      22.613890      56.272721  ...         1001.878139  429019.135168  106916.471842      2524.605947
  max        49.665216  274.120840      29.750185      81.486994  ...         1452.671623  685428.162668  726684.139340      5069.175504

Note que na coluna 'Tempo_Vida_dias', existem valores negativos, o que não faz nenhum sentido.
Então, eu vou precisar tratar eles tambem, a escala deles tambem

Note que a coluna 'Humidade_Solo' existem valores negativos tambem, , o que não faz nenhum sentido.
Então, eu vou precisar tratar eles tambem, e a escala deles tambem
"""

"""
Primeiro vou tratar a Tempo_Vida_Dias
vou eliminar os numeros negativos, depois voltar a escala ao normal
"""
# Tratei isso: primeiro eu somo um valor bem grande para elimiar os negativos
dataset_balanceado['Tempo_Vida_dias'] = dataset_balanceado['Tempo_Vida_dias'] + 10000

# conferindo se isso resolveu
print( 'Tempo_Vida_dias após remover negativos: ', dataset_balanceado['Tempo_Vida_dias'].describe() );

"""
Ficou assim:
Tempo_Vida_dias após remover negativos:  count      875.000000
mean     11559.276327
std       1418.514971
min       6501.890011
25%      10658.908617
50%      11573.795971
75%      12524.605947
max      15069.175504
Name: Tempo_Vida_dias, dtype: float64

Funcionou!
Agora o Tempo_Vida_dias não tem mais valores negativos
Porém, a escala dele ficou absurda devido a grande soma

VOU TRATAR A ESCALA DELE
"""
dataset_balanceado['Tempo_Vida_dias'] = dataset_balanceado['Tempo_Vida_dias'] / 100

# conferindo se isso resolveu a escala
print( 'Tempo_Vida_dias após tratar escala: ', dataset_balanceado['Tempo_Vida_dias'].describe() );

"""
Após tratar a escala do Tempo_Vida_Dias, ficou assim:

Tempo_Vida_dias após tratar escala:  count    875.000000
mean     115.592763
std       14.185150
min       65.018900
25%      106.589086
50%      115.737960
75%      125.246059
max      150.691755
Name: Tempo_Vida_dias, dtype: float64
"""

"""
Pronto!, agora o Tempo_Vida_dias não tem mais valores negativos, e está em uma escala que faz muito mais sentido
"""

"""
Agora quero tratar o 'Humidade_Solo' que tem valores negativos
Pra isso eu posso descrever o dataset denovo pra ver as colunas
"""
print('\nDATASET AGORA DEPOIS DE TODOS ESSES TRATAMENTOS FEITOS:')
print( dataset_balanceado.describe() );

# Vendo especificamente a coluna Humidade_Solo 
print( 'Humidade_Solo atual das amostras: ',dataset_balanceado['Humidade_Solo'].describe() );

"""
HUMIDADE DO SOLO ATUAL DAS AMOSTRAS

Humidade_Solo atual das amostras:  count    875.000000
mean      36.660594
std       25.571283
min      -20.161422
25%       18.748046
50%       37.830503
75%       56.272721
max       81.486994
Name: Humidade_Solo, dtype: float64

Note que, existem valores negativos

Eu vou tratar exatamente da mesma forma que eu fiz com todos os outros
Porém não vou tratar a escala, por que eu testei e não ficou muito bom
então pra presentar a escala, eu tive ideia de usar outra estrategia simples
"""

"""
Vou eliminar os numeros negativos
"""
# Tratei isso: primeiro eu somo um valor qualquer que seja capaz de elimiar os negativos
dataset_balanceado['Humidade_Solo'] = dataset_balanceado['Humidade_Solo'] + 25

# conferindo se isso resolveu
print( 'Humidade_Solo após remover negativos: ', dataset_balanceado['Humidade_Solo'].describe() );

"""
Humidade_Solo após remover negativos: 

count     875.000000
mean     1036.660594
std        25.571283
min       979.838578
25%      1018.748046
50%      1037.830503
75%      1056.272721
max      1081.486994
Name: Humidade_Solo, dtype: float64

Ele removeu os negativos porém, a escala ficou absurda, por causa da grande soma
Agora vou tratar a escala divindo por um valor
"""

"""
Agora eu posso conferir se esses valores fazem sentido pra acda estação do ano
"""
print('\nAPÒS TRATAR ESCALA Humidade_Solo:')

# qual a média da Humidade_Solo na primavera
print( 'MIN Humidade_Solo PRIMAVERA', dataset_balanceado[ dataset_balanceado['Estacao_Ano'] == 'Primavera' ]['Humidade_Solo'].min() ) 
print( 'MEDIA Humidade_Solo PRIMAVERA', dataset_balanceado[ dataset_balanceado['Estacao_Ano'] == 'Primavera' ]['Humidade_Solo'].mean() ) 
print( 'MAX Humidade_Solo PRIMAVERA', dataset_balanceado[ dataset_balanceado['Estacao_Ano'] == 'Primavera' ]['Humidade_Solo'].max() ) 

print('')

# qual a média de Humidade_Solo no verao
print( 'MIN Humidade_Solo VERAO', dataset_balanceado[ dataset_balanceado['Estacao_Ano'] == 'Verão' ]['Humidade_Solo'].min() ) 
print( 'MEDIA Humidade_Solo VERAO', dataset_balanceado[ dataset_balanceado['Estacao_Ano'] == 'Verão' ]['Humidade_Solo'].mean() ) 
print( 'MAX Humidade_Solo VERAO', dataset_balanceado[ dataset_balanceado['Estacao_Ano'] == 'Verão' ]['Humidade_Solo'].max() ) 

print('')

# qual a média de Humidade_Solo no outono
print( 'MIN Humidade_Solo OUTONO', dataset_balanceado[ dataset_balanceado['Estacao_Ano'] == 'Outono' ]['Humidade_Solo'].min() ) 
print( 'MEDIA Humidade_Solo OUTONO', dataset_balanceado[ dataset_balanceado['Estacao_Ano'] == 'Outono' ]['Humidade_Solo'].mean() ) 
print( 'MAX Humidade_Solo OUTONO', dataset_balanceado[ dataset_balanceado['Estacao_Ano'] == 'Outono' ]['Humidade_Solo'].max() ) 

print('')

# qual a Humidade_Solo de chuvas no inverno
print( 'MIN Humidade_Solo INVERNO', dataset_balanceado[ dataset_balanceado['Estacao_Ano'] == 'Inverno' ]['Humidade_Solo'].min() ) 
print( 'MEDIA Humidade_Solo INVERNO', dataset_balanceado[ dataset_balanceado['Estacao_Ano'] == 'Inverno' ]['Humidade_Solo'].mean() ) 
print( 'MAX Humidade_Solo INVERNO', dataset_balanceado[ dataset_balanceado['Estacao_Ano'] == 'Inverno' ]['Humidade_Solo'].max() ) 

print('')

"""
Faz sentido!
e não só isso, o padrão se manteve exatamente o mesmo, porém com valores negativos
por exemplo a subtração do percentil 25% subtraido com o percentil 50%, deu 19, igual era antes, então a proporção dos valores não mudou
"""


"""
Agora eu preciso ver se existem Outliers(amostras que valores extremos ou fora do padrão), e se tiver, remover eles
"""
import seaborn as sns
import matplotlib.pyplot as plt

"""
Para esse exemplo, eu sei que os outliers estão apenas na coluna PRECO VENDA,
pois eu propositalmente criei esse dataset para ter Outliers nessa coluna para ensinar como identificar eles
"""


print('\n')

# OUTLIERS PARA O PRECO VENDA
# Criar um boxplot para uma variável específica
sns.boxplot(x=dataset_balanceado['Preco_Venda'])
plt.title('Boxplot de Preco_Venda')
plt.show()

print('\n')
print('PROCURANDO OUTLIERS USANDO QUARTIS')
print('\n')

# Calcular o IQR (Intervalo Interquartil)
Q1 = dataset_balanceado['Preco_Venda'].quantile(0.25)
Q3 = dataset_balanceado['Preco_Venda'].quantile(0.75)
IQR = Q3 - Q1

# Definir limites para outliers
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

# Filtrar os outliers
outliers = dataset_balanceado[(dataset_balanceado['Preco_Venda'] < limite_inferior) | 
                              (dataset_balanceado['Preco_Venda'] > limite_superior)]

print("Outliers encontrados:\n", outliers)


print('\n')
print('PROCURANDO OUTLIERS USANDO ZSCORE')
print('\n')
from scipy.stats import zscore

# Calcular Z-score para a coluna
dataset_balanceado['Z_Score'] = zscore(dataset_balanceado['Preco_Venda'])

# Identificar os indices dos Outliers
outliers_testeZ = dataset_balanceado[(dataset_balanceado['Z_Score'] > 3) | (dataset_balanceado['Z_Score'] < -3)]
print("Outliers pelo Z-Score:\n", outliers_testeZ)

"""
Como voce pode ver no gráfico do matplotlib, existem amostras que tem o Preco_Venda muito alto!, valores extremos que fogem do padrão. 
E isso é um exemplo de outlier que precisa ser tratado.

Esses não são os unicos tipos que podem existir.
Podem haver outros tipos de Outliers também, mais todos eles vão ter algo em comum: Vão ser valores extremos.

Nos outros dois testes feitos com quartis e com o Z-Score, vemos que existem no mínimo de 7 a 18 outliers, na coluna Preco_Venda.
Ou seja, existem de 7 a 18 amostras que tem valores extremos na coluna Preco_Venda. E precisam ser tratados ou removidos.
"""

"""
Eu fiz dois tipos de testes: teste dos quartis e no teste do ZTEST
Cada teste tem resultados diferentes.

Eu na minha opinião, acho que remover 18 outliers(apontados pelo teste dos quartis) poderia ser algo não muito bom, pois, tem muitas amostras do verão, e pouca das outras,
isso poderia desbalancear meu dataset

Então vou optar por remover os 7 Outliers apontados pelo ZTEST, que são mais especificos, e vai afetar menos meu dataset

VOU REMOVER
"""

# Removendo os 7 Outliers apontados pelo ZTEST,  pelos índices deles
outliers_indices = outliers_testeZ.index
dataset_sem_outliers = dataset_balanceado.drop(outliers_indices, axis=0)

"""
Agora eu posso visualizar o dataset pra ver como ficou
"""
print( dataset_sem_outliers.describe() )

print( dataset_sem_outliers.head(10) )

"""
Pronto, os Outliers foram removidos!
"""

"""
Agora vou reduzir um pouco a escala do preço de venda e custo cultivo, pra ficar menor
"""
dataset_sem_outliers['Custo_Cultivo'] = dataset_sem_outliers['Custo_Cultivo'] / 10
dataset_sem_outliers['Preco_Venda'] = dataset_sem_outliers['Preco_Venda'] / 10

"""
Isso não ajuda muito, mais não cria valores muito grandes demais
"""

"""
Agora eu posso visualizar o dataset pra ver como ficou
"""
print( dataset_sem_outliers.describe() )

print( dataset_sem_outliers.head(10) )


"""
No pandas, tambem podemos criar novas colunas, usando colunas já existentes, ou cálculos matemáticos sobre os valores das colunas já existentes
Abaixo eu criei um exemplo bem simples para criar algumas novas colunas:
"""

"""
Tambem quero criar uma nova coluna chamada Altura_mm, para ser a altura em metros
"""
dataset_sem_outliers['Altura_mm'] = dataset_sem_outliers['Altura_cm'] / 100

"""
Tambem quero fazer uma nova coluna pra representar a chuva em metros
"""
dataset_sem_outliers['Chuva_mm'] = dataset_sem_outliers['Chuva_mm'] / 100

"""
Tambem quero criar uma nova coluna para representar a diferença entre o Preço de Venda e o Custo de Cultivo
"""
dataset_sem_outliers['dif_preco_venda_custo_cultivo'] = dataset_sem_outliers['Preco_Venda'] - dataset_sem_outliers['Custo_Cultivo']

"""
Tambem quero remover a coluna ZScore, que é desnecessária
"""
dataset_sem_outliers = dataset_sem_outliers.drop('Z_Score', axis=1);

"""
Essa ideia de criar novas colunas é chamada de Feature Engineering, que significa Engenharia de Features, pois permite criar/inventar novas features, ou caracteristicas
"""

"""
Agora eu posso visualizar o dataset pra ver como ficou
"""
print( dataset_sem_outliers.describe() )

print( dataset_sem_outliers.head(10) )

"""
Porém, ao criar novas features, notei que na maioria das vezes o Custo_Cultivo é muito maior do que o Preco_Venda
Sendo que o preço de venda deveria ser um pouco maior que o Custo_Cultivo
Essa simulação não fez sentido
"""

# Analisando esse problema, em cada versão do meu dataset, ao longo dos tratamentos que eu fiz
dataset['custo_maior_que_venda'] = dataset['Custo_Cultivo'] > dataset['Preco_Venda']
print(dataset['custo_maior_que_venda'].sum(), dataset.shape)

dataset_balanceado['custo_maior_que_venda'] = dataset_balanceado['Custo_Cultivo'] > dataset_balanceado['Preco_Venda']
print(dataset_balanceado['custo_maior_que_venda'].sum(), dataset_balanceado.shape)

dataset_sem_outliers['custo_maior_que_venda'] = dataset_sem_outliers['Custo_Cultivo'] > dataset_sem_outliers['Preco_Venda']
print(dataset_sem_outliers['custo_maior_que_venda'].sum(), dataset_sem_outliers.shape)

"""
Ao analisar:

2944 (3000, 24)
869 (875, 25)
868 (868, 26)

vi que esse padrão se manteve em cada versão do meu dataset, ao longo dos tratamentos que eu fiz~
Eu preciso tratar isso!
"""

"""
Vou aumentar o Preco_Venda somando com o Custo_Cultivo, acredito que isso faça sentido
"""
# Tratei isso
dataset_sem_outliers['Preco_Venda'] = dataset_sem_outliers['Preco_Venda'] + dataset_sem_outliers['Custo_Cultivo']

# Analisando se esse problema foi resolvido
dataset_sem_outliers['custo_maior_que_venda'] = dataset_sem_outliers['Custo_Cultivo'] > dataset_sem_outliers['Preco_Venda']
print(dataset_sem_outliers['custo_maior_que_venda'].sum(), dataset_sem_outliers.shape)

"""
E agora foi:

0 (868, 26)

O que significa que eu consegui tratar isso!
"""

"""
Agora eu preciso calcular denovo a diferença entre o Custo_Cultivo e Preço_Venda
"""
dataset_sem_outliers['dif_preco_venda_custo_cultivo'] = dataset_sem_outliers['Preco_Venda'] - dataset_sem_outliers['Custo_Cultivo']

"""
Tambem vou remover a coluna custo_maior_que_venda que é desnecessária
"""
dataset_sem_outliers = dataset_sem_outliers.drop('custo_maior_que_venda', axis=1);

"""
Agora eu posso visualizar o dataset pra ver como ficou
"""
print( dataset_sem_outliers.describe() )

print( dataset_sem_outliers.head(10) )

"""
Agora ficou certo,
O Preco_Venda sempre vai ser maior que o Custo_Cultivo
"""

"""
Montei gráficos para analisar melhor

Notei mudanças para fazer no tempo de crescimento das plantas:
 
  Primavera: Tempo mais curto (crescimento rápido devido ao clima ameno e boas condições).  

  Verão: Tempo ainda um pouco menor que a primavera (mais luz solar acelera o crescimento, mas pode haver estresse térmico).  

  Outono: Tempo um pouco maior que no verão (temperaturas mais baixas desaceleram o crescimento).  

  Inverno: Tempo mais longo (crescimento mais lento devido à baixa temperatura e menos luz solar).  

"""

dataset_sem_outliers.loc[dataset_sem_outliers['Estacao_Ano'] == 'Primavera', 'Tempo_Crescimento_horas'] -= 850;
# A soja precisa demorar um pouco menos nessa estação
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Primavera') & (dataset_sem_outliers['Tipo_Planta'] == 'Soja'), 'Tempo_Crescimento_horas'] -= 30;
# O trigo precisa demorar um pouco mias nessa estação
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Primavera') & (dataset_sem_outliers['Tipo_Planta'] == 'Trigo'), 'Tempo_Crescimento_horas'] += 25;
# O tomate precisa demorar um pouco menos nessa estação
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Primavera') & (dataset_sem_outliers['Tipo_Planta'] == 'Tomate'), 'Tempo_Crescimento_horas'] -= 35;


dataset_sem_outliers.loc[dataset_sem_outliers['Estacao_Ano'] == 'Verão', 'Tempo_Crescimento_horas'] -= 1200;
# A soja precisa demorar um pouco menos nessa estação
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Verão') & (dataset_sem_outliers['Tipo_Planta'] == 'Soja'), 'Tempo_Crescimento_horas'] -= 160;
# O trigo precisa demorar um pouco menos nessa estação
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Verão') & (dataset_sem_outliers['Tipo_Planta'] == 'Trigo'), 'Tempo_Crescimento_horas'] -= 4;
# O tomate precisa demorar um pouco menos nessa estação
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Verão') & (dataset_sem_outliers['Tipo_Planta'] == 'Tomate'), 'Tempo_Crescimento_horas'] -= 60;

dataset_sem_outliers.loc[dataset_sem_outliers['Estacao_Ano'] == 'Outono', 'Tempo_Crescimento_horas'] -= 370;
# A batata precisa demorar um pouco menos nessa estação
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Outono') & (dataset_sem_outliers['Tipo_Planta'] == 'Batata'), 'Tempo_Crescimento_horas'] -= 25;
# A cenoura precisa demorar um pouco menos nessa estação
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Outono') & (dataset_sem_outliers['Tipo_Planta'] == 'Cenoura'), 'Tempo_Crescimento_horas'] -= 15;
# A soja precisa demorar um pouco menos nessa estação
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Outono') & (dataset_sem_outliers['Tipo_Planta'] == 'Soja'), 'Tempo_Crescimento_horas'] -= 20;
# A tomate precisa demorar um pouco mais nessa estação
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Outono') & (dataset_sem_outliers['Tipo_Planta'] == 'Tomate'), 'Tempo_Crescimento_horas'] += 10;


dataset_sem_outliers.loc[dataset_sem_outliers['Estacao_Ano'] == 'Inverno', 'Tempo_Crescimento_horas'] -= 215;


"""
Percebi que eu tambem preciso tratar o tempo de vida dias por cada estação do ano pra fazer mais sentido
"""
dataset_sem_outliers.loc[dataset_sem_outliers['Estacao_Ano'] == 'Primavera', 'Tempo_Vida_dias'] -= 3;
dataset_sem_outliers.loc[dataset_sem_outliers['Estacao_Ano'] == 'Verão', 'Tempo_Vida_dias'] += 38;

dataset_sem_outliers.loc[dataset_sem_outliers['Estacao_Ano'] == 'Outono', 'Tempo_Vida_dias'] -= 40;
dataset_sem_outliers.loc[dataset_sem_outliers['Estacao_Ano'] == 'Inverno', 'Tempo_Vida_dias'] -= 90;


"""
Percebi que a coluna Nivel_Pesticida tem valores negativos
Quero tratar tambem

Vou elimitar os negativos, e vou fazer da forma que fiz no outro, pra não precisar mexer na escala

Como eu sei que o minimo do Nivel_Pesticida foi -80, eu somo com esse valor positivo e mais um pouco
"""
dataset_sem_outliers['Nivel_Pesticida'] = dataset_sem_outliers['Nivel_Pesticida'] + 89;

"""
Pronto!
Agora ficou bom
"""

"""
Eu quero verificar tambem o Frequencia_Podas e o Nivel_Pesticida, por estação, pra ver se o padrão está refletindo o que eu quero
"""

"""
Vou começar vendo o Nivel_Pesticida por estação
"""
print('\nMEDIAS Nivel_Pesticida POR ESTAÇÂO:')

# qual a média da Nivel_Pesticida na primavera
print( 'MIN Nivel_Pesticida PRIMAVERA', dataset_sem_outliers[ dataset_sem_outliers['Estacao_Ano'] == 'Primavera' ]['Nivel_Pesticida'].min() ) 
print( 'MEDIA Nivel_Pesticida PRIMAVERA', dataset_sem_outliers[ dataset_sem_outliers['Estacao_Ano'] == 'Primavera' ]['Nivel_Pesticida'].mean() ) 
print( 'MAX Nivel_Pesticida PRIMAVERA', dataset_sem_outliers[ dataset_sem_outliers['Estacao_Ano'] == 'Primavera' ]['Nivel_Pesticida'].max() ) 

print('')

# qual a média de Nivel_Pesticida no verao
print( 'MIN Nivel_Pesticida VERAO', dataset_sem_outliers[ dataset_sem_outliers['Estacao_Ano'] == 'Verão' ]['Nivel_Pesticida'].min() ) 
print( 'MEDIA Nivel_Pesticida VERAO', dataset_sem_outliers[ dataset_sem_outliers['Estacao_Ano'] == 'Verão' ]['Nivel_Pesticida'].mean() ) 
print( 'MAX Nivel_Pesticida VERAO', dataset_sem_outliers[ dataset_sem_outliers['Estacao_Ano'] == 'Verão' ]['Nivel_Pesticida'].max() ) 

print('')

# qual a média de Nivel_Pesticida no outono
print( 'MIN Nivel_Pesticida OUTONO', dataset_sem_outliers[ dataset_sem_outliers['Estacao_Ano'] == 'Outono' ]['Nivel_Pesticida'].min() ) 
print( 'MEDIA Nivel_Pesticida OUTONO', dataset_sem_outliers[ dataset_sem_outliers['Estacao_Ano'] == 'Outono' ]['Nivel_Pesticida'].mean() ) 
print( 'MAX Nivel_Pesticida OUTONO', dataset_sem_outliers[ dataset_sem_outliers['Estacao_Ano'] == 'Outono' ]['Nivel_Pesticida'].max() ) 

print('')

# qual a Nivel_Pesticida de chuvas no inverno
print( 'MIN Nivel_Pesticida INVERNO', dataset_sem_outliers[ dataset_sem_outliers['Estacao_Ano'] == 'Inverno' ]['Nivel_Pesticida'].min() ) 
print( 'MEDIA Nivel_Pesticida INVERNO', dataset_sem_outliers[ dataset_sem_outliers['Estacao_Ano'] == 'Inverno' ]['Nivel_Pesticida'].mean() ) 
print( 'MAX Nivel_Pesticida INVERNO', dataset_sem_outliers[ dataset_sem_outliers['Estacao_Ano'] == 'Inverno' ]['Nivel_Pesticida'].max() ) 

print('')

"""
MEDIAS Nivel_Pesticida POR ESTAÇÂO:
MIN Nivel_Pesticida PRIMAVERA 88.75335863851059
MEDIA Nivel_Pesticida PRIMAVERA 91.25124714909755
MAX Nivel_Pesticida PRIMAVERA 93.71821420900419

MIN Nivel_Pesticida VERAO 88.74795040396387
MEDIA Nivel_Pesticida VERAO 91.24298626905178
MAX Nivel_Pesticida VERAO 93.7370857402004

MIN Nivel_Pesticida OUTONO 84.26829101511547
MEDIA Nivel_Pesticida OUTONO 86.54059781052068
MAX Nivel_Pesticida OUTONO 89.23421439356044

MIN Nivel_Pesticida INVERNO 8.756710420398761
MEDIA Nivel_Pesticida INVERNO 11.192677018837143
MAX Nivel_Pesticida INVERNO 13.729130800567091

Analisando, eu tive a ideia de:
  Diminuir um pouquino a Primavera pra ficar abaixo do Verão
  Aumentar um pouquino o Verão, por que tem mais pragas
  E no Outono diminuir mais um pouco pra mostrar que está indo Ritmo do inverno. O Outono precisa ficar abaixo da Primavera
"""
dataset_sem_outliers.loc[dataset_sem_outliers['Estacao_Ano'] == 'Primavera', 'Nivel_Pesticida'] -= 8;
dataset_sem_outliers.loc[dataset_sem_outliers['Estacao_Ano'] == 'Verão', 'Nivel_Pesticida'] += 10;
dataset_sem_outliers.loc[dataset_sem_outliers['Estacao_Ano'] == 'Outono', 'Nivel_Pesticida'] -= 18;

"""
Vou calcular as médias denovo
"""
print('\nMEDIAS Nivel_Pesticida POR ESTAÇÂO DEPOIS DE MUDAR:')

# qual a média da Nivel_Pesticida na primavera
print( 'MIN Nivel_Pesticida PRIMAVERA', dataset_sem_outliers[ dataset_sem_outliers['Estacao_Ano'] == 'Primavera' ]['Nivel_Pesticida'].min() ) 
print( 'MEDIA Nivel_Pesticida PRIMAVERA', dataset_sem_outliers[ dataset_sem_outliers['Estacao_Ano'] == 'Primavera' ]['Nivel_Pesticida'].mean() ) 
print( 'MAX Nivel_Pesticida PRIMAVERA', dataset_sem_outliers[ dataset_sem_outliers['Estacao_Ano'] == 'Primavera' ]['Nivel_Pesticida'].max() ) 

print('')

# qual a média de Nivel_Pesticida no verao
print( 'MIN Nivel_Pesticida VERAO', dataset_sem_outliers[ dataset_sem_outliers['Estacao_Ano'] == 'Verão' ]['Nivel_Pesticida'].min() ) 
print( 'MEDIA Nivel_Pesticida VERAO', dataset_sem_outliers[ dataset_sem_outliers['Estacao_Ano'] == 'Verão' ]['Nivel_Pesticida'].mean() ) 
print( 'MAX Nivel_Pesticida VERAO', dataset_sem_outliers[ dataset_sem_outliers['Estacao_Ano'] == 'Verão' ]['Nivel_Pesticida'].max() ) 

print('')

# qual a média de Nivel_Pesticida no outono
print( 'MIN Nivel_Pesticida OUTONO', dataset_sem_outliers[ dataset_sem_outliers['Estacao_Ano'] == 'Outono' ]['Nivel_Pesticida'].min() ) 
print( 'MEDIA Nivel_Pesticida OUTONO', dataset_sem_outliers[ dataset_sem_outliers['Estacao_Ano'] == 'Outono' ]['Nivel_Pesticida'].mean() ) 
print( 'MAX Nivel_Pesticida OUTONO', dataset_sem_outliers[ dataset_sem_outliers['Estacao_Ano'] == 'Outono' ]['Nivel_Pesticida'].max() ) 

print('')

# qual a Nivel_Pesticida de chuvas no inverno
print( 'MIN Nivel_Pesticida INVERNO', dataset_sem_outliers[ dataset_sem_outliers['Estacao_Ano'] == 'Inverno' ]['Nivel_Pesticida'].min() ) 
print( 'MEDIA Nivel_Pesticida INVERNO', dataset_sem_outliers[ dataset_sem_outliers['Estacao_Ano'] == 'Inverno' ]['Nivel_Pesticida'].mean() ) 
print( 'MAX Nivel_Pesticida INVERNO', dataset_sem_outliers[ dataset_sem_outliers['Estacao_Ano'] == 'Inverno' ]['Nivel_Pesticida'].max() ) 

print('')

"""
Ficou legal

Agora vou tratar a coluna Frequencia_Podas
"""
print('\nMEDIAS Frequencia_Podas POR ESTAÇÂO:')

# qual a média da Frequencia_Podas na primavera
print( 'MIN Frequencia_Podas PRIMAVERA', dataset_sem_outliers[ dataset_sem_outliers['Estacao_Ano'] == 'Primavera' ]['Frequencia_Podas'].min() ) 
print( 'MEDIA Frequencia_Podas PRIMAVERA', dataset_sem_outliers[ dataset_sem_outliers['Estacao_Ano'] == 'Primavera' ]['Frequencia_Podas'].mean() ) 
print( 'MAX Frequencia_Podas PRIMAVERA', dataset_sem_outliers[ dataset_sem_outliers['Estacao_Ano'] == 'Primavera' ]['Frequencia_Podas'].max() ) 

print('')

# qual a média de Frequencia_Podas no verao
print( 'MIN Frequencia_Podas VERAO', dataset_sem_outliers[ dataset_sem_outliers['Estacao_Ano'] == 'Verão' ]['Frequencia_Podas'].min() ) 
print( 'MEDIA Frequencia_Podas VERAO', dataset_sem_outliers[ dataset_sem_outliers['Estacao_Ano'] == 'Verão' ]['Frequencia_Podas'].mean() ) 
print( 'MAX Frequencia_Podas VERAO', dataset_sem_outliers[ dataset_sem_outliers['Estacao_Ano'] == 'Verão' ]['Frequencia_Podas'].max() ) 

print('')

# qual a média de Frequencia_Podas no outono
print( 'MIN Frequencia_Podas OUTONO', dataset_sem_outliers[ dataset_sem_outliers['Estacao_Ano'] == 'Outono' ]['Frequencia_Podas'].min() ) 
print( 'MEDIA Frequencia_Podas OUTONO', dataset_sem_outliers[ dataset_sem_outliers['Estacao_Ano'] == 'Outono' ]['Frequencia_Podas'].mean() ) 
print( 'MAX Frequencia_Podas OUTONO', dataset_sem_outliers[ dataset_sem_outliers['Estacao_Ano'] == 'Outono' ]['Frequencia_Podas'].max() ) 

print('')

# qual a Frequencia_Podas de chuvas no inverno
print( 'MIN Frequencia_Podas INVERNO', dataset_sem_outliers[ dataset_sem_outliers['Estacao_Ano'] == 'Inverno' ]['Frequencia_Podas'].min() ) 
print( 'MEDIA Frequencia_Podas INVERNO', dataset_sem_outliers[ dataset_sem_outliers['Estacao_Ano'] == 'Inverno' ]['Frequencia_Podas'].mean() ) 
print( 'MAX Frequencia_Podas INVERNO', dataset_sem_outliers[ dataset_sem_outliers['Estacao_Ano'] == 'Inverno' ]['Frequencia_Podas'].max() ) 

print('')

"""
Eu não acho que seja necessário tratar nada aqui
MEDIAS Frequencia_Podas POR ESTAÇÂO DEPOIS DE MUDAR:
MIN Frequencia_Podas PRIMAVERA 2.0
MEDIA Frequencia_Podas PRIMAVERA 6.626666666666667
MAX Frequencia_Podas PRIMAVERA 11.0

MIN Frequencia_Podas VERAO 2.0
MEDIA Frequencia_Podas VERAO 6.6298076923076925
MAX Frequencia_Podas VERAO 11.0

MIN Frequencia_Podas OUTONO 1.5
MEDIA Frequencia_Podas OUTONO 3.129018767528854
MAX Frequencia_Podas OUTONO 6.5

MIN Frequencia_Podas INVERNO 1.5002815696779608
MEDIA Frequencia_Podas INVERNO 1.7531050181307093
MAX Frequencia_Podas INVERNO 1.9949520399371448
"""


"""
Analisando os graficos, eu ainda quero tratar a Altura_cm, para ela refletir melhor os padrões das estações do ano, e reforçar mais o padrão de cada planta
"""

"""
Vou calcular as médidas de Altura por estação
"""
print('\nMEDIAS Altura_cm POR ESTAÇÂO:')

# qual a média da NivelAltura_cm_Pesticida na primavera
print( 'MIN Altura_cm PRIMAVERA', dataset_sem_outliers[ dataset_sem_outliers['Estacao_Ano'] == 'Primavera' ]['Altura_cm'].min() ) 
print( 'MEDIA Altura_cm PRIMAVERA', dataset_sem_outliers[ dataset_sem_outliers['Estacao_Ano'] == 'Primavera' ]['Altura_cm'].mean() ) 
print( 'MAX Altura_cm PRIMAVERA', dataset_sem_outliers[ dataset_sem_outliers['Estacao_Ano'] == 'Primavera' ]['Altura_cm'].max() ) 

print('')

# qual a média de Altura_cm no verao
print( 'MIN Altura_cm VERAO', dataset_sem_outliers[ dataset_sem_outliers['Estacao_Ano'] == 'Verão' ]['Altura_cm'].min() ) 
print( 'MEDIA Altura_cm VERAO', dataset_sem_outliers[ dataset_sem_outliers['Estacao_Ano'] == 'Verão' ]['Altura_cm'].mean() ) 
print( 'MAX Altura_cm VERAO', dataset_sem_outliers[ dataset_sem_outliers['Estacao_Ano'] == 'Verão' ]['Altura_cm'].max() ) 

print('')

# qual a média de Altura_cm no outono
print( 'MIN Altura_cm OUTONO', dataset_sem_outliers[ dataset_sem_outliers['Estacao_Ano'] == 'Outono' ]['Altura_cm'].min() ) 
print( 'MEDIA Altura_cm OUTONO', dataset_sem_outliers[ dataset_sem_outliers['Estacao_Ano'] == 'Outono' ]['Altura_cm'].mean() ) 
print( 'MAX Altura_cm OUTONO', dataset_sem_outliers[ dataset_sem_outliers['Estacao_Ano'] == 'Outono' ]['Altura_cm'].max() ) 

print('')

# qual a Altura_cm de chuvas no inverno
print( 'MIN Altura_cm INVERNO', dataset_sem_outliers[ dataset_sem_outliers['Estacao_Ano'] == 'Inverno' ]['Altura_cm'].min() ) 
print( 'MEDIA Altura_cm INVERNO', dataset_sem_outliers[ dataset_sem_outliers['Estacao_Ano'] == 'Inverno' ]['Altura_cm'].mean() ) 
print( 'MAX Altura_cm INVERNO', dataset_sem_outliers[ dataset_sem_outliers['Estacao_Ano'] == 'Inverno' ]['Altura_cm'].max() ) 

print('')

"""
Nas médias

MEDIAS Altura_cm POR ESTAÇÂO:
MIN Altura_cm PRIMAVERA 570.1529472844369
MEDIA Altura_cm PRIMAVERA 1097.2191176192623
MAX Altura_cm PRIMAVERA 1530.456724216624

MIN Altura_cm VERAO 490.99212836782254
MEDIA Altura_cm VERAO 1169.1226788700808
MAX Altura_cm VERAO 1655.9892149813713

MIN Altura_cm OUTONO 799.9801296078371
MEDIA Altura_cm OUTONO 1224.3013677639879
MAX Altura_cm OUTONO 1713.2223540637722

MIN Altura_cm INVERNO 631.2714618605553
MEDIA Altura_cm INVERNO 924.5964319324788
MAX Altura_cm INVERNO 1256.5416605140344

Parece que não faz muito sentido a Altura no Verão ser menor do que no Outono por exemplo
"""

"""
Primeiro vou aplicar um reforço no padrão das estações do ano, pra frizar quais estações tendem as plantas a terem maior altura e quais menos
"""
# O Verão precisa ter as maiores alturas de planta
dataset_sem_outliers.loc[dataset_sem_outliers['Estacao_Ano'] == 'Verão', 'Altura_cm'] += 250;
#O outono precisa ser um pouco mais baixo que o Verão
dataset_sem_outliers.loc[dataset_sem_outliers['Estacao_Ano'] == 'Outono', 'Altura_cm'] -= 115;
#O inverno precisa ser bem mais baixo a altura
dataset_sem_outliers.loc[dataset_sem_outliers['Estacao_Ano'] == 'Inverno', 'Altura_cm'] -= 170;

"""
Agora vou reforçar alguns padrões especificos, para cada planta
"""
# na primavera a cenoura cresce um pouco mais
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Primavera') & (dataset_sem_outliers['Tipo_Planta'] == 'Cenoura'), 'Altura_cm'] -= 210;
# na primavera, a batata precisa diminuir um pouquinho a altura
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Primavera') & (dataset_sem_outliers['Tipo_Planta'] == 'Batata'), 'Altura_cm'] -= 55;
# na primavera, o milho precisa diminuir um pouquinho a altura
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Primavera') & (dataset_sem_outliers['Tipo_Planta'] == 'Milho'), 'Altura_cm'] -= 210;
# na primavera, a soja precisa diminuir um pouquinho a altura
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Primavera') & (dataset_sem_outliers['Tipo_Planta'] == 'Soja'), 'Altura_cm'] -= 10;
# na primavera, o tomate precisa diminuir um pouquinho a altura
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Primavera') & (dataset_sem_outliers['Tipo_Planta'] == 'Tomate'), 'Altura_cm'] -= 130;

# no verão, a batata precisa diminuir um pouquinho a altura
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Verão') & (dataset_sem_outliers['Tipo_Planta'] == 'Batata'), 'Altura_cm'] -= 200;
# no verão, a cenora precisa diminuir um pouquinho a altura
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Verão') & (dataset_sem_outliers['Tipo_Planta'] == 'Cenoura'), 'Altura_cm'] -= 210;
# no verão, o milho 
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Verão') & (dataset_sem_outliers['Tipo_Planta'] == 'Milho'), 'Altura_cm'] -= 0;
# no verão, a soja precisa diminuir um pouquinho a altura
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Verão') & (dataset_sem_outliers['Tipo_Planta'] == 'Soja'), 'Altura_cm'] -= 10;
# no verão, o tomate precisa diminuir um pouquinho a altura
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Verão') & (dataset_sem_outliers['Tipo_Planta'] == 'Tomate'), 'Altura_cm'] -= 18;
# no verão, o trigo precisa diminuir um pouquinho a altura
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Verão') & (dataset_sem_outliers['Tipo_Planta'] == 'Trigo'), 'Altura_cm'] -= 200;

# no outono, a cenora precisa diminuir um pouquinho a altura
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Outono') & (dataset_sem_outliers['Tipo_Planta'] == 'Cenoura'), 'Altura_cm'] -= 65;
# no outono, o milho precisa diminuir um pouquinho a altura
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Outono') & (dataset_sem_outliers['Tipo_Planta'] == 'Milho'), 'Altura_cm'] -= 210;
# no outono, o tomate precisa diminuir um pouquinho a altura
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Outono') & (dataset_sem_outliers['Tipo_Planta'] == 'Tomate'), 'Altura_cm'] -= 260;
# no outono, a soja precisa diminuir um pouquinho a altura
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Outono') & (dataset_sem_outliers['Tipo_Planta'] == 'Soja'), 'Altura_cm'] -= 205;
# no outono, o trigo precisa diminuir um pouquinho a altura
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Outono') & (dataset_sem_outliers['Tipo_Planta'] == 'Trigo'), 'Altura_cm'] -= 15;

# no inverno, a cenora precisa diminuir um pouquinho a altura
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Inverno') & (dataset_sem_outliers['Tipo_Planta'] == 'Cenoura'), 'Altura_cm'] -= 45;
# no inverno, a batata precisa diminuir um pouquinho a altura
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Inverno') & (dataset_sem_outliers['Tipo_Planta'] == 'Batata'), 'Altura_cm'] -= 108;
# no inverno, o milho precisa diminuir um pouquinho a altura
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Inverno') & (dataset_sem_outliers['Tipo_Planta'] == 'Milho'), 'Altura_cm'] -= 108;
# no inverno, a soja precisa diminuir um pouquinho a altura
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Inverno') & (dataset_sem_outliers['Tipo_Planta'] == 'Soja'), 'Altura_cm'] -= 108;
# no inverno, o trigo precisa diminuir um pouquinho a altura
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Inverno') & (dataset_sem_outliers['Tipo_Planta'] == 'Trigo'), 'Altura_cm'] -= 108;
# no inverno, não faz sentido o tomate creser mais, precisa diminuir um pouquinho a altura
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Inverno') & (dataset_sem_outliers['Tipo_Planta'] == 'Tomate'), 'Altura_cm'] -= 140;


"""
Ficou bom
"""

"""
Agora vou retocar o Tempo de Crescimento de cada tipo de planta por estação
"""
# Na primavera aumentar um pouco mais o tempo de crescimento pra balancear um pouco
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Primavera'), 'Tempo_Crescimento_horas'] += 60;
# No inverno aumentar ainda mais o tempo de crescimento pra ficar bem evidente
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Inverno'), 'Tempo_Crescimento_horas'] += 210;
# No outono diminuir um pouco mais o tempo de crescimento pra não exagerar
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Outono'), 'Tempo_Crescimento_horas'] -= 150;


# Tomate: Cresce mais rapido na primavera e verão
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Primavera') & (dataset_sem_outliers['Tipo_Planta'] == 'Tomate'), 'Tempo_Crescimento_horas'] -= 150;
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Verão') & (dataset_sem_outliers['Tipo_Planta'] == 'Tomate'), 'Tempo_Crescimento_horas'] -= 100;
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Outono') & (dataset_sem_outliers['Tipo_Planta'] == 'Tomate'), 'Tempo_Crescimento_horas'] += 150; # No outono demora mais pra crescer, pois parece que diminui

# Cenora: Cresce mais rapido na primavera e outono
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Primavera') & (dataset_sem_outliers['Tipo_Planta'] == 'Cenoura'), 'Tempo_Crescimento_horas'] -= 150;
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Outono') & (dataset_sem_outliers['Tipo_Planta'] == 'Cenoura'), 'Tempo_Crescimento_horas'] -= 190; 
# Vou aplicar a mesma coisa pro Inverno
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Inverno') & (dataset_sem_outliers['Tipo_Planta'] == 'Cenoura'), 'Tempo_Crescimento_horas'] -= 225; 

# Trigo: Cresce mais rapido na primavera e verão
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Primavera') & (dataset_sem_outliers['Tipo_Planta'] == 'Trigo'), 'Tempo_Crescimento_horas'] -= 150;
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Verão') & (dataset_sem_outliers['Tipo_Planta'] == 'Trigo'), 'Tempo_Crescimento_horas'] -= 120; 
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Outono') & (dataset_sem_outliers['Tipo_Planta'] == 'Trigo'), 'Tempo_Crescimento_horas'] += 150; # No outono demora mais pra crescer, pois parece que diminui

# Batata: Cresce mais rapido na primavera e verão
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Primavera') & (dataset_sem_outliers['Tipo_Planta'] == 'Batata'), 'Tempo_Crescimento_horas'] -= 190;
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Verão') & (dataset_sem_outliers['Tipo_Planta'] == 'Batata'), 'Tempo_Crescimento_horas'] -= 170; 
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Outono') & (dataset_sem_outliers['Tipo_Planta'] == 'Batata'), 'Tempo_Crescimento_horas'] += 150; # No outono demora mais pra crescer, pois parece que diminui

# Milho: Cresce mais rapido no verão apenas
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Verão') & (dataset_sem_outliers['Tipo_Planta'] == 'Milho'), 'Tempo_Crescimento_horas'] -= 50; 
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Outono') & (dataset_sem_outliers['Tipo_Planta'] == 'Milho'), 'Tempo_Crescimento_horas'] += 100; 

# Soja: Cresce mais rapido no verão apenas
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Verão') & (dataset_sem_outliers['Tipo_Planta'] == 'Soja'), 'Tempo_Crescimento_horas'] -= 200; 
dataset_sem_outliers.loc[(dataset_sem_outliers['Estacao_Ano'] == 'Outono') & (dataset_sem_outliers['Tipo_Planta'] == 'Soja'), 'Tempo_Crescimento_horas'] += 100; 


# Salvar CSV
dataset_sem_outliers.to_csv('datasets/dataset-tratado-normalizado-sem-outliers.csv', index=False, sep=';')
print("Dataset atualizado com sucesso!")



tentando_abrir = pd.read_csv('datasets/dataset-tratado-normalizado-sem-outliers.csv', sep=';');

"""
Agora eu posso visualizar o dataset pra ver como ficou
"""
print( tentando_abrir.describe() )

print( tentando_abrir.head(10) )
