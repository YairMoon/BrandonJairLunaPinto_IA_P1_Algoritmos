# Exploración vs. Explotación usando un entorno tipo multi-armed bandit
import random

class Bandit:
    """
    Entorno tipo 'k-armed bandit': cada acción tiene una probabilidad fija de recompensa.
    """
    def __init__(self, probabilidades):
        self.probabilidades = probabilidades  # Probabilidad de recompensa por cada acción

    def tirar(self, accion):
        """
        Simula tirar del brazo indicado. Retorna 1 con cierta probabilidad, 0 de lo contrario.
        """
        return 1 if random.random() < self.probabilidades[accion] else 0


def epsilon_greedy(bandit, epsilon=0.1, iteraciones=1000):
    """
    Estrategia epsilon-greedy: con probabilidad ε se explora, si no, se explota.
    """
    n_acciones = len(bandit.probabilidades)
    conteos = [0] * n_acciones  # Número de veces que se ha elegido cada acción
    recompensas = [0] * n_acciones  # Suma de recompensas por acción

    historial = []  # Guardamos la recompensa por paso

    for t in range(iteraciones):
        # Explora con probabilidad ε
        if random.random() < epsilon:
            accion = random.randint(0, n_acciones - 1)
        else:
            # Explotamos la acción con mejor recompensa promedio
            promedios = [recompensas[i] / conteos[i] if conteos[i] > 0 else 0 for i in range(n_acciones)]
            accion = promedios.index(max(promedios))

        recompensa = bandit.tirar(accion)

        conteos[accion] += 1
        recompensas[accion] += recompensa
        historial.append(recompensa)

    return conteos, recompensas, sum(historial)


# ----------------------------
# Ejemplo de uso
# ----------------------------
if __name__ == "__main__":
    # Probabilidades reales de recompensa de cada acción (desconocidas para el agente)
    probabilidades_reales = [0.1, 0.5, 0.9]
    bandit = Bandit(probabilidades_reales)

    print("Probabilidades reales de los brazos:", probabilidades_reales)

    epsilon = 0.1
    conteos, recompensas, total = epsilon_greedy(bandit, epsilon)

    print(f"\nExploración ε = {epsilon}")
    print("Número de veces que se eligió cada acción:", conteos)
    print("Recompensas acumuladas por acción:", recompensas)
    print("Recompensa total obtenida:", total)
#     # Mostramos los resultados