# Proceso de Decisión de Markov (MDP) - Solución por Iteración de Valores

def mdp_value_iteration(states, actions, transition_model, reward, gamma=0.9, epsilon=0.01): # Iteración de Valores
    """
    Implementa el algoritmo de Iteración de Valores para resolver un Proceso de Decisión de Markov (MDP).
    
    :param states: Lista de estados posibles.
    :param actions: Lista de acciones posibles.
    :param transition_model: Modelo de transiciones, un diccionario[state][action] = lista de (next_state, probabilidad).
    :param reward: Función de recompensa que toma (estado, acción, siguiente_estado) y retorna una recompensa.
    :param gamma: Factor de descuento (valor entre 0 y 1).
    :param epsilon: Umbral para determinar la convergencia.
    :return: Diccionario con los valores de los estados.
    """
    # Inicializamos los valores de los estados en 0
    V = {s: 0 for s in states}

    while True:
        delta = 0  # Diferencia máxima entre los valores anteriores y nuevos
        new_V = V.copy()  # Copia de los valores actuales para actualizarlos

        # Iteramos sobre cada estado
        for s in states:
            max_value = float('-inf')  # Inicializamos el valor máximo para el estado

            # Iteramos sobre todas las acciones
            for a in actions:
                expected_value = 0  # Valor esperado para la acción

                # Calculamos el valor esperado basado en el modelo de transiciones
                for (next_state, prob) in transition_model[s][a]:
                    expected_value += prob * (reward(s, a, next_state) + gamma * V[next_state])

                # Tomamos la acción que maximiza el valor esperado
                max_value = max(max_value, expected_value)

            new_V[s] = max_value  # Actualizamos el valor del estado
            delta = max(delta, abs(V[s] - new_V[s]))  # Calculamos el cambio máximo

        V = new_V  # Actualizamos los valores de los estados

        if delta < epsilon:  # Si el cambio es menor al umbral, terminamos
            break

    return V


# ----------------------------
# Ejemplo de uso
# ----------------------------
if __name__ == "__main__":
    # Estados posibles
    states = ['A', 'B']

    # Acciones posibles
    actions = ['ir_A', 'ir_B']

    # Modelo de transiciones: diccionario[state][action] = lista de (next_state, probabilidad)
    transition_model = {
        'A': {
            'ir_A': [('A', 1.0)],
            'ir_B': [('B', 1.0)],
        },
        'B': {
            'ir_A': [('A', 1.0)],
            'ir_B': [('B', 1.0)],
        }
    }

    # Función de recompensa: recompensa por transición (s, a, s')
    def reward(s, a, s1):
        if s == 'A' and s1 == 'B':
            return 10  # Premio por ir a B
        elif s == 'B' and s1 == 'A':
            return -1  # Castigo por volver a A
        else:
            return 0  # Sin cambio

    # Ejecutamos la iteración de valores
    V = mdp_value_iteration(states, actions, transition_model, reward)

    # Mostramos los valores finales de cada estado
    for state, value in V.items():
        print(f"Valor de {state}: {value:.2f}")  # Mostramos el valor de cada estado con dos decimales
# Proceso de Decisión de Markov (MDP) - Solución por Iteración de Políticas