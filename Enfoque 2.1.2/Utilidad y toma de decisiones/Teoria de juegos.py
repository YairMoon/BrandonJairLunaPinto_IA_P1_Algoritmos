# Teoría de Juegos - Cálculo del Equilibrio de Nash en un juego simple

import numpy as np
from scipy.optimize import linprog

def nash_equilibrium(payoff_matrix_player1, payoff_matrix_player2):
    # Número de estrategias de cada jugador
    num_strategies_player1 = len(payoff_matrix_player1)
    num_strategies_player2 = len(payoff_matrix_player2[0])

    # Maximización de las utilidades de ambos jugadores
    c1 = [-1] * num_strategies_player1
    c2 = [-1] * num_strategies_player2

    # Restricciones de probabilidad para que las probabilidades sumen 1
    A_ub = np.ones((num_strategies_player1, num_strategies_player2))
    b_ub = [1] * num_strategies_player2

    # Resolver el problema de programación lineal para encontrar el equilibrio
    result_player1 = linprog(c1, A_ub=A_ub, b_ub=b_ub, bounds=[(0, 1)] * num_strategies_player1)
    result_player2 = linprog(c2, A_ub=A_ub, b_ub=b_ub, bounds=[(0, 1)] * num_strategies_player2)

    return result_player1.x, result_player2.x


# ----------------------------
# Ejemplo de uso
# ----------------------------
if __name__ == "__main__":
    # Matrices de pago para los jugadores
    payoff_matrix_player1 = np.array([[3, 0], [5, 1]])  # Jugador 1
    payoff_matrix_player2 = np.array([[3, 5], [0, 1]])  # Jugador 2

    eq_player1, eq_player2 = nash_equilibrium(payoff_matrix_player1, payoff_matrix_player2)

    print(f"Equilibrio de Nash para Jugador 1: {eq_player1}")
    print(f"Equilibrio de Nash para Jugador 2: {eq_player2}")
#     # Mostramos los resultados        
#     print(f"Equilibrio de Nash para Jugador 1: {eq_player1}")
#     print(f"Equilibrio de Nash para Jugador 2: {eq_player2}")