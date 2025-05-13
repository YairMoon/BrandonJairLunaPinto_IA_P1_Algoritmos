# Diccionario simple de traducción de palabras (Inglés a Español)
diccionario = {
    "hello": "hola",
    "world": "mundo",
    "cat": "gato",
    "dog": "perro"
}
# Definimos un diccionario que mapea palabras en inglés a sus equivalentes en español.

# Función para traducir una frase
def traducir(entrada, diccionario):
    """
    Traduce una frase del inglés al español utilizando un diccionario.

    :param entrada: Frase en inglés como cadena de texto.
    :param diccionario: Diccionario de traducción (Inglés a Español).
    :return: Frase traducida al español.
    """
    palabras = entrada.split()
    # Dividimos la frase en palabras individuales.

    traduccion = [diccionario.get(palabra, palabra) for palabra in palabras]
    # Traducimos cada palabra utilizando el diccionario.
    # Si una palabra no está en el diccionario, se deja sin traducir.

    return " ".join(traduccion)
    # Unimos las palabras traducidas en una sola cadena.

# Traducir una frase
frase_ingles = "hello world"
# Definimos una frase en inglés para traducir.

frase_espanol = traducir(frase_ingles, diccionario)
# Llamamos a la función para traducir la frase al español.

print("Frase en Español:", frase_espanol)
# Mostramos la frase traducida.