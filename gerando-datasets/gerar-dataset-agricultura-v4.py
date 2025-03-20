"""
Código python parar gerar o dataset

Author: William Alves Jardim

Descrição da ideia que tive para melhorar a v3:

Melhorar ele da seguinte forma:

As variáveis climáticas (temperatura, chuva, sol) devem seguir um padrão sazonal explícito, o que tornaria os dados mais realistas. Precisa ter uma variação clara ao longo do ano. A temperatura no inverno deveria ser mais baixa, e no verão mais alta.

Além disso, fazer as seguintes melhorias no tempo de crescimento:
Temperatura afeta o crescimento de forma específica
Nem todas as plantas crescem melhor em temperaturas altas. Algumas, como o trigo, preferem temperaturas mais amenas.

Horas de sol afetam a fotossíntese e crescimento
Mais horas de sol aceleram o crescimento de plantas que precisam de muita luz.
No inverno, há menos luz disponível, o que pode reduzir o crescimento.

Chuvas e umidade impactam o crescimento
Muita chuva pode prejudicar plantas que preferem solos secos (ex: cenoura).
Pouca chuva pode afetar culturas que precisam de solo úmido (ex: soja, arroz).

Fatores combinados para um modelo mais realista
Agora podemos juntar tudo! O tempo de crescimento final deve considerar temperatura, luz e chuva ao mesmo tempo:

Fiz as mudanças como adições com os novos fatores sendo multiplicativos, sem remover nada que já tinha antes
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
df['Num_Praga'] = np.random.randint(0, 50, n_samples) * df['Ervas_Daninhas']
df.loc[df['Nivel_Pesticida'] > 3, ['Ervas_Daninhas', 'Num_Praga']] *= 0.5
df.loc[df['Estacao_Ano'] == 'Verão', ['Ervas_Daninhas', 'Num_Praga']] *= 1.5

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
    np.random.uniform(500, 3000, n_samples) + noise(50) -
    df['Horas_Sol_Dia'] * 10 + df['Chuva_mm'] * 3 + df['Num_Praga'] * 5 +
    df['Tipo_Planta'].factorize()[0] * 100 - df['Humidade_Solo'] * 5 - df['Ervas_Daninhas'] * 20 +
    df.apply(growth_adjustment, axis=1)
)

# Consumo de água por semana baseado no tipo de planta
df['Litros_Agua_Semana'] = (
    np.random.uniform(5, 50, n_samples) + noise(3) + df['Humidade_Solo'] * 0.3 - df['Num_Praga'] * 0.2 +
    df['Tipo_Planta'].factorize()[0] * 2
)

# Custo de cultivo afetado por umidade, ervas daninhas, pragas, tipo de solo e água
df['Custo_Cultivo'] = (
    np.random.uniform(50, 500, n_samples) + noise(20) +
    df['Tipo_Solo'].map({'Arenoso': 30, 'Argiloso': 50, 'Siltoso': 40, 'Humoso': 60}) +
    df['Num_Praga'] * 2 + df['Ervas_Daninhas'] * 15 + df['Humidade_Solo'] * 0.5 + df['Litros_Agua_Semana'] * 0.3
)

# Preço de venda baseado no custo e qualidade
df['Preco_Venda'] = (
    df['Custo_Cultivo'] * np.random.uniform(1.5, 3.0, n_samples) +
    df['Indice_Crescimento'] * 20 + noise(50) - df['Num_Praga'] * 1.5
)

# Saúde baseada na umidade, temperatura, poda, pragas e ervas daninhas
df['Saude'] = np.where(
    (df['Humidade_Solo'] > 30) & (df['Temperatura_C'] < 35) & (df['Frequencia_Podas'] > 2) & (df['Num_Praga'] < 10) & (df['Ervas_Daninhas'] == 0),
    'Saudável', 'Doente'
)

# Tempo de vida atualizado levando em conta mais fatores
df['Tempo_Vida_dias'] = (
    np.where(df['Saude'] == 'Saudável', np.random.uniform(100, 365, n_samples), np.random.uniform(30, 150, n_samples))
    + noise(10)
    + df['Resistencia_Clima'] * 2
    - df['Num_Praga'] * 0.8
    - df['Ervas_Daninhas'] * 10
    + (df['Nivel_Pesticida'] * -5 + df['Nivel_Pesticida'] ** 2)  # Pouco pesticida ajuda, muito prejudica
    + df['Frequencia_Podas'] * 3  # Podas moderadas aumentam a vida
    - np.abs(df['Humidade_Solo'] - 40) * 0.3  # Umidade ideal = 40
    - np.abs(df['Temperatura_C'] - 25) * 0.5  # Temperatura ideal = 25
)

# Introduzir valores nulos
df.loc[random.sample(range(n_samples), k=25), 'Humidade_Solo'] = np.nan
df.loc[random.sample(range(n_samples), k=10), 'Custo_Cultivo'] = np.nan

# Salvar CSV
df.to_csv('csv/dataset-agricultura-v4.csv', index=False, sep=';')
print("Dataset atualizado com sucesso!")