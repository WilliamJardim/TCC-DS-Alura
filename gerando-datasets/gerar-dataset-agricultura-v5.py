"""
Código python parar gerar o dataset

Author: William Alves Jardim

Descrição da ideia que tive para melhorar a v4:

  - Reduzir os ruidos para melhorar as correlações

  - Aumentei o impacto das features

  - Melhorei o realismo

"""

import pandas as pd 
import numpy as np
import random
from datetime import datetime, timedelta

# Definir parâmetros do dataset
n_samples = 3000  # Número de amostras
plant_types = ['Milho', 'Trigo', 'Soja', 'Tomate', 'Batata', 'Cenoura']
soil_types = ['Arenoso', 'Argiloso', 'Siltoso', 'Humoso']
seasons = ['Primavera', 'Verão', 'Outono', 'Inverno']
health_status = ['Saudável', 'Doente']

# Gerar datas sazonais
start_date = datetime(2020, 1, 1)
dates = [start_date + timedelta(days=i) for i in range(n_samples)]
season_map = {0: 'Inverno', 1: 'Primavera', 2: 'Verão', 3: 'Outono'}
seasons_series = [season_map[(date.month % 12) // 3] for date in dates]

# Definir padrões sazonais para variáveis climáticas
def seasonal_variation(season, base, variation):
    adjustments = {'Inverno': -variation, 'Primavera': -variation/2, 'Verão': variation, 'Outono': variation/2}
    return base + adjustments.get(season, 0)

# Função para gerar ruído
noise = lambda scale: np.random.normal(0, scale)

# Criar DataFrame
np.random.seed(42)
df = pd.DataFrame({
    'Data': dates,
    'Estacao_Ano': seasons_series,
    'Tipo_Planta': np.random.choice(plant_types, n_samples),
    'Tipo_Solo': np.random.choice(soil_types, n_samples)
})

# Aplicar padrões sazonais às variáveis climáticas
df['Temperatura_C'] = [seasonal_variation(s, np.random.uniform(10, 40), 10) for s in df['Estacao_Ano']]
df['Chuva_mm'] = [seasonal_variation(s, np.random.uniform(0, 200), 50) for s in df['Estacao_Ano']]
df['Horas_Sol_Dia'] = [seasonal_variation(s, np.random.uniform(4, 12), 2) for s in df['Estacao_Ano']]
df['Humidade_Solo'] = np.random.uniform(10, 80, n_samples) + np.random.normal(0, 3)
df['Frequencia_Podas'] = np.random.randint(0, 10, n_samples)
df['Nivel_Pesticida'] = np.random.uniform(0, 5, n_samples) + np.random.normal(0, 0.2)

# Características únicas da planta para classificação multiclasse
df['Cor_Folha'] = np.random.uniform(0, 25, n_samples) + df['Tipo_Planta'].factorize()[0] * 7 + noise(3)
df['Densidade_Fibra'] = np.random.uniform(0.5, 3.5, n_samples) + df['Tipo_Planta'].factorize()[0] * 0.2 + noise(0.2)
df['Tamanho_Raiz_cm'] = np.random.uniform(5, 50, n_samples) + df['Tipo_Planta'].factorize()[0] * 2 + noise(2)
df['Indice_Crescimento'] = np.random.uniform(0.1, 1.5, n_samples) + df['Tipo_Planta'].factorize()[0] * 0.05 + noise(0.1)
df['Resistencia_Clima'] = np.random.uniform(0, 10, n_samples) + df['Tipo_Planta'].factorize()[0] * 0.5 + noise(0.5)

# Presença de ervas daninhas e pragas influenciadas pela estação e pesticida
df['Ervas_Daninhas'] = np.random.choice([0, 1], n_samples, p=[0.7, 0.3])
# Nao vai ter negativo
df['Ervas_Daninhas'] = df['Ervas_Daninhas'].abs();


df['Num_Praga'] = np.random.randint(0, 50, n_samples) * df['Ervas_Daninhas']
# Nao vai ter negativo
df['Num_Praga'] = df['Num_Praga'].abs();



df.loc[df['Nivel_Pesticida'] > 3, ['Ervas_Daninhas', 'Num_Praga']] *= 0.5
df.loc[df['Estacao_Ano'] == 'Verão', ['Ervas_Daninhas', 'Num_Praga']] *= 1.5

# Aplicando padrões

def condicao_crescimento_inverno(row):
    impacto = 0;

    if row['Estacao_Ano'] == 'Inverno':
        impacto = 160;
    
    if row['Estacao_Ano'] == 'Outono':
        impacto = 9;

    return impacto;

# No inverno e outono, tem menas horas sol
df['Horas_Sol_Dia'] = df['Horas_Sol_Dia'] - (df.apply(condicao_crescimento_inverno, axis=1))

# No inverno e outono, tem menas humidade
df['Humidade_Solo'] = df['Humidade_Solo'] - (df.apply(condicao_crescimento_inverno, axis=1) * 0.2)

# No interno e outono, tem menas chuvas
df['Chuva_mm'] = df['Chuva_mm'] - (df.apply(condicao_crescimento_inverno, axis=1) * 0.5)
# No inverno e outono a temperatura é muito menor
df['Temperatura_C'] = df['Temperatura_C'] - df.apply(condicao_crescimento_inverno, axis=1)
# No inverno e outono a ressistencia ao clima é menor
df['Resistencia_Clima'] = df['Resistencia_Clima'] - df.apply(condicao_crescimento_inverno, axis=1)
# No inverno e outono a frequencia de podas é menor
df['Frequencia_Podas'] = df['Frequencia_Podas'] - (df.apply(condicao_crescimento_inverno, axis=1) * 0.5 )
# No inverno e outono o nivel de pesticida é menor
df['Nivel_Pesticida'] = df['Nivel_Pesticida'] - (df.apply(condicao_crescimento_inverno, axis=1) * 0.5)
# No inverno e outono tem menas pragas e hervas daninhas
df['Num_Praga'] = df['Num_Praga'] - (df.apply(condicao_crescimento_inverno, axis=1) * 0.5)
df['Ervas_Daninhas'] = df['Ervas_Daninhas'] - (df.apply(condicao_crescimento_inverno, axis=1) * 0.5)

# Nao deixa ter pagas nem ervas daninhas menores do que zero
def naoPodeTerPragasMenorQueZero(row):
    if row['Num_Praga'] < 0:
        return 0;

    else:
        return row['Num_Praga']

df['Num_Praga'] = df.apply(naoPodeTerPragasMenorQueZero, axis=1)



def naoPodeTerErvasDaninhasMenorQueZero(row):
    if row['Ervas_Daninhas'] < 0:
        return 0;

    else:
        return row['Ervas_Daninhas']

df['Ervas_Daninhas'] = df.apply(naoPodeTerErvasDaninhasMenorQueZero, axis=1)




# Altura da planta depende do tipo, solo e ambiente
df['Altura_cm'] = (
    # valor aleatorio
    np.random.uniform(10, 100, n_samples) 

    # ruidos aleatorios
    + noise(2) 

    # a altura tambem depende do tipo da planta
    + df['Tipo_Planta'].map({'Milho': 98, 'Trigo': 10, 'Soja': 35, 'Tomate': 12, 'Batata': 48, 'Cenoura': 22}) * 150 

    # a altura pode ser maior com boa humidade 
    + (df['Humidade_Solo'] * 2500)
    
    # pode ser reduzida pela má temperatura
    - (df['Temperatura_C'] * 40)

    # vai depender das horas do sol
    + (df['Horas_Sol_Dia'] * 180)

    # A chuva melhora a altura tambem
    + (df['Chuva_mm'] * 2500)  
    
    # vai ser afetado pelo numero de pragas
    - (df['Num_Praga'] * 9900)

    # vai ser afetado com ervas daninhas
    - (df['Ervas_Daninhas'] * 9900)
)

# Ajustes no tempo de crescimento baseado em fatores ambientais
def growth_adjustment(row):
    ajuste = 0
    if row['Tipo_Planta'] == 'Trigo':
        ajuste += -abs(row['Temperatura_C'] - 20) * 5  # Trigo cresce melhor em temperaturas amenas
    if row['Tipo_Planta'] in ['Milho', 'Tomate']:
        ajuste += row['Horas_Sol_Dia'] * 10  # Essas plantas se beneficiam de mais sol
    if row['Tipo_Planta'] == 'Cenoura':
        ajuste += -row['Chuva_mm'] * 2  # Cenoura prefere solo mais seco
    if row['Tipo_Planta'] in ['Soja', 'Arroz']:
        ajuste += row['Chuva_mm'] * 1.5  # Soja e arroz precisam de mais umidade
    return ajuste

# Tempo de crescimento afetado por estação, tipo de planta, ervas daninhas, solo e umidade
df['Tempo_Crescimento_horas'] = (
    #O valor é aleatorio
    #np.random.uniform(6800, 10600, n_samples) 
    889600

    # Existe um ruido aleatorio tambem
    + noise(5)
    
    #O tempo de crescimento diminui com horas do sol e chuva
    -(df['Horas_Sol_Dia'] * 2900) 
    -(df['Chuva_mm'] * 1800)

    # O tempo aumenta com pragas
    + (df['Num_Praga'] * 30500)

    # o tempo tambem depende do tipo da planta
    + df['Tipo_Planta'].map({'Milho': 98, 'Trigo': 10, 'Soja': 35, 'Tomate': 12, 'Batata': 48, 'Cenoura': 22}) * 150 

    # o tempo diminui com um solo bem irrigado
    - (df['Humidade_Solo'] * 3000)
    
    # O tempo aumenta com ervas daninhas
    + (df['Ervas_Daninhas'] * 38000)
    
    # o tempo tambem depende do tipo da planta
    + df.apply(growth_adjustment, axis=1)
)

# Consumo de água por semana baseado no tipo de planta
df['Litros_Agua_Semana'] = (
    # um valor aleatorio
    #np.random.uniform(3500, 7000, n_samples) 
    985500

    # tem um ruido aleatorio
    + noise(8) 
    
    # a planta consome menos agua se o solo for bem irrigado
    - (df['Humidade_Solo'] * 2900)

    # a planta consome menos agua se tiver bastante chuva
    - (df['Chuva_mm'] * 1800)

    # Podas moderadas aumentam a reduzir um pouco o uso da agua
    - (df['Frequencia_Podas'] * 5)  

    # Quanto mais tempo a planta levou pra crescer, mais agua ela consome
    - (df['Tempo_Crescimento_horas'] * 0.05)
    
    # a planta perde agua com pragas(que consomem a agua dela)
    + (df['Num_Praga'] * 10900)

    # A planta perde agua com ervas daninhas
    + (df['Ervas_Daninhas'] * 10900)

    # O tipo de planta pode consumir mais agua que outras
    + df['Tipo_Planta'].map({'Milho': 45, 'Trigo': 35, 'Soja': 38, 'Tomate': 60, 'Batata': 50, 'Cenoura': 22}) * 6

    # a resistencia ao clima ajuda
    - (df['Resistencia_Clima'] * 15)
)



# Saúde baseada na umidade, temperatura, poda, pragas e ervas daninhas
def calcular_saude(row):
    score = 100  # Começamos com uma pontuação de saúde máxima
    
    # Impacto das condições ambientais
    score -= abs(row['Temperatura_C'] - 25) * 2  # Temperaturas extremas reduzem a saúde
    score -= abs(row['Humidade_Solo'] - 50) * 1.5  # Solo muito seco ou muito úmido prejudica
    score += row['Horas_Sol_Dia'] * 2  # Mais sol, em geral, melhora a saúde
    score -= row['Chuva_mm'] * 0.5  # Excesso de chuva pode ser prejudicial
    
    # Impacto de pragas e ervas daninhas
    score -= row['Num_Praga'] * 10  # Muitas pragas reduzem a saúde
    score -= row['Ervas_Daninhas'] * 10  # Presença de ervas daninhas reduz a saúde
    
    # Impacto do manejo agrícola
    score += row['Nivel_Pesticida'] * 8  # Pesticidas ajudam a reduzir impacto de pragas
    score += row['Frequencia_Podas'] * 10  # Podas melhoram a saúde
    
    # Ajuste baseado no tipo de planta (sensibilidade às condições)
    if row['Tipo_Planta'] in ['Milho', 'Tomate']:
        score += row['Horas_Sol_Dia'] * 2  # Essas plantas gostam de mais sol

    if row['Tipo_Planta'] == 'Cenoura':
        score -= row['Chuva_mm'] * 1.2  # Cenouras não lidam bem com excesso de chuva

    if row['Tipo_Planta'] in ['Soja', 'Arroz']:
        score += row['Humidade_Solo'] * 1.2  # Solo úmido beneficia essas plantas
    
    # Garantir que a pontuação de saúde fique dentro dos limites
    score = max(0, min(100, score))
    
    return 'Saudável' if score >= 50 else 'Doente'

# Aplicar a função ao dataset
df['Saude'] = df.apply(calcular_saude, axis=1)




# a alta temperatura pode aumentar o custo do cultivo
def ajuste_custo_temperatura(row):
    ajuste = 0
    if row['Temperatura_C'] < 0:
        ajuste + abs(row['Temperatura_C']) * 50

    else:
        ajuste + row['Temperatura_C'] * 10

    return ajuste

# Se a planta for doente, o custo de cultivo vai ser bem maior
def ajuste_custo_doentes(row):
    ajuste = 0
    if row['Saude'] == 'Doente':
        ajuste + 6000;

    else:
        #planta saudavel é mais facil de cuidar
        ajuste - 0;

    return ajuste

# Custo de cultivo afetado por umidade, ervas daninhas, pragas, tipo de solo e água
df['Custo_Cultivo'] = (
    # um valor aleatorio
    #np.random.uniform(50, 500, n_samples) 
    68829000

    # com um ruido aleatorio
    + noise(8) 

    # A quantidade de agua gasta também pode aumentar o custo do cultimo
    + df['Litros_Agua_Semana'] * 200

    # a chuva pode reduzir um pouco o custo do cultivo
    - (df['Chuva_mm'] * 699800)

    # A boa humidade do solo pode rezudir um pouco o custo do cultivo
    - (df['Humidade_Solo'] * 1800)

    # Podas moderadas aumentam a reduzir um pouco o custo
    - (df['Frequencia_Podas'] * 8)  

    # Quanto mais tempo a planta levou pra crescer, maior o custo de cultivo
    - (df['Tempo_Crescimento_horas'] * 0.05)
    
    # O tipo do solo pode fazer com que o custo de cultivo seja mais caro
    + df['Tipo_Solo'].map({'Arenoso': 30, 'Argiloso': 50, 'Siltoso': 40, 'Humoso': 60}) * 2.5 

    # o numero de pragas, hervas daninhas tambem pode fazer com que o custo de cultivo seja mais caro
    + (df['Num_Praga'] * 2985900)
    + (df['Ervas_Daninhas'] * 29885900) 

    # a alta temperatura pode aumentar o custo do cultivo
    + df.apply(ajuste_custo_temperatura, axis=1)

    # Se a planta for doente, o custo de cultivo vai ser bem maior
    + df.apply(ajuste_custo_doentes, axis=1)

    # a resistencia ao clima ajuda
    - (df['Resistencia_Clima'] * 15)
)

# Preço de venda baseado no custo e qualidade
df['Preco_Venda'] = (
    # valor base
    10

    # mais um ruido aleatorio
    + noise(8)

    # o custo do cultimo mais um lucro em cima
    + (df['Custo_Cultivo'] * np.random.uniform(100.5, 500.0, n_samples) )

    # mais a qualidade
    + (df['Indice_Crescimento'] * 20)  
    
    # porém, o numero de pragas afeta o preço da venda
    - (df['Num_Praga'] * 300)
)



# Tempo de vida atualizado levando em conta mais fatores
df['Tempo_Vida_dias'] = (
    # o tempo de vida varia se a planta é saudavel ou não
    #(np.where(df['Saude'] == 'Saudável', np.random.uniform(585, 1065, n_samples), np.random.uniform(150, 300, n_samples)) + 300),
    2955000 + 
    + (np.where(df['Saude'] == 'Saudável', np.random.uniform(100, 200, n_samples), np.random.uniform(15, 50, n_samples)))

    + noise(8)
    
    + (df['Resistencia_Clima'] * 4000)

    # o numero de pragas afeta o tempo de vida
    - (df['Num_Praga'] * 90900)

    # o numero de hervas daninhas afeta o tempo de vida
    - (df['Ervas_Daninhas'] * 90900)

    # Quanto mais tempo a planta levou pra crescer, menor o tempo de vida dela, POIS DEMORARIA MUITO PARA SE DESENVOLVER
    - (df['Tempo_Crescimento_horas'] * 0.08)

    # usar pesticidade é bom, mais não em excesso
    + (df['Nivel_Pesticida'] * -5 + df['Nivel_Pesticida'] ** 2)  # Pouco pesticida ajuda, muito prejudica

    # Podas moderadas aumentam a vida
    + (df['Frequencia_Podas'] * 110)  

    # Umidade ideal = 40
    - (np.abs(df['Humidade_Solo'] - 40) * 1000)  

    # Temperatura ideal = 25
    - (np.abs(df['Temperatura_C'] - 25) * 300)  

    # A chuva melhora a vida tambem
    + (df['Chuva_mm'] * 9900)  

    # vai depender das horas do sol
    + (df['Horas_Sol_Dia'] * 4000)
)

# Introduzir valores nulos
df.loc[random.sample(range(n_samples), k=25), 'Humidade_Solo'] = np.nan
df.loc[random.sample(range(n_samples), k=10), 'Custo_Cultivo'] = np.nan

# Introduzir outliers
df.loc[random.sample(range(n_samples), k=20), 'Preco_Venda'] *= 5  # Aumenta muito o preço
df.loc[random.sample(range(n_samples), k=15), 'Altura_cm'] *= 0.1  # Plantas muito pequenas


# Tratar outras coisas

# CUSTO DE CULTIVO DAS PLANTAS DOENTES VAI SER MAIOR
def custoMaiorPraPlantasDoentes(row):
    if row['Saude'] == 'Doente':
        return 99900000
    else:
        return -9950000

df['Custo_Cultivo'] = df['Custo_Cultivo'] + df.apply(custoMaiorPraPlantasDoentes, axis=1)



# Salvar CSV
df.to_csv('csv/dataset-agricultura-v5.csv', index=False, sep=';')
print("Dataset atualizado com sucesso!")