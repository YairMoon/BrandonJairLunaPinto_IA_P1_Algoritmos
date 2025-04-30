# Función de utilidad simple para distintos tipos de estados

def utility(state):
    # Si el estado es "goal", se asigna una utilidad alta
    if state == "goal":
        return 100
    # Si el estado representa un obstáculo, la utilidad es negativa
    elif state == "obstacle":
        return -100
    # En otros casos, retornamos una utilidad neutra o baja
    else:
        return -1
