# Teoría de Juegos - Cálculo del Equilibrio de Nash en un juego simple

import numpy as np  # Importamos numpy para manejar matrices y cálculos numéricos
from scipy.optimize import linprog  # Importamos linprog para resolver problemas de programación lineal

def nash_equilibrium(payoff_matrix_player1, payoff_matrix_player2): ## Definimos la función para calcular el equilibrio de Nash
    """
    Calcula el Equilibrio de Nash para un juego de dos jugadores con estrategias mixtas.
    
    :param payoff_matrix_player1: Matriz de pagos para el Jugador 1.
    :param payoff_matrix_player2: Matriz de pagos para el Jugador 2.
    :return: Estrategias mixtas de equilibrio para ambos jugadores.
    """
    # Número de estrategias de cada jugador
    num_strategies_player1 = len(payoff_matrix_player1)  # Filas de la matriz del Jugador 1
    num_strategies_player2 = len(payoff_matrix_player2[0])  # Columnas de la matriz del Jugador 2

    # Maximización de las utilidades de ambos jugadores
    c1 = [-1] * num_strategies_player1  # Coeficientes para maximizar la utilidad del Jugador 1
    c2 = [-1] * num_strategies_player2  # Coeficientes para maximizar la utilidad del Jugador 2

    # Restricciones de probabilidad para que las probabilidades sumen 1
    A_ub = np.ones((num_strategies_player1, num_strategies_player2))  # Restricciones de desigualdad
    b_ub = [1] * num_strategies_player2  # Suma de probabilidades debe ser 1

    # Resolver el problema de programación lineal para encontrar el equilibrio
    result_player1 = linprog(c1, A_ub=A_ub, b_ub=b_ub, bounds=[(0, 1)] * num_strategies_player1) # Resolvemos para el Jugador 1
    result_player2 = linprog(c2, A_ub=A_ub, b_ub=b_ub, bounds=[(0, 1)] * num_strategies_player2) # Resolvemos para el Jugador 2

    return result_player1.x, result_player2.x  # Retornamos las estrategias mixtas de equilibrio


# ----------------------------
# Ejemplo de uso
# ----------------------------
if __name__ == "__main__":
    # Matrices de pago para los jugadores
    payoff_matrix_player1 = np.array([[3, 0], [5, 1]])  # Matriz de pagos del Jugador 1
    payoff_matrix_player2 = np.array([[3, 5], [0, 1]])  # Matriz de pagos del Jugador 2

    # Calculamos el equilibrio de Nash
    eq_player1, eq_player2 = nash_equilibrium(payoff_matrix_player1, payoff_matrix_player2) ## Llamamos a la función para calcular el equilibrio
    # Normalizamos las estrategias para que sumen 1

    # Mostramos los resultados
    print(f"Equilibrio de Nash para Jugador 1: {eq_player1}") # Mostramos el equilibrio de Nash para el Jugador 1
    print(f"Equilibrio de Nash para Jugador 2: {eq_player2}") # Mostramos el equilibrio de Nash para el Jugador 2