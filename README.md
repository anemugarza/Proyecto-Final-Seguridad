# MLSecOps – Pipeline Seguro para Modelos de Machine Learning

Este proyecto implementa un prototipo funcional de MLSecOps que entrena un modelo de machine learning, lo registra con MLflow, lo empaqueta en un contenedor Docker y lo escanea con Trivy para detectar vulnerabilidades.


## Objetivo

Mostrar cómo aplicar principios de seguridad (SecOps) al ciclo de vida de un modelo de ML en producción, detectando posibles vulnerabilidades y automatizando buenas prácticas.


## Tecnologías utilizadas

| Herramienta   | Uso                                      |
|---------------|------------------------------------------|
| Python 3.10+   | Lenguaje de programación principal       |
| Scikit-learn   | Entrenamiento de modelos de ML           |
| MLflow         | Registro y tracking del modelo           |
| Docker         | Contenerización del modelo y entorno     |
| Trivy          | Escaneo de seguridad de la imagen Docker|


## Estructura del proyecto

```
codigo/
├── train.py             # Entrenamiento y registro del modelo
├── requirements.txt     # Dependencias del proyecto
├── Dockerfile           # Imagen para contenerizar el entorno
├── README.md            # Este archivo
└── mlruns/              # Directorio generado automáticamente por MLflow
```


## Instrucciones de uso

### 1. Acceder al directorio del proyecto

```bash
cd ruta/a/tu/carpeta/codigo/
```

### 2. Crear y activar un entorno virtual (opcional pero recomendado)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar las dependencias necesarias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar el script de entrenamiento

```bash
python train.py
```

Esto entrena un modelo y lo registra automáticamente con MLflow en la carpeta `mlruns/`.


## 🐳 Docker: Contenerización del modelo

### 5. Construir la imagen Docker

```bash
docker build -t mlsecops-model .
```

### 6. Ejecutar la imagen

```bash
docker run --rm mlsecops-model
```

Este comando ejecuta el mismo entrenamiento dentro del contenedor, simulando un entorno de producción.


## Escaneo de seguridad con Trivy

### 7. Instalar Trivy (si no lo tienes)

En Mac con Homebrew:

```bash
brew install aquasecurity/trivy/trivy
```

### 8. Escanear la imagen Docker

```bash
trivy image mlsecops-model
```

Esto mostrará las vulnerabilidades encontradas (CVE, paquetes desactualizados, etc.).


## Resultado

Con este prototipo demostramos cómo implementar buenas prácticas de seguridad en el despliegue de modelos de ML:

- Entrenamiento y registro automatizado con MLflow.
- Entorno reproducible y portable con Docker.
- Escaneo de vulnerabilidades con Trivy.



