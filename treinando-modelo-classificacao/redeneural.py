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
