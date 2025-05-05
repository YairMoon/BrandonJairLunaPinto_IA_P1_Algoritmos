# Proceso simple para generar explicaciones y extraer información relevante
def generar_explicacion(modelo, caracteristicas):
    explicacion = f"Modelo predice con características {caracteristicas}."
    return explicacion

# Definimos un modelo simple (puede ser un árbol de decisión o regresión)
modelo = "Modelo de clasificación simple"

# Generamos explicación
explicacion = generar_explicacion(modelo, [3, 5])
print(explicacion)
