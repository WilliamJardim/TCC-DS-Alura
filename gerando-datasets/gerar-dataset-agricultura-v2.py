"""
Código python parar gerar o dataset

Author: William Alves Jardim

Descrição da ideia que tive para melhorar a v1:
Adicionar novas features numéricas, com relações baseadas em outras features, e que afetam a saude, o tempo de vida, e o tempo de crescimento, e consequentemente todas elas impactam de forma realista no custo de cultivo e no preço de venda. 
Ou seja o custo de cultivo é influenciado pela saude da planta tambem. Features adicionar: as que voce achar relevante, e também as que eu disse a seguir: se tem presença de herva daninhas, se tem pragas que prejudicam a planta e quantas são. 
Também, a presença de hervas daninhas pode ser algo sacional ou/e também relacionado ao tipo de solo, cuidados que o dono tem, etc.... 

Adicionar características numéricas e categóricas, pelo menos umas 5, que identificam unicamente o tipo da planta. Pra dar pra fazer classificação Multiclasse. Mais com algumas variações aleatórias nesses características pra ficar realista, pra dar entender que as características podem virar um pouco como acontece na vida real 
Adicionar que tempo de crescimento e o consumo de água varia de acordo com o tipo da planta, Mais com algumas variações aleatórias nesses características pra ficar realista, pra dar entender que as características podem virar um pouco como acontece na vida real 
Adicionar um padrão sacional que indica que, favorece certos tipos de plantas em determinadas datas, e em outras não. Um padrão perceptível. E também, determinadas épocas influenciam na presença de pragas e hervas daninhas 

OUTROS AJUSTES:

Adicionamente o nível de pesticida vai impactar nas pregas e hervas daninhas(o que consequentemente vai impactar outras features, naturalmente)
Os litros de água adicionamente também vai ser afetado pelo tipo da planta(como mencionei no começo desse prompt)
O tempo de crescimento adicionamente também deve ser afetado pelas hervas daninhas, o tipo do solo, e humidade. Além disso, também vai ser afetado pelo tipo da planta(como mencionei no começo desse prompt)
O custo de cultivo adicionamente também vai ser afetado pela humidade, e litros de água.

"""

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Definir parâmetros do dataset
n_samples = 3000  # Número de amostras
plant_types = ['Milho', 'Trigo', 'Soja', 'Tomate', 'Batata', 'Cenoura']
soil_types = ['Arenoso', 'Argiloso', 'Siltoso', 'Humoso']
health_status = ['Saudável', 'Doente']

# Gerar datas sazonais
start_date = datetime(2020, 1, 1)
dates = [start_date + timedelta(days=i) for i in range(n_samples)]

# Função para gerar ruído
noise = lambda scale: np.random.normal(0, scale)

# Criar DataFrame com relações entre features
df = pd.DataFrame({
    'Data': dates,
    'Tipo_Planta': np.random.choice(plant_types, n_samples),
    'Tipo_Solo': np.random.choice(soil_types, n_samples),
    'Humidade_Solo': np.random.uniform(10, 80, n_samples) + noise(3),
    'Temperatura_C': np.random.uniform(10, 40, n_samples) + noise(1),
    'Chuva_mm': np.random.uniform(0, 200, n_samples) + noise(5),
    'Horas_Sol_Dia': np.random.uniform(4, 12, n_samples) + noise(1),
    'Frequencia_Podas': np.random.randint(0, 10, n_samples),
})

# Presença de ervas daninhas e pragas
df['Ervas_Daninhas'] = np.random.choice([0, 1], n_samples, p=[0.7, 0.3])
df['Num_Praga'] = np.random.randint(0, 50, n_samples) * df['Ervas_Daninhas']

# Impacto do tipo de solo nas ervas daninhas
df.loc[df['Tipo_Solo'] == 'Humoso', 'Ervas_Daninhas'] = np.random.choice([0, 1], df[df['Tipo_Solo'] == 'Humoso'].shape[0], p=[0.5, 0.5])

# Altura da planta depende do tipo, solo e ambiente
df['Altura_cm'] = (
    np.random.uniform(10, 300, n_samples) + noise(10) +
    df['Humidade_Solo'] * 0.5 - df['Temperatura_C'] * 1.2 +
    df['Horas_Sol_Dia'] * 2.5 - df['Num_Praga'] * 0.5
)

# Tempo de crescimento relacionado a condições ambientais e pragas
df['Tempo_Crescimento_horas'] = (
    np.random.uniform(500, 3000, n_samples) + noise(50) -
    df['Horas_Sol_Dia'] * 10 + df['Chuva_mm'] * 3 + df['Num_Praga'] * 5
)

# Custo de cultivo depende da planta, solo, pragas e ervas daninhas
df['Custo_Cultivo'] = (
    np.random.uniform(50, 500, n_samples) + noise(20) +
    (df['Tipo_Solo'].map({'Arenoso': 30, 'Argiloso': 50, 'Siltoso': 40, 'Humoso': 60})) +
    df['Num_Praga'] * 2 + df['Ervas_Daninhas'] * 15
)

# Preço de venda baseado no custo e qualidade
df['Preco_Venda'] = (
    df['Custo_Cultivo'] * np.random.uniform(1.5, 3.0, n_samples) +
    df['Altura_cm'] * 0.3 + noise(50) - df['Num_Praga'] * 1.5
)

# Saúde baseada na umidade, temperatura, poda, pragas e ervas daninhas
df['Saude'] = np.where(
    (df['Humidade_Solo'] > 30) & (df['Temperatura_C'] < 35) & (df['Frequencia_Podas'] > 2) & (df['Num_Praga'] < 10) & (df['Ervas_Daninhas'] == 0),
    'Saudável', 'Doente'
)

# Tempo de vida baseado na saúde e condições
df['Tempo_Vida_dias'] = (
    np.where(df['Saude'] == 'Saudável', np.random.uniform(100, 365, n_samples), np.random.uniform(30, 150, n_samples))
    + noise(10)
)

# Litros de água por semana baseado na umidade e planta
df['Litros_Agua_Semana'] = (
    np.random.uniform(5, 50, n_samples) + noise(3) + df['Humidade_Solo'] * 0.3 - df['Num_Praga'] * 0.2
)

# Outras features

df['Espaco_Ocupado_m2'] = np.random.uniform(1, 5, n_samples) + noise(0.5)
df['Indice_Fertilizacao'] = np.random.uniform(0, 10, n_samples) + noise(0.5)
df['Nivel_Pesticida'] = np.random.uniform(0, 5, n_samples) + noise(0.2)
df['Feature_Irrelevante1'] = np.random.uniform(0, 100, n_samples)
df['Feature_Irrelevante2'] = np.random.choice(['A', 'B', 'C', 'D'], n_samples)

# Introduzir outliers
df.loc[random.sample(range(n_samples), k=20), 'Preco_Venda'] *= 5  # Aumenta muito o preço
df.loc[random.sample(range(n_samples), k=15), 'Altura_cm'] *= 0.1  # Plantas muito pequenas

# Introduzir valores nulos
df.loc[random.sample(range(n_samples), k=25), 'Humidade_Solo'] = np.nan
df.loc[random.sample(range(n_samples), k=10), 'Custo_Cultivo'] = np.nan

df.to_csv('csv/dataset-agricultura-v2.csv', index=False, sep=';')
print("Dataset criado com sucesso!")
