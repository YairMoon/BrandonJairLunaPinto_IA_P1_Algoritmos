# Diccionario simple de traducción de palabras (Inglés a Español)
diccionario = {
    "hello": "hola",
    "world": "mundo",
    "cat": "gato",
    "dog": "perro"
}

# Función para traducir una frase
def traducir(entrada, diccionario):
    palabras = entrada.split()
    traduccion = [diccionario.get(palabra, palabra) for palabra in palabras]
    return " ".join(traduccion)

# Traducir una frase
frase_ingles = "hello world"
frase_espanol = traducir(frase_ingles, diccionario)
print("Frase en Español:", frase_espanol)
