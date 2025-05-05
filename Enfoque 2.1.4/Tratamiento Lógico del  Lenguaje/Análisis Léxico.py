# El análisis léxico es el proceso de dividir una cadena de texto en tokens (palabras, números, etc.)
# Simulamos un análisis léxico simple dividiendo un texto en palabras y clasificándolas.

import re

def analisis_lexico(texto):
    # Expresiones regulares para identificar tipos de tokens
    patron_palabra = r'\b\w+\b'  # Para encontrar palabras
    patron_numero = r'\b\d+\b'   # Para encontrar números
    
    # Encontramos todas las palabras y números
    palabras = re.findall(patron_palabra, texto)
    numeros = re.findall(patron_numero, texto)
    
    return {"palabras": palabras, "numeros": numeros}

# Ejemplo de uso
texto = "El precio es 100 y el descuento es 20"
resultado = analisis_lexico(texto)
print("Palabras:", resultado["palabras"])
print("Números:", resultado["numeros"])
# Output:
# Palabras: ['El', 'precio', 'es', 'y', 'el', 'descuento', 'es']