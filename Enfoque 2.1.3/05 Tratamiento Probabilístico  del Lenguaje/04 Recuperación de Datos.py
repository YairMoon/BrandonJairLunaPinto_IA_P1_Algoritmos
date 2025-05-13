from sklearn.feature_extraction.text import TfidfVectorizer
# Importamos `TfidfVectorizer` de scikit-learn para calcular la matriz TF-IDF.

# Corpus de documentos de ejemplo
documentos = [
    "el gato duerme en la cama",
    "el perro juega en el jardín",
    "el gato juega en el jardín",
]
# Definimos un corpus de documentos, donde cada documento es una cadena de texto.

# Crear el modelo TF-IDF
vectorizador = TfidfVectorizer() ## Creamos una instancia de `TfidfVectorizer` para calcular la matriz TF-IDF.
# `TfidfVectorizer` convierte una colección de documentos en una matriz TF-IDF.
# Creamos una instancia del vectorizador TF-IDF.

tfidf_matrix = vectorizador.fit_transform(documentos) ## Ajustamos el vectorizador al corpus de documentos.
# `fit_transform` ajusta el modelo y transforma los documentos en una matriz TF-IDF.
# Calculamos la matriz TF-IDF para el corpus de documentos.

# Mostrar la matriz TF-IDF
print("Matriz TF-IDF:")
print(tfidf_matrix.toarray()) 
# Convertimos la matriz TF-IDF a un arreglo y la mostramos.

# Mostrar las palabras asociadas
print("Palabras en el corpus:")
print(vectorizador.get_feature_names_out()) 
# Mostramos las palabras únicas (características) del corpus que se utilizaron para construir la matriz TF-IDF.