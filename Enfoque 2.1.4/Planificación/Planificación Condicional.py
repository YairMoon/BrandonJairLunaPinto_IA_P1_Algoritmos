# Planificación condicional según el estado
estado = {"es_tarde": False, "hay_comida": True}

def plan_condicional(estado):
    if estado["es_tarde"]:
        return "Ir a dormir"
    elif estado["hay_comida"]:
        return "Cenar"
    else:
        return "Leer un libro"

plan = plan_condicional(estado)
print("Plan condicional:", plan)
# La salida mostrará el plan condicional basado en el estado actual.
# En este caso, si es tarde, el plan es "Ir a dormir", si hay comida, el plan es "Cenar", de lo contrario, "Leer un libro".