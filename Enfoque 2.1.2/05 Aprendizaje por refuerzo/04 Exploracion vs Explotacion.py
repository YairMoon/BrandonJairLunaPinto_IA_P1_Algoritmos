# Exploración vs. Explotación usando un entorno tipo multi-armed bandit

import random  # Importamos la librería random para manejar la exploración aleatoria.

class Bandit:
    """
    Entorno tipo 'k-armed bandit': cada acción tiene una probabilidad fija de recompensa.
    """
    def __init__(self, probabilidades):
        # Inicializamos las probabilidades de recompensa para cada acción.
        self.probabilidades = probabilidades  # Probabilidad de recompensa por cada acción.

    def tirar(self, accion):
        """
        Simula tirar del brazo indicado. Retorna 1 con cierta probabilidad, 0 de lo contrario.
        """
        # Generamos un número aleatorio y comparamos con la probabilidad de la acción.
        return 1 if random.random() < self.probabilidades[accion] else 0


def epsilon_greedy(bandit, epsilon=0.1, iteraciones=1000):
    """
    Estrategia epsilon-greedy: con probabilidad ε se explora, si no, se explota.

    Parámetros:
    - bandit: instancia del entorno tipo multi-armed bandit.
    - epsilon: probabilidad de exploración.
    - iteraciones: número de iteraciones para ejecutar la estrategia.

    Retorna:
    - conteos: número de veces que se eligió cada acción.
    - recompensas: suma de recompensas obtenidas por cada acción.
    - total: recompensa total acumulada.
    """
    n_acciones = len(bandit.probabilidades)  # Número de acciones disponibles.
    conteos = [0] * n_acciones  # Inicializamos el conteo de elecciones por acción.
    recompensas = [0] * n_acciones  # Inicializamos la suma de recompensas por acción.

    historial = []  # Lista para guardar la recompensa obtenida en cada iteración.

    for t in range(iteraciones):  # Iteramos sobre el número de iteraciones.
        # Explora con probabilidad ε.
        if random.random() < epsilon:
            accion = random.randint(0, n_acciones - 1)  # Elegimos una acción aleatoria.
        else:
            # Explotamos la acción con mejor recompensa promedio.
            promedios = [recompensas[i] / conteos[i] if conteos[i] > 0 else 0 for i in range(n_acciones)]
            accion = promedios.index(max(promedios))  # Seleccionamos la acción con el mayor promedio.

        recompensa = bandit.tirar(accion)  # Obtenemos la recompensa al tirar del brazo seleccionado.

        conteos[accion] += 1  # Incrementamos el conteo de la acción seleccionada.
        recompensas[accion] += recompensa  # Sumamos la recompensa obtenida.
        historial.append(recompensa)  # Guardamos la recompensa en el historial.

    return conteos, recompensas, sum(historial)  # Retornamos los resultados.


# ----------------------------
# Ejemplo de uso
# ----------------------------
if __name__ == "__main__":
    # Probabilidades reales de recompensa de cada acción (desconocidas para el agente).
    probabilidades_reales = [0.1, 0.5, 0.9]  # Definimos las probabilidades de recompensa para cada brazo.
    bandit = Bandit(probabilidades_reales)  # Creamos una instancia del entorno tipo bandit.

    print("Probabilidades reales de los brazos:", probabilidades_reales)  # Mostramos las probabilidades reales.

    epsilon = 0.1  # Definimos la probabilidad de exploración.
    conteos, recompensas, total = epsilon_greedy(bandit, epsilon)  # Ejecutamos la estrategia epsilon-greedy.

    # Mostramos los resultados obtenidos.
    print(f"\nExploración ε = {epsilon}")
    print("Número de veces que se eligió cada acción:", conteos)  # Veces que se eligió cada acción.
    print("Recompensas acumuladas por acción:", recompensas)  # Recompensas acumuladas por acción.
    print("Recompensa total obtenida:", total)  # Recompensa total acumulada.