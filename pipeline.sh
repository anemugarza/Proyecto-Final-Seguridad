#!/bin/bash

echo "=== INICIO DEL PIPELINE MLSecOps ==="

echo "[1/6] Ejecutando entrenamiento y registro con MLflow..."
python3 train.py

echo "[2/6] Verificando integridad del modelo..."
python3 verificar_modelo.py

echo "[3/6] Comparando versiones anteriores en MLflow..."
mlflow ui --port 5001 &
sleep 5
open http://127.0.0.1:5001
echo "   Abierta interfaz de MLflow para comparar runs."

echo "[4/6] Ejecutando prueba de comportamiento del modelo..."
python3 test_modelo.py

echo "[5/6] Construyendo imagen Docker..."
docker build -t mlsecops-model .

echo "[6/6] Ejecutando contenedor para verificar modelo..."
docker run --rm mlsecops-model

echo "Escaneando imagen con Trivy..."
trivy image mlsecops-model --severity HIGH,CRITICAL -f table -o resumen_trivy.txt

echo "Pipeline completado. Revisa resumen_trivy.txt y MLflow UI para comparar resultados."
