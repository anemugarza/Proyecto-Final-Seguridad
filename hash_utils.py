import hashlib

def calcular_hash(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def guardar_hash(path_modelo, archivo_hash="hash_original.txt"):
    hash_val = calcular_hash(path_modelo)
    with open(archivo_hash, "w") as f:
        f.write(hash_val)

def verificar_integridad(path_modelo, archivo_hash="hash_original.txt"):
    hash_actual = calcular_hash(path_modelo)
    with open(archivo_hash, "r") as f:
        hash_guardado = f.read().strip()
    if hash_actual == hash_guardado:
        print(" El modelo NO ha sido manipulado.")
    else:
        print(" El modelo ha sido MODIFICADO.")
