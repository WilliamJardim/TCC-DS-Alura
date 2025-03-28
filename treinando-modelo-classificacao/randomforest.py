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