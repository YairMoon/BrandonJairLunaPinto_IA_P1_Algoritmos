# Q-Learning en un entorno simple de moverse hacia la derecha

import random  # Importamos la librería random para manejar la exploración aleatoria.

class EntornoLineal:
    """
    Entorno simple: avanzar desde estado 0 hasta el estado final (meta = 4).
    """
    def __init__(self):
        self.estado_final = 4  # Definimos el estado objetivo (meta).
        self.estado = 0        # Estado inicial del agente.

    def reset(self):
        """
        Reinicia el entorno al estado inicial.
        """
        self.estado = 0  # Reiniciamos el estado al inicial.
        return self.estado  # Retornamos el estado inicial.

    def step(self, estado, accion):
        """
        Ejecuta una acción en el entorno.

        Parámetros:
        - estado: estado actual.
        - accion: 0 = quedarse, 1 = avanzar.

        Retorna:
        - nuevo_estado: estado resultante.
        - recompensa: +1 si llega a la meta, -0.1 en otro caso.
        """
        if accion == 1:  # Si la acción es avanzar.
            nuevo_estado = min(estado + 1, self.estado_final)  # Avanzamos al siguiente estado, sin exceder la meta.
        else:  # Si la acción es quedarse.
            nuevo_estado = estado  # El estado no cambia.

        recompensa = 1 if nuevo_estado == self.estado_final else -0.1  # Recompensa por llegar a la meta o penalización.
        return nuevo_estado, recompensa  # Retornamos el nuevo estado y la recompensa.

    def acciones(self):
        """
        Lista de acciones posibles.
        """
        return [0, 1]  # 0 = quedarse, 1 = avanzar.


def q_learning(entorno, alpha=0.1, gamma=0.9, epsilon=0.2, episodios=500):
    """
    Algoritmo Q-learning: aprende valores Q para un entorno.

    Parámetros:
    - alpha: tasa de aprendizaje.
    - gamma: factor de descuento.
    - epsilon: tasa de exploración.
    - episodios: número de episodios de entrenamiento.

    Retorna:
    - Q: tabla de valores Q aprendida.
    """
    Q = {}  # Tabla Q: Q[estado][accion].
    acciones = entorno.acciones()  # Obtenemos las acciones posibles.

    for ep in range(episodios):  # Iteramos sobre el número de episodios.
        estado = entorno.reset()  # Reiniciamos el entorno al estado inicial.

        while estado != entorno.estado_final:  # Mientras no lleguemos al estado final.
            # Inicializamos Q[estado] si no existe.
            if estado not in Q:
                Q[estado] = {a: 0 for a in acciones}  # Inicializamos las acciones con valor 0.

            # Selección de acción: exploración vs. explotación.
            if random.random() < epsilon:  # Con probabilidad epsilon, exploramos.
                accion = random.choice(acciones)  # Elegimos una acción aleatoria.
            else:
                # Explotamos la mejor acción según Q.
                accion = max(Q[estado], key=Q[estado].get)

            # Ejecutamos la acción.
            nuevo_estado, recompensa = entorno.step(estado, accion)

            # Inicializamos Q[nuevo_estado] si no existe.
            if nuevo_estado not in Q:
                Q[nuevo_estado] = {a: 0 for a in acciones}

            # Valor máximo del siguiente estado.
            mejor_Q_siguiente = max(Q[nuevo_estado].values())

            # Actualizamos la Q-table usando la fórmula de Q-learning.
            Q[estado][accion] += alpha * (recompensa + gamma * mejor_Q_siguiente - Q[estado][accion])

            # Avanzamos al siguiente estado.
            estado = nuevo_estado

    return Q  # Retornamos la tabla Q aprendida.


# ----------------------------
# Ejemplo de uso
# ----------------------------
if __name__ == "__main__":
    entorno = EntornoLineal()  # Creamos una instancia del entorno.

    Q = q_learning(entorno)  # Entrenamos al agente utilizando Q-learning.

    # Mostramos la tabla Q aprendida.
    print("Tabla Q aprendida:")
    for estado in sorted(Q):  # Iteramos sobre los estados en orden.
        print(f"Estado {estado}: {Q[estado]}")  # Mostramos los valores Q para cada estado.

    # Mostramos la política aprendida.
    print("\nPolítica aprendida:")
    for estado in sorted(Q):  # Iteramos sobre los estados en orden.
        mejor_accion = max(Q[estado], key=Q[estado].get)  # Seleccionamos la mejor acción según Q.
        accion_texto = "Avanzar" if mejor_accion == 1 else "Quedarse"  # Convertimos la acción a texto.
        print(f"Estado {estado}: {accion_texto}")  # Mostramos la acción óptima para cada estado.