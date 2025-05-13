# STRIPS es un modelo de planificación basado en un espacio de estados.
# Definimos la condición inicial, los objetivos y las acciones posibles.

# Estado inicial
estado_inicial = {"en_biblioteca": True, "tiene_libro": False}

# Objetivos
objetivo = {"tiene_libro": True}

# Definimos una acción de "ir_a_biblioteca"
def ir_a_biblioteca(estado):
    if estado["en_biblioteca"] == False:
        estado["en_biblioteca"] = True
        print("Ahora estás en la biblioteca.")
    return estado

# Definimos una acción de "tomar_libro"
def tomar_libro(estado):
    if estado["en_biblioteca"] and estado["tiene_libro"] == False:
        estado["tiene_libro"] = True
        print("Ahora tienes el libro.")
    return estado

# Secuencia de acciones para cumplir los objetivos
estado = ir_a_biblioteca(estado_inicial)
estado = tomar_libro(estado)

# Verificamos si se ha alcanzado el objetivo
print("Objetivo alcanzado:", estado == objetivo)
# La salida mostrará si se ha alcanzado el objetivo de tener el libro después de realizar las acciones definidas.
# En este caso, el estado final debe ser {"en_biblioteca": True, "tiene_libro": True} para que el objetivo se considere alcanzado.