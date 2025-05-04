import random
from collections import Counter

# Corpus de ejemplo (puedes sustituirlo por un corpus real)
corpus = "el gato duerme en la cama el perro juega en el jardín el gato juega en el jardín".split()

# Contar las ocurrencias de cada palabra
def crear_modelo_probabilistico(corpus):
    total_palabras = len(corpus)
    conteo_palabras = Counter(corpus)
    
    # Calcular la probabilidad de cada palabra
    probabilidades = {palabra: conteo / total_palabras for palabra, conteo in conteo_palabras.items()}
    
    return probabilidades

# Crear el modelo probabilístico
modelo = crear_modelo_probabilistico(corpus)

# Mostrar el modelo probabilístico
print("Modelo Probabilístico del Lenguaje:")
for palabra, probabilidad in modelo.items():
    print(f"{palabra}: {probabilidad:.4f}")
