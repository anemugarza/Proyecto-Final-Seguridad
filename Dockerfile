FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY train.py .
COPY hash_utils.py .
COPY verificar_modelo.py .
COPY modelo_guardado.pkl .
COPY hash_original.txt .
COPY mlruns/ ./mlruns/

CMD ["python", "verificar_modelo.py"]
