import pandas as pd
import numpy as np

# Definição das classes e valores médios
plantas = ["Soja", "Trigo", "Batata", "Tomate"]
altura_media = [80, 100, 60, 120]  # cm
largura_folha_media = [7, 5, 10, 8]  # cm
petalas_media = [5, 3, 0, 5]  # Algumas plantas não têm pétalas
crescimento_media = [1.5, 2.0, 1.0, 2.5]  # cm/dia

# Criando amostras aleatórias variando em torno da média
np.random.seed(42)  # Para reprodutibilidade
dados = []

for i in range(150):  # 150 amostras por planta
    for j, planta in enumerate(plantas):
        dados.append([
            planta,
            np.random.normal(altura_media[j], 5),  # ±5 cm de variação
            np.random.normal(largura_folha_media[j], 1),
            max(0, int(np.random.normal(petalas_media[j], 1))),  # Pétalas não podem ser negativas
            np.random.normal(crescimento_media[j], 0.3)  # ±0.3 cm/dia de variação
        ])

# Criando DataFrame
df = pd.DataFrame(dados, columns=["Tipo_Planta", "Altura_cm", "Largura_Folha_cm", "Num_Petalas", "Crescimento_cm_dia"])

# Salvando como CSV
df.to_csv("datasets/tipos_plantas.csv", sep=';', index=False)

# Exibir as primeiras linhas
print(df.head())
