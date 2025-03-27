# Datasets que criei
Para fazer esse trabalho de conclusão de meu curso, eu decici criar meus própios datasets.
Criei um script em python que gera esses datasets, de uma forma realista e prática, usando o pandas e o numpy.

# Pastas
A pasta `csv/` contém os arquivos CSV desses meus datasets gerados pelo script python.
Se quiser ver como eles foram construidos, veja os scripts: `gerar-dataset-agricultura-v1.py`, `gerar-dataset-agricultura-v2.py`, `gerar-dataset-agricultura-v3.py`, `gerar-dataset-agricultura-v4.py` e `gerar-dataset-agricultura-v5.py`

# Versões
A versão `v5` é a mais completa. 

# Balançeamento que fiz
As vezes, nosso dataset pode ter muito mais amostras de uma determinada categoria do que de outras classes. Por exemplo, no dataset `dataset-agricultura-v4.csv` a quantidade de plantas doentes e muito maior do que a de plantas saudáveis. Então pra resolver isso, tive que remover algumas plantas, para igualar as duas classes. Isso vai ser muito importante quando eu for treinar um modelo.

**NOTA: Eu melhorei o dataset, e o atual agora é o v5, mais o conceito explicado aqui funciona para qualquer dataset**

