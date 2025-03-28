# Tratamento de dados do dataset
Na etapa anterior, eu mostrei como abrir um dataset com o pandas, e como visualizar ele usando gráficos, verificar se tem valores NaN ou Outliers, calcular médias moveis e correlação. **Agora nessa próxima etapa vou mostrar alguns tratamentos de dados que eu vou fazer nesse dataset.**

# Tratamento de Escala
Em alguns datasets, os valores das colunas podem ter valores bem grandes ou ter valores muito pequenos, que vão ser obviamente mais dificil de interpretar e ver com os olhos, e também, podem afetar a exibição de gráficos e modelos de Machine Learning. Por isso, se percebermos que o dataset tem valores em escalas muito grande ou muito pequenas, é necessário tratar isso, para deixar a informação mais clara. 

## Como tratar a Escala
Para tratar a escala podemos usar diferentes técnicas. Por exemplo, podemos dividir o valor da coluna que estamos tratando por um mesmo número fixo(por exemplo 10 ou 100), em cada uma das amostras, para diminuir a escala. Também podemos somar ou subtrair números fixos(como 1000 ou 100) para tentar elimitar números negativos por exemplo. 

Mais além dessas técnicas mais simples, podemos usar funções como as do Sklearn, como por exemplo, o MinMaxScaler da biblioteca Sklearn, que servem para normalizar escalas de valores nas amostras.

# Conversão de Datas e Textos
Também, podemos converter colunas que tenham valores de texto para números, por exemplo na codificação One Hot Enconding, que transforma variáveis categóricas em colunas contendo apenas zeros e uns.

Também podemos converter textos para datas, texto para números, ou números para texto, etc. Por exemplo, podemos converter o número do mês para o nome do mês. 

## Remover Outliers(valores extremos)
Na etapa anterior de análise exploratória, eu expliquei formas de identificar Outliers. Com isso, sabendo onde estão esses Outliers, podemos apagar eles do nosso dataset usando funções como o `drop` do pandas. É assim que se trata Outliers.

## Tratar valores NaN(valores faltando)
Na etapa anterior de análise exploratória, eu expliquei formas de identificar valores NaN. Com isso, sabendo quais são as colunas que tem valores faltando, podemos tratar elas substituindo esses valores faltantes por alguma coisa. Por exemplo, se em uma determinada coluna temos 200 números, e um deles é NaN(está faltando), podemos tirar a média dessa coluna, e substituir esses valores NaN pela média da própia coluna.

Também poderiamos substituir esses valores por um valor fixo, como por exemplo zero ou um.

Também poderiamos apagar essas amostras, se isso não foi afetar o dataset.

Também poderiamos usar regressão linear na coluna, para tentar estimar o valor que a coluna deveria ter.

Essas são algumas formas mais conhecidas de se tratar valores NaN. Cada um escolhe o que acha melhor.








