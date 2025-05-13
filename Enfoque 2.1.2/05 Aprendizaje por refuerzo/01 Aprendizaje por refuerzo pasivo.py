# Aprendizaje por Refuerzo Pasivo (Passive Reinforcement Learning)
# En este enfoque, el agente ya tiene una política fija y aprende los valores esperados de los estados observando episodios.

import random  # Importamos la librería random para manejar aleatoriedad si es necesario.

class EntornoSimple:
    """
    Entorno simple en forma de diccionario con recompensas por estado.
    Cada estado es una clave, y el valor es (siguiente_estado, recompensa).
    """
    def __init__(self):
        # Definimos los estados del entorno y sus transiciones.
        # Cada estado tiene un siguiente estado y una recompensa asociada.
        self.estados = {
            "A": ("B", -1),  # Desde el estado "A", se pasa al estado "B" con recompensa -1.
            "B": ("C", -1),  # Desde el estado "B", se pasa al estado "C" con recompensa -1.
            "C": ("Meta", 10),  # Desde el estado "C", se pasa al estado "Meta" con recompensa 10.
            "Meta": (None, 0)  # El estado "Meta" es terminal, no tiene siguiente estado ni recompensa.
        }

    def reset(self):
        """
        Reinicia el entorno al estado inicial.
        """
        return "A"  # Siempre comenzamos desde el estado "A".

    def step(self, estado_actual):
        """
        Devuelve el siguiente estado y la recompensa correspondiente.
        """
        siguiente_estado, recompensa = self.estados[estado_actual]  # Obtenemos el siguiente estado y la recompensa.
        return siguiente_estado, recompensa  # Retornamos el nuevo estado y la recompensa.


def aprendizaje_por_refuerzo_pasivo(entorno, politica, gamma=0.9, episodios=100):
    """
    Aprende el valor de los estados siguiendo una política fija.
    Parámetros:
    - entorno: instancia del entorno donde el agente interactúa.
    - politica: política fija que el agente sigue.
    - gamma: factor de descuento para recompensas futuras.
    - episodios: número de episodios de entrenamiento.

    Retorna:
    - V: diccionario con los valores esperados de los estados.
    """
    # Inicializamos los valores esperados de los estados en 0.
    V = {estado: 0 for estado in entorno.estados}
    # Inicializamos un contador de visitas para cada estado en 0.
    N = {estado: 0 for estado in entorno.estados}

    # Iteramos sobre el número de episodios.
    for _ in range(episodios):
        estado = entorno.reset()  # Reiniciamos el entorno al estado inicial.
        trayectoria = []  # Lista para almacenar la trayectoria del episodio.

        # Seguimos la política hasta llegar a un estado terminal.
        while estado != "Meta":
            trayectoria.append(estado)  # Agregamos el estado actual a la trayectoria.
            estado, recompensa = entorno.step(estado)  # Obtenemos el siguiente estado y la recompensa.

        # Valor de recompensa final (estado terminal).
        G = recompensa

        # Actualizamos los valores hacia atrás en la trayectoria.
        for estado in reversed(trayectoria):  # Recorremos la trayectoria en orden inverso.
            N[estado] += 1  # Incrementamos el contador de visitas para el estado.
            alpha = 1 / N[estado]  # Calculamos la tasa de aprendizaje (disminuye con más visitas).
            V[estado] += alpha * (G - V[estado])  # Actualizamos el valor esperado del estado.
            G = V[estado] * gamma  # Calculamos el valor descontado para el siguiente estado.

    return V  # Retornamos los valores esperados de los estados.


# ----------------------------
# Ejemplo de uso
# ----------------------------
if __name__ == "__main__":
    # Creamos una instancia del entorno.
    entorno = EntornoSimple()

    # Definimos una política fija (aunque no se usa directamente, ya que el entorno tiene transiciones definidas).
    politica = {
        "A": "B",  # Desde el estado "A", la política indica ir al estado "B".
        "B": "C",  # Desde el estado "B", la política indica ir al estado "C".
        "C": "Meta"  # Desde el estado "C", la política indica ir al estado "Meta".
    }

    # Entrenamos al agente utilizando el aprendizaje por refuerzo pasivo.
    valores = aprendizaje_por_refuerzo_pasivo(entorno, politica)

    # Mostramos los valores esperados aprendidos por estado.
    print("Valores aprendidos por estado:")
    for estado, valor in valores.items():
        print(f"{estado}: {valor:.2f}")  # Mostramos el valor esperado de cada estado con dos decimales.