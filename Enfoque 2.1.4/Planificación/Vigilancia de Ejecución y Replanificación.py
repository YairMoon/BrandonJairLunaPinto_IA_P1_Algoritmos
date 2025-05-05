# Vigilamos el estado de las tareas y replanificamos si es necesario
estado_ejecucion = {"tarea_terminada": False}

def vigilancia(estado):
    if not estado["tarea_terminada"]:
        print("Replanificando...")
        estado["tarea_terminada"] = True
        return "Tarea completada"
    else:
        return "Tarea ya completada"

resultado = vigilancia(estado_ejecucion)
print("Resultado de la vigilancia:", resultado)
# La salida mostrará el resultado de la vigilancia y replanificación de la tarea.
# En este caso, si la tarea no está terminada, se replanifica y se marca como completada.