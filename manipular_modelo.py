# manipular_modelo.py

import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Cargar datos
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

# Dividir datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)  # <-- diferente semilla

# Entrenar modelo manipulado
model = RandomForestClassifier(n_estimators=100, random_state=99)
model.fit(X_train, y_train)

# Sobrescribir modelo original (simula ataque)
joblib.dump(model, "modelo_guardado.pkl")
print("🛑 Modelo manipulado guardado como modelo_guardado.pkl")
