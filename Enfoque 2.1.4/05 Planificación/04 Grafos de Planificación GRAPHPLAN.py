# Simulación de GRAPHPLAN con un pequeño conjunto de acciones
acciones = {
    "ir_a_biblioteca": {"precondiciones": ["en_casa"], "efectos": ["en_biblioteca"]},
    "tomar_libro": {"precondiciones": ["en_biblioteca", "libro_disponible"], "efectos": ["tiene_libro"]},
}

estado = {"en_casa": True, "en_biblioteca": False, "libro_disponible": True, "tiene_libro": False}

# Planificación con GRAPHPLAN (de manera simplificada)
def graphplan(acciones, estado, objetivo):
    plan = []
    while not all(estado.get(o, False) for o in objetivo):
        for accion, detalles in acciones.items():
            if all(estado.get(cond, False) for cond in detalles["precondiciones"]):
                plan.append(accion)
                for efecto in detalles["efectos"]:
                    estado[efecto] = True
    return plan

# Generamos el plan con GRAPHPLAN
plan = graphplan(acciones, estado, ["tiene_libro"])
print("Plan generado por GRAPHPLAN:", plan)
# # La salida mostrará el plan generado para alcanzar el objetivo de tener un libro.
# # En este caso, el plan debe incluir las acciones necesarias para cumplir con los efectos deseados.