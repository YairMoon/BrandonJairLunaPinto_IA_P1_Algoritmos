# El análisis sintáctico valida la estructura de la oración según las reglas gramaticales.
# Usamos una gramática simple para oraciones en el formato: "Sujeto Verbo Objeto"

def analisis_sintactico(oracion):
    # Gramática simple: Sujeto + Verbo + Objeto
    if len(oracion) == 3:
        sujeto, verbo, objeto = oracion
        if isinstance(sujeto, str) and isinstance(verbo, str) and isinstance(objeto, str):
            return "Estructura válida"
    return "Estructura inválida"

# Ejemplo de uso
oracion1 = ["Juan", "come", "manzana"]
oracion2 = ["Juan", "come"]
print(analisis_sintactico(oracion1))  # Estructura válida
print(analisis_sintactico(oracion2))  # Estructura inválida
# Output:
# Estructura válida