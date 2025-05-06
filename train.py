# train.py

import pandas as pd
import numpy as np
import mlflow
import mlflow.sklearn
import joblib
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from hash_utils import guardar_hash  # ✅ Para verificar integridad

# Configura el tracking local de MLflow
mlflow.set_tracking_uri("file:./mlruns")
mlflow.set_experiment("MLSecOps")

def train_and_log():
    # Cargar dataset
    data = load_breast_cancer()
    X = pd.DataFrame(data.data, columns=data.feature_names)
    y = pd.Series(data.target)

    # Dividir en train/test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Entrenar modelo
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluar
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)

    print("Accuracy:", acc)
    print("Classification Report:\n", classification_report(y_test, preds))

    # Iniciar MLflow run
    with mlflow.start_run() as run:
        mlflow.log_param("n_estimators", 100)
        mlflow.log_metric("accuracy", acc)

        # Guardar modelo con MLflow
        mlflow.sklearn.log_model(model, "random_forest_model")
        print("Modelo registrado con MLflow.")

    # Guardar modelo como .pkl localmente
    joblib.dump(model, "modelo_guardado.pkl")

    # Guardar hash del modelo
    guardar_hash("modelo_guardado.pkl")

if __name__ == "__main__":
    train_and_log()
