import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression

# Carregar os dados
df = pd.read_csv('./datasets/dataset-tratado-normalizado-sem-outliers.csv', sep=';');

# Separar variáveis explicativas e alvo
X = df.drop(columns=['Data', 'Custo_Cultivo', 'Tempo_Crescimento_horas'])
y = df['Custo_Cultivo']

# Transformações para colunas categóricas e numéricas
categorical_features = ['Estacao_Ano', 'Tipo_Planta']
numeric_features = ['Chuva_mm', 'Num_Praga']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ]
)

# Criar pipeline com regressão linear
model = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

# Separar treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Treinar o modelo
model.fit(X_train, y_train)

# Avaliação
score = model.score(X_test, y_test)
print(f'R² do modelo: {score:.4f}')

print(model.predict(X_test))
