# Como encontrar outliers
Para encontrar outliers, podemos procurar por valores extremos nas colunas das amostras.
Ou seja, valores absurdos, que não precisam estar incorretos, mais que sejam extremos, que fojem do padrão.

Voce pode usar gráficos de dispersão, ou boxplot para encontrar outliers. 
Eles vão aparecer longe do dentro do gráfico.

Voce também pode usar testes estatisticos para procurar outliers.

# Outliers que encontrei
Para esse exemplo, eu sei que os outliers estão apenas na coluna PRECO VENDA,
pois eu propositalmente criei esse dataset para ter Outliers nessa coluna para ensinar como identificar eles

Com as analises feitas, como voce pode ver no gráfico do matplotlib, existem amostras que tem o Preco_Venda muito alto!, valores extremos que fogem do padrão. E isso é um exemplo de outlier que precisa ser tratado.

Esses não são os unicos tipos que podem existir.
Podem haver outros tipos de Outliers também, mais todos eles vão ter algo em comum: Vão ser valores extremos.

Nos outros dois testes feitos com quartis e com o Z-Score, vemos que existem no mínimo de 8 a 14 outliers, na coluna Preco_Venda.
Ou seja, existem de 8 a 14 amostras que tem valores extremos na coluna Preco_Venda. E precisam ser tratados ou removidos.
