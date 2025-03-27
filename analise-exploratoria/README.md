# Análise Explorátoria
O processo de Análise Explorátoria envolve analisar os dados do dataset, para entender os valores minimos, máximos, médias, desvio padrão, percentis,  dentre outras métricas que podemos calcular. Isso ajuda a entender os valores de cada coluna, para termos uma notação do nosso cenário que estamos explorando.

Muitas vezes, se pode observar valores extremos, e possivelmente outliers, olhando os valores minimos, máximos, onde poderiamos perceber informações que não fariam sentido, por exemplo, valores negativos em certas colunas que deveriam ser apenas positivas.

## Lendo o dataset com o pandas
```python
import pandas as pd

dataset = pd.read_csv('../criando-dataset/datasets/crescimento-soja.csv', sep=';')
```
<code>

## Descrevendo o dataset
```python
dataset.describe();
```

### Descrição do dataset dada pelo pandas:
```text
        Ano          Mes         Crescimento
count  1805.000000  1805.000000  1802.000000
mean   2022.496399     6.398892    69.758602
std       1.709052     3.286301    44.412608
min    2020.000000     1.000000    30.000000
25%    2021.000000     3.000000    40.000000
50%    2022.000000     6.000000    49.000000
75%    2024.000000     9.000000    95.000000
max    2025.000000    12.000000  1024.000000
```

Isso permite visualizar os minimos, máximos e média de cada Coluna, o que é muito util!

## Ver o tamanho do dataset
```python
dataset.shape;
```

### Descrição do tamanho do dataset dada pelo pandas:
```python
(1805, 4)
```

Ou seja, esse meu dataset tem 1805 linhas e 4 colunas.

## Vendo se tem valores negativos na coluna Crescimento
O método describe já mostrou isso. Mais quero garantir que não haja valores negativos.

```python
print( dataset[ dataset['Crescimento'] < 0 ].count()['Crescimento'].sum() )
```

### Resultado
```text
0
```

Ou seja, na coluna Crescimento não existe nenhum valor negativo. E não deveria ter mesmo!

## Vendo se tem valores NaN(valores faltando) em alguma das colunas
As vezes, as colunas podem ter valores faltando. E isso precisa ser tratado de alguma forma para não causar problemas na hora de treinar modelos de Machine Learning, ou de fazer análises.

```python
# Ver se tem valores NaN e contar quantos são, por coluna
quantidade_nan_por_coluna = dataset.isna().sum()
print(quantidade_nan_por_coluna)
```

```text
Ano            0
Mes            0
Estacao        0
Crescimento    3
dtype: int64
```

**Isso significa que na coluna Crescimento tem 3 valores NaN.**
Para tratar isso podemos usar a média da coluna, ou usar regressão linear na coluna, ou colocar tudo zero, ou mesmo remover as amostras que tem NaN.

# Vendo se tem Outliers(valores extremos no Dataset)
Isso é importante. Outliers são amostras que tem colunas com valores extremos ou absurdos, que mesmo que não estejam errados, ainda assim fogem do padrão. Por exemplo, valores muito altos, ou muito baixos que o normal. Ou seja que amostras que tem colunas com valores que fogem do padrão do dataset.

## Como verificar se tem Outliers no Dataset?
Existem duas formas de verificar a presença de Outliers:
  - Gráfico de Box Plot: Nesse gráfico de caixa, os Outliers vão aparece sempre fora da zona do gráfico

  - Testes estatísticos, como o Z-Score.

## O que fazer? E por que?
Outliers devem ser removidos, para não causar problemas na hora de treinar modelos de Machine Learning, ou de fazer análises. Pois os Outliers causam instabilidade nos modelos, distorcendo o padrão, e tambem exageram e distorcem gráficos.



