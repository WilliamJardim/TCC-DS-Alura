# Tópico anterior:
[Tópico anterior: Meu Dataset de Tipo das plantas](../criando-dataset-multiclasse/)

# Treinando um modelo de Machine Learning para fazer classificação dos tipos de plantas do meu outro dataset

## Treinamento de modelos de classificação usando a biblioteca Sklearn do python
Nas etapas anteriores, eu criei um outro dataset diferente do primeiro, e agora vou treinar dois modelos de classificação para classificar qual é o tipo da planta pelas suas caracteristicas.

## RandomForest
```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('../criando-dataset-multiclasse/datasets/tipos_plantas.csv', sep=';')

print(df)

# Convertendo rótulos para números
encoder = LabelEncoder()
df["Tipo_Planta"] = encoder.fit_transform(df["Tipo_Planta"])

# Separando features e labels
X = df.drop(columns=["Tipo_Planta"])
y = df["Tipo_Planta"]

# Separando treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.6, random_state=42)

# Treinando modelo
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Testando modelo
y_pred = model.predict(X_test)

# Calculando a Acurácia do modelo RandomForest
from sklearn.metrics import accuracy_score
print("Acurácia:", accuracy_score(y_test, y_pred))

# Usando várias métricas do Sklearn
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))
```

O modelo RandomForest acertou com precisão de 0.9888888888888889. Foi muito bom.

## Redes Neurais MLP
```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neural_network import MLPClassifier

# Carregar o dataset
df = pd.read_csv('../criando-dataset-multiclasse/datasets/tipos_plantas.csv', sep=';')

# Separar recursos (X) e rótulos (y)
X = df.drop(columns=['Tipo_Planta'])  # Remover a coluna com os tipos de planta
y = df['Tipo_Planta']

# Converter rótulos de texto para números (Ex: "Soja" → 0, "Trigo" → 1, etc.)
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Padronizar os dados (Esse tipo de modelo é sensível a escalas)
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Dividir os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.6, stratify=y, random_state=42)

# Criar e treinar o modelo MLP
model = MLPClassifier(hidden_layer_sizes=(50, 30), activation='relu', solver='adam', max_iter=500, random_state=42)
model.fit(X_train, y_train)

# Fazer previsões
y_pred = model.predict(X_test)

# Avaliar o modelo
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred)
print(f'Acurácia: {accuracy:.4f}')

# Usando várias métricas do Sklearn
from sklearn.metrics import accuracy_score, classification_report
print(classification_report(y_test, y_pred, target_names=label_encoder.classes_))

```

O modelo MLP acertou com precisão de 0.9861. Foi muito bom.

Esses são só alguns modelos de Machine Learning que o Sklearn tem. Poderiamos usar muitos outros dele ou de outras bibliotecas.

# Próximo tópico:
[Próximo tópico: Conclusão](../conclusao/)