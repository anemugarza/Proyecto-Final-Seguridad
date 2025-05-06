# manipular_modelo.py
import joblib
import numpy as np
from sklearn.dummy import DummyClassifier

# Crear un modelo totalmente aleatorio
modelo_malo = DummyClassifier(strategy="uniform", random_state=99)

# Entrenar con datos falsos 
X_falso = np.random.rand(10, 30)  # 10 muestras, 30 features
y_falso = np.random.choice(['BENIGNO', 'MALIGNO'], size=10)

modelo_malo.fit(X_falso, y_falso)

# Sobreescribir el modelo legítimo
joblib.dump(modelo_malo, "modelo_guardado.pkl")

print("Modelo manipulado: modelo aleatorio guardado como modelo_guardado.pkl")
