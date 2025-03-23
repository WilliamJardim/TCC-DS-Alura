# Necessidade de normalizar os dados
Na hora de gerar o dataset, eu acabei gerando dados ficticios, sem me preocupar com escala, pois eu queria propositalmente um dataset com alguns problemas como esses, para mostrar como lidar com eles. 

Como vimos na primeira etapa de [Análise Exploratória](../analise-exporatoria/), no script `analise-basica.py`, existem muitos valores em escalas enormes, em faixa de milhões, o que é um baita exagero!


## Exemplo de colunas que tem valores em escalas extremas
Valores como:
<pre>
Temperatura_C     Chuva_mm  Horas_Sol_Dia  Humidade_Solo  Frequencia_Podas  ...  Tempo_Crescimento_horas  Litros_Agua_Semana  Custo_Cultivo   Preco_Venda  Tempo_Vida_dias
count    3000.000000  3000.000000    3000.000000    2975.000000       3000.000000  ...             3.000000e+03        3.000000e+03   2.990000e+03  3.000000e+03     3.000000e+03
mean      -19.259555    74.953493     -35.918143      37.629188        -17.451000  ...             9.082197e+05        7.526629e+05   2.547188e+08  5.762628e+10     2.831568e+06
std        75.242972    89.638360      70.240618      24.922044         34.724192  ...             4.741514e+05        1.968979e+05   1.301182e+08  4.983617e+10     1.605434e+06
min      -159.971698  -129.919691    -157.965008     -20.390887        -80.000000  ...             1.880800e+05        3.012891e+05  -4.799936e+07 -1.915901e+10    -3.494612e+06
25%      -131.123078    17.606081    -150.332400      19.558552        -71.000000  ...             5.249483e+05        6.037221e+05   1.506293e+08  2.454040e+10     1.480987e+06
50%        19.734231    78.117093       3.394958      38.348396          1.000000  ...             7.166597e+05        7.373271e+05   2.396445e+08  4.773649e+10     3.261369e+06
75%        29.772989   143.589816       8.550532      57.561895          4.500000  ...             1.322659e+06        9.010537e+05   3.600127e+08  7.973994e+10     4.127169e+06
max        49.986731   249.160474      13.994681      81.486994          9.000000  ...             2.952793e+06        1.451219e+06   6.847427e+08  7.266834e+11     5.470994e+06

[8 rows x 19 columns]
</pre>

Eu criei esse dataset e sei quais são as colunas que vão ter valores muito altos. 
As colunas `Tempo_Crescimento_horas`, `Litros_Agua_Semana`, `Custo_Cultivo`, `Preco_Venda`, 

## Normalizando o tempo de crescimento para fazer mais sentido
Eu quero normalizar o tempo de crescimento, para fazer mais sentido com a vida real. E para saber se essa normalização faz mais sentido, eu preciso pesquisar o tempo de crescimento das plantas usadas:

## Tempos de Crescimento Comuns para plantas:

  - Trigo: Pode levar de 90 a 120 dias para crescer totalmente, o que equivale a cerca de 2.160 a 2.880 horas.

  - Tomate: Normalmente leva entre 50 a 85 dias para amadurecer, ou seja, de 1.200 a 2.040 horas.

  - Milho: O milho geralmente cresce em torno de 60 a 100 dias, o que equivale a 1.440 a 2.400 horas.

  - Cenoura: Leva entre 70 a 80 dias para crescer, ou seja, de 1.680 a 1.920 horas.

  - Soja: O tempo de crescimento varia, mas pode ser de 100 a 150 dias, o que dá entre 2.400 a 3.600 horas.

No trecho de código do arquivo `reduzir_escala.py`, eu escrevi o seguinte:
<pre>
<code>
dataset = pd.read_csv('./datasets/dataset-agricultura-v5-balanceado.csv', sep=';');

print('DATASET ANTES DE MUDAR A ESCALA DO TEMPO CRESCIMENTO:')
print(dataset.head()['Tempo_Crescimento_horas'])

dataset['Tempo_Crescimento_horas'] = dataset['Tempo_Crescimento_horas'] / 999

print('DATASET DEPOIS DE MUDAR A ESCALA DO TEMPO CRESCIMENTO')
print(dataset.head()['Tempo_Crescimento_horas'])
</code>
</pre>

Como voce pode ver, eu dividi os dados de `Tempo_Crescimento_horas` assim: `dataset['Tempo_Crescimento_horas'] / 999`, e isso funcionou muito bem para essa coluna!

## Valores de tempo de crescimento ANTES DA NORMALIZAÇÂO
<pre>
DATASET ANTES DE MUDAR A ESCALA DO TEMPO CRESCIMENTO:
0    1.283856e+06
1    1.365897e+06
2    1.612399e+06
3    1.404261e+06
4    1.414649e+06
Name: Tempo_Crescimento_horas, dtype: float64
</pre>

## Valores de tempo de crescimento DEPOIS DA NORMALIZAÇÂO
<pre>
DATASET DEPOIS DE MUDAR A ESCALA DO TEMPO CRESCIMENTO
0    1285.141548
1    1367.263878
2    1614.013103
3    1405.667104
4    1416.065403
Name: Tempo_Crescimento_horas, dtype: float64
</pre>

Agora faz muito mais sentido!

Mais não acabou por aqui. Preciso normalizar as outras colunas.

