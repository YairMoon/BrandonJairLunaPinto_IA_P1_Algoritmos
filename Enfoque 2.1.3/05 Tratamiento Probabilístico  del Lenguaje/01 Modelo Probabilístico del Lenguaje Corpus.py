import random
from collections import Counter
# Importamos `random` para generar selecciones aleatorias y `Counter` para contar ocurrencias de palabras.

# Corpus de ejemplo (puedes sustituirlo por un corpus real)
corpus = "el gato duerme en la cama el perro juega en el jardín el gato juega en el jardín".split() 
# Definimos un corpus de texto como una lista de palabras separadas.

# Contar las ocurrencias de cada palabra
def crear_modelo_probabilistico(corpus):
    """
    Crea un modelo probabilístico basado en la frecuencia de palabras en el corpus.

    :param corpus: Lista de palabras del corpus.
    :return: Diccionario con las palabras y sus probabilidades.
    """
    total_palabras = len(corpus) #len(corpus) es el número total de palabras en el corpus.
    # Contamos el número total de palabras en el corpus.
    # Calculamos el número total de palabras en el corpus.

    conteo_palabras = Counter(corpus) ## Utilizamos Counter para contar las ocurrencias de cada palabra en el corpus.
    # `Counter` crea un diccionario donde las claves son las palabras y los valores son sus conteos.
    # Contamos cuántas veces aparece cada palabra en el corpus.

    # Calcular la probabilidad de cada palabra
    probabilidades = {palabra: conteo / total_palabras for palabra, conteo in conteo_palabras.items()} ## Creamos un diccionario de probabilidades.
    # Usamos una comprensión de diccionario para calcular la probabilidad de cada palabra.
    # Dividimos el conteo de cada palabra entre el total de palabras para obtener su probabilidad.

    return probabilidades #
    # Retornamos el diccionario de probabilidades.

# Crear el modelo probabilístico
modelo = crear_modelo_probabilistico(corpus) 
# Llamamos a la función para crear el modelo probabilístico basado en el corpus.

# Mostrar el modelo probabilístico
print("Modelo Probabilístico del Lenguaje:")
for palabra, probabilidad in modelo.items():
    print(f"{palabra}: {probabilidad:.4f}")
# Mostramos cada palabra junto con su probabilidad en el modelo.