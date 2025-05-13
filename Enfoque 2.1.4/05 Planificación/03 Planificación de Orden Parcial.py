# La planificación de orden parcial permite definir acciones y objetivos sin establecer un orden rígido.
acciones = [
    {"acción": "A", "precondiciones": ["X"], "efectos": ["Y"]},
    {"acción": "B", "precondiciones": ["Y"], "efectos": ["Z"]}
]

# Buscamos la secuencia de acciones que cumpla con los objetivos
objetivo = ["Z"]
plan = []

# Ejecutamos el plan parcialmente
estado = {"X": True, "Y": False, "Z": False}

def planificar(acciones, estado, objetivo):
    while not all(estado.get(o, False) for o in objetivo):
        for accion in acciones:
            if all(estado.get(cond, False) for cond in accion["precondiciones"]):
                plan.append(accion["acción"])
                for efecto in accion["efectos"]:
                    estado[efecto] = True
    return plan

plan = planificar(acciones, estado, objetivo)
print("Plan generado:", plan)
# La salida mostrará el plan generado para alcanzar el objetivo Z a partir del estado inicial.
# En este caso, el plan debe incluir las acciones necesarias para cumplir con los efectos deseados.