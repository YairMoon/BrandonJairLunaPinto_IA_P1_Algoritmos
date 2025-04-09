# Aprendizaje por Refuerzo Pasivo (Passive Reinforcement Learning)
# En este enfoque, el agente ya tiene una política fija y aprende los valores esperados de los estados observando episodios.

import random

class EntornoSimple:
    """
    Entorno simple en forma de diccionario con recompensas por estado.
    Cada estado es una clave, y el valor es (siguiente_estado, recompensa).
    """
    def __init__(self):
        self.estados = {
            "A": ("B", -1),
            "B": ("C", -1),
            "C": ("Meta", 10),
            "Meta": (None, 0)
        }

    def reset(self):
        # Iniciamos siempre desde el estado "A"
        return "A"

    def step(self, estado_actual):
        # Devuelve el siguiente estado y la recompensa correspondiente
        siguiente_estado, recompensa = self.estados[estado_actual]
        return siguiente_estado, recompensa


def aprendizaje_por_refuerzo_pasivo(entorno, politica, gamma=0.9, episodios=100):
    """
    Aprende el valor de los estados siguiendo una política fija
    """
    V = {estado: 0 for estado in entorno.estados}  # Inicializamos los valores a 0
    N = {estado: 0 for estado in entorno.estados}  # Contador de visitas

    for _ in range(episodios):
        estado = entorno.reset()
        trayectoria = []

        # Seguimos la política hasta llegar a un estado terminal
        while estado != "Meta":
            trayectoria.append(estado)
            estado, recompensa = entorno.step(estado)

        # Valor de recompensa final
        G = recompensa

        # Actualizamos los valores hacia atrás en la trayectoria
        for estado in reversed(trayectoria):
            N[estado] += 1
            alpha = 1 / N[estado]  # Tasa de aprendizaje decae con visitas
            V[estado] += alpha * (G - V[estado])  # Promedio incremental
            G = V[estado] * gamma  # Descuento futuro

    return V


# ----------------------------
# Ejemplo de uso
# ----------------------------
if __name__ == "__main__":
    entorno = EntornoSimple()

    # Política fija (no se usa directamente, ya que el entorno tiene transiciones definidas)
    politica = {
        "A": "B",
        "B": "C",
        "C": "Meta"
    }

    valores = aprendizaje_por_refuerzo_pasivo(entorno, politica)
    print("Valores aprendidos por estado:")
    for estado, valor in valores.items():
        print(f"{estado}: {valor:.2f}")
