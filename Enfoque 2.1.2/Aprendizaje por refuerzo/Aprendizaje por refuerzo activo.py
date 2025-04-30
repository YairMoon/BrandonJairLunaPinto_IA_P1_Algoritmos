# Aprendizaje por Refuerzo Activo (Active Reinforcement Learning)
# Aquí el agente explora activamente para aprender la mejor política.
import random

class EntornoSimple:
    """
    Entorno simple con estados y acciones posibles.
    """
    def __init__(self):
        # Estados: A, B, C, Meta
        # Cada estado tiene acciones que llevan a otros estados
        self.transiciones = {
            "A": {"ir": ("B", -1)},
            "B": {"ir": ("C", -1)},
            "C": {"ir": ("Meta", 10)},
            "Meta": {}  # Estado terminal
        }

    def reset(self):
        # Estado inicial
        return "A"

    def step(self, estado, accion):
        # Si la acción es válida, retorna el nuevo estado y la recompensa
        if accion in self.transiciones[estado]:
            nuevo_estado, recompensa = self.transiciones[estado][accion]
            return nuevo_estado, recompensa
        else:
            return estado, -10  # Penalización por acción inválida


def aprendizaje_por_refuerzo_activo(entorno, gamma=0.9, alpha=0.1, epsilon=0.1, episodios=100):
    """
    Algoritmo activo: aprende la mejor política probando acciones.
    """
    Q = {}  # Q(s, a): valor de estado-acción
    politica = {}  # Política derivada del Q

    for estado in entorno.transiciones:
        Q[estado] = {}
        for accion in entorno.transiciones[estado]:
            Q[estado][accion] = 0  # Inicializamos Q en cero

    for ep in range(episodios):
        estado = entorno.reset()

        while estado != "Meta":
            # Exploración vs explotación
            if random.random() < epsilon:
                accion = random.choice(list(Q[estado].keys()))  # Acción aleatoria
            else:
                accion = max(Q[estado], key=Q[estado].get)  # Mejor acción actual

            nuevo_estado, recompensa = entorno.step(estado, accion)

            # Actualización Q-learning
            max_Q_nuevo = max(Q[nuevo_estado].values()) if nuevo_estado in Q and Q[nuevo_estado] else 0
            Q[estado][accion] += alpha * (recompensa + gamma * max_Q_nuevo - Q[estado][accion])

            estado = nuevo_estado  # Avanzamos al siguiente estado

    # Derivamos la política óptima de Q
    for estado in Q:
        if Q[estado]:
            politica[estado] = max(Q[estado], key=Q[estado].get)

    return Q, politica


# ----------------------------
# Ejemplo de uso
# ----------------------------
if __name__ == "__main__":
    entorno = EntornoSimple()

    Q, politica = aprendizaje_por_refuerzo_activo(entorno)

    print("Q-valores aprendidos:")
    for estado in Q:
        for accion in Q[estado]:
            print(f"Q({estado}, {accion}) = {Q[estado][accion]:.2f}")

    print("\nPolítica derivada:")
    for estado in politica:
        print(f"{estado} -> {politica[estado]}")
#     # Mostramos los valores finales de cada estado
#     for state, value in V.items():