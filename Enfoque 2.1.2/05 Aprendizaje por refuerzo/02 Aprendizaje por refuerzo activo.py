# Aprendizaje por Refuerzo Activo (Active Reinforcement Learning)
# Este script implementa un algoritmo de aprendizaje por refuerzo activo utilizando Q-learning.
# El agente explora activamente un entorno para aprender la mejor política.

import random  # Se utiliza para generar números aleatorios, necesarios para la exploración.

class EntornoSimple:## Definición de un entorno simple para el aprendizaje por refuerzo.
    """
    Clase que define un entorno simple con estados y acciones posibles.
    """
    def __init__(self):## Inicializa el entorno.
        # Diccionario que define las transiciones entre estados.
        # Cada estado tiene acciones que llevan a otros estados y recompensas asociadas.
        self.transiciones = {
            "A": {"ir": ("B", -1)},  # Desde el estado "A", la acción "ir" lleva al estado "B" con recompensa -1.
            "B": {"ir": ("C", -1)},  # Desde el estado "B", la acción "ir" lleva al estado "C" con recompensa -1.
            "C": {"ir": ("Meta", 10)},  # Desde el estado "C", la acción "ir" lleva al estado "Meta" con recompensa 10.
            "Meta": {}  # El estado "Meta" es terminal, no tiene acciones.
        }

    def reset(self): ## Reinicia el entorno al estado inicial.
        """
        Reinicia el entorno al estado inicial.
        """
        return "A"  # El estado inicial siempre es "A".

    def step(self, estado, accion): 
        """
        Realiza una acción en el estado actual.
        - Si la acción es válida, retorna el nuevo estado y la recompensa.
        - Si la acción no es válida, retorna el mismo estado y una penalización de -10.
        """
        if accion in self.transiciones[estado]: ## Verificamos si la acción es válida en el estado actual.
            nuevo_estado, recompensa = self.transiciones[estado][accion]## Obtenemos el nuevo estado y la recompensa asociada a la acción.
            return nuevo_estado, recompensa## Retornamos el nuevo estado y la recompensa.
        else:
            return estado, -10  # Penalización por acción inválida.


def aprendizaje_por_refuerzo_activo(entorno, gamma=0.9, alpha=0.1, epsilon=0.1, episodios=100):## Implementación del algoritmo de Q-learning para aprendizaje por refuerzo activo.
    """
    Implementa el algoritmo de Q-learning para aprendizaje por refuerzo activo.
    Parámetros:
    - entorno: instancia del entorno donde el agente interactúa.
    - gamma: factor de descuento para recompensas futuras.
    - alpha: tasa de aprendizaje.
    - epsilon: probabilidad de exploración (acción aleatoria).
    - episodios: número de episodios de entrenamiento.

    Retorna:
    - Q: diccionario con los valores Q(s, a) aprendidos.
    - politica: diccionario con la política óptima derivada de Q.
    """
    Q = {}  # Diccionario para almacenar los valores Q(s, a).
    politica = {}  # Diccionario para almacenar la política óptima.

    # Inicialización de Q para todos los estados y acciones.
    for estado in entorno.transiciones:## Iteramos sobre los estados definidos en el entorno.
        Q[estado] = {}## Inicializamos un diccionario para cada estado.
        for accion in entorno.transiciones[estado]:## Iteramos sobre las acciones posibles en el estado.
            Q[estado][accion] = 0  # Inicializamos todos los valores Q en 0.

    # Iteramos sobre el número de episodios.
    for ep in range(episodios):## Para cada episodio, reiniciamos el entorno.
        estado = entorno.reset()  # Reiniciamos el entorno al estado inicial.

        # Mientras no se alcance el estado terminal ("Meta").
        while estado != "Meta":## Mientras el estado no sea "Meta", continuamos explorando.
            # Decisión de exploración vs explotación.
            if random.random() < epsilon:## Con probabilidad epsilon, exploramos (acción aleatoria).
                # Exploración: seleccionamos una acción aleatoria.
                accion = random.choice(list(Q[estado].keys()))## Elegimos una acción aleatoria entre las posibles en el estado actual.
            else:
                # Explotación: seleccionamos la mejor acción según Q.
                accion = max(Q[estado], key=Q[estado].get)## Elegimos la acción con el mayor valor Q en el estado actual.

            # Realizamos la acción y obtenemos el nuevo estado y la recompensa.
            nuevo_estado, recompensa = entorno.step(estado, accion) 

            # Actualización de Q-learning.
            # Calculamos el valor máximo de Q para el nuevo estado.
            max_Q_nuevo = max(Q[nuevo_estado].values()) if nuevo_estado in Q and Q[nuevo_estado] else 0## Si el nuevo estado no tiene acciones, max_Q_nuevo es 0.
            # Fórmula de actualización de Q.
            Q[estado][accion] += alpha * (recompensa + gamma * max_Q_nuevo - Q[estado][accion])## Actualizamos el valor Q(s, a) utilizando la fórmula de Q-learning.

            # Avanzamos al siguiente estado.
            estado = nuevo_estado## Actualizamos el estado actual al nuevo estado.

    # Derivamos la política óptima a partir de los valores Q.
    for estado in Q:## Iteramos sobre los estados aprendidos.
        if Q[estado]:  # Si hay acciones disponibles en el estado.
            politica[estado] = max(Q[estado], key=Q[estado].get)  # Seleccionamos la acción con el mayor valor Q.

    return Q, politica  # Retornamos los valores Q y la política óptima.


# ----------------------------
# Ejemplo de uso
# ----------------------------
if __name__ == "__main__":## Bloque principal para ejecutar el script.
    # Creamos una instancia del entorno.
    entorno = EntornoSimple()## Creamos el entorno simple.

    # Entrenamos al agente utilizando el algoritmo de aprendizaje por refuerzo activo.
    Q, politica = aprendizaje_por_refuerzo_activo(entorno)## Entrenamos al agente y obtenemos los valores Q y la política óptima.

    # Mostramos los valores Q aprendidos.
    print("Q-valores aprendidos:")
    for estado in Q:## Iteramos sobre los estados aprendidos.
        for accion in Q[estado]:## Iteramos sobre las acciones posibles en el estado.
            print(f"Q({estado}, {accion}) = {Q[estado][accion]:.2f}")## Mostramos el valor Q(s, a) para cada estado y acción.
    # Mostramos la política óptima derivada.
    print("\nPolítica derivada:")## Mostramos la política óptima aprendida.
    for estado in politica:## Iteramos sobre los estados aprendidos.
        print(f"{estado} -> {politica[estado]}")## Mostramos la acción óptima para cada estado.