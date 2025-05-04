from sklearn.feature_extraction.text import TfidfVectorizer

# Corpus de documentos de ejemplo
documentos = [
    "el gato duerme en la cama",
    "el perro juega en el jardín",
    "el gato juega en el jardín",
]

# Crear el modelo TF-IDF
vectorizador = TfidfVectorizer()
tfidf_matrix = vectorizador.fit_transform(documentos)

# Mostrar la matriz TF-IDF
print("Matriz TF-IDF:")
print(tfidf_matrix.toarray())

# Mostrar las palabras asociadas
print("Palabras en el corpus:")
print(vectorizador.get_feature_names_out())
