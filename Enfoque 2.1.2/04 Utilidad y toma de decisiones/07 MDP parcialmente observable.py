# MDP Parcialmente Observable (POMDP) - Resolución de un POMDP simple

def pomdp_value_iteration(states, actions, transition_model, reward, observation_model, gamma=0.9, epsilon=0.01): 
    """
    Implementa el algoritmo de Iteración de Valores para un MDP Parcialmente Observable (POMDP).
    
    :param states: Lista de estados posibles.
    :param actions: Lista de acciones posibles.
    :param transition_model: Modelo de transiciones, un diccionario[state][action] = lista de (next_state, probabilidad).
    :param reward: Función de recompensa que toma (estado, acción, siguiente_estado) y retorna una recompensa.
    :param observation_model: Modelo de observaciones, un diccionario[state][action] = lista de (observación, probabilidad).
    :param gamma: Factor de descuento (valor entre 0 y 1).
    :param epsilon: Umbral para determinar la convergencia.
    :return: Diccionario con los valores de los estados.
    """
    # Inicializamos los valores de los estados
    V = {s: 0 for s in states}

    while True:
        delta = 0  # Diferencia máxima entre los valores anteriores y nuevos
        new_V = V.copy()  # Copia de los valores actuales para actualizarlos

        # Iteramos sobre cada estado
        for s in states:
            max_value = float('-inf')  # Inicializamos el valor máximo para el estado

            for a in actions:
                expected_value = 0  # Valor esperado para la acción

                # Calculamos el valor esperado basado en el modelo de transiciones
                for (next_state, prob) in transition_model[s][a]:
                    expected_value += prob * (reward(s, a, next_state) + gamma * V[next_state])

                # Incorporamos el modelo de observaciones
                for observation, prob in observation_model[s][a]:
                    expected_value += prob * V[next_state]

                # Actualizamos el valor máximo para el estado
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

    # Modelo de observaciones: diccionario[state][action] = lista de (observación, probabilidad)
    observation_model = {
        'A': {
            'ir_A': [('A', 0.9), ('B', 0.1)],
            'ir_B': [('A', 0.2), ('B', 0.8)],
        },
        'B': {
            'ir_A': [('A', 0.1), ('B', 0.9)],
            'ir_B': [('A', 0.8), ('B', 0.2)],
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

    # Ejecutamos la iteración de valores para el POMDP
    V = pomdp_value_iteration(states, actions, transition_model, reward, observation_model)

    # Mostramos los valores finales de cada estado
    for state, value in V.items():
        print(f"Valor de {state}: {value:.2f}")  # Mostramos el valor de cada estado con dos decimales
# Este código implementa un algoritmo de Iteración de Valores para un MDP Parcialmente Observable (POMDP).