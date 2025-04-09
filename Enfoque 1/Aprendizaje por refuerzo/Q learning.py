# Q-Learning en un entorno simple de moverse hacia la derecha

import random

class EntornoLineal:
    """
    Entorno simple: avanzar desde estado 0 hasta el estado final (meta = 4).
    """
    def __init__(self):
        self.estado_final = 4  # Estado objetivo
        self.estado = 0        # Estado inicial

    def reset(self):
        """
        Reinicia el entorno al estado inicial.
        """
        self.estado = 0
        return self.estado

    def step(self, estado, accion):
        """
        Ejecuta una acción en el entorno.

        Parámetros:
        - estado: estado actual
        - accion: 0 = quedarse, 1 = avanzar

        Retorna:
        - nuevo_estado: estado resultante
        - recompensa: +1 si llega a la meta, -0.1 en otro caso
        """
        if accion == 1:
            nuevo_estado = min(estado + 1, self.estado_final)
        else:
            nuevo_estado = estado

        recompensa = 1 if nuevo_estado == self.estado_final else -0.1
        return nuevo_estado, recompensa

    def acciones(self):
        """
        Lista de acciones posibles.
        """
        return [0, 1]  # 0 = quedarse, 1 = avanzar


def q_learning(entorno, alpha=0.1, gamma=0.9, epsilon=0.2, episodios=500):
    """
    Algoritmo Q-learning: aprende valores Q para un entorno.

    Parámetros:
    - alpha: tasa de aprendizaje
    - gamma: factor de descuento
    - epsilon: tasa de exploración
    - episodios: número de episodios de entrenamiento

    Retorna:
    - Q: tabla de valores Q aprendida
    """
    Q = {}  # Tabla Q: Q[estado][accion]
    acciones = entorno.acciones()

    for ep in range(episodios):
        estado = entorno.reset()

        while estado != entorno.estado_final:
            # Inicializa Q[estado] si no existe
            if estado not in Q:
                Q[estado] = {a: 0 for a in acciones}

            # Selección de acción: exploración vs. explotación
            if random.random() < epsilon:
                accion = random.choice(acciones)  # Explorar
            else:
                # Elegir la mejor acción según Q
                accion = max(Q[estado], key=Q[estado].get)

            # Ejecutar acción
            nuevo_estado, recompensa = entorno.step(estado, accion)

            # Inicializa Q[nuevo_estado] si no existe
            if nuevo_estado not in Q:
                Q[nuevo_estado] = {a: 0 for a in acciones}

            # Valor máximo del siguiente estado
            mejor_Q_siguiente = max(Q[nuevo_estado].values())

            # Actualizar la Q-table
            Q[estado][accion] += alpha * (recompensa + gamma * mejor_Q_siguiente - Q[estado][accion])

            # Avanzamos al siguiente estado
            estado = nuevo_estado

    return Q


# ----------------------------
# Ejemplo de uso
# ----------------------------
if __name__ == "__main__":
    entorno = EntornoLineal()

    Q = q_learning(entorno)

    print("Tabla Q aprendida:")
    for estado in sorted(Q):
        print(f"Estado {estado}: {Q[estado]}")

    print("\nPolítica aprendida:")
    for estado in sorted(Q):
        mejor_accion = max(Q[estado], key=Q[estado].get)
        accion_texto = "Avanzar" if mejor_accion == 1 else "Quedarse"
        print(f"Estado {estado}: {accion_texto}")
#     print(f"Estado {estado}: {mejor_accion}")
#     print(f"Estado {estado}: {accion_texto}")