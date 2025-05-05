# El análisis semántico busca verificar el significado de las oraciones.
# Para este ejemplo, verificaremos si una oración tiene sentido lógico.

def analisis_semanico(oracion):
    sujeto, verbo, objeto = oracion
    if verbo == "come" and objeto in ["manzana", "plátano", "pera"]:
        return f"{sujeto} está comiendo una fruta."
    elif verbo == "corre" and objeto == "camino":
        return f"{sujeto} está corriendo en el camino."
    else:
        return "Oración sin sentido lógico."

# Ejemplo de uso
oracion1 = ["Juan", "come", "manzana"]
oracion2 = ["Ana", "lee", "libro"]
print(analisis_semanico(oracion1))  # Juan está comiendo una fruta.
print(analisis_semanico(oracion2))  # Oración sin sentido lógico.
# Output:
# Juan está comiendo una fruta.