# Algoritmo de Iteración de Políticas para resolver un MDP

def policy_iteration(states, actions, transition_model, reward, gamma=0.9, epsilon=0.01): # Iteración de Políticas
    """
    Implementa el algoritmo de Iteración de Políticas para resolver un Proceso de Decisión de Markov (MDP).
    
    :param states: Lista de estados posibles.
    :param actions: Lista de acciones posibles.
    :param transition_model: Modelo de transiciones, un diccionario[state][action] = lista de (next_state, probabilidad).
    :param reward: Función de recompensa que toma (estado, acción, siguiente_estado) y retorna una recompensa.
    :param gamma: Factor de descuento (valor entre 0 y 1).
    :param epsilon: Umbral para determinar la convergencia en la evaluación de políticas.
    :return: Una tupla con la política óptima y los valores de los estados.
    """
    # Inicializamos la política (al azar) y los valores de los estados
    policy = {s: actions[0] for s in states}  # Política inicial: asignamos la primera acción a todos los estados
    V = {s: 0 for s in states}  # Valores de los estados inicializados a 0

    while True:
        # Paso 1: Evaluación de la política
        while True:
            delta = 0  # Diferencia máxima entre los valores anteriores y nuevos
            new_V = V.copy()

            for s in states:
                # Calculamos el valor de un estado usando la política actual
                action = policy[s]
                expected_value = 0

                for (next_state, prob) in transition_model[s][action]:
                    # Calculamos el valor esperado para el estado siguiente
                    expected_value += prob * (reward(s, action, next_state) + gamma * V[next_state])

                new_V[s] = expected_value  # Actualizamos el valor del estado
                delta = max(delta, abs(V[s] - new_V[s]))  # Verificamos el cambio máximo

            V = new_V  # Actualizamos los valores de los estados

            if delta < epsilon:  # Si el cambio es muy pequeño, terminamos la evaluación
                break

        # Paso 2: Mejora de la política
        policy_stable = True

        for s in states:
            old_action = policy[s]
            best_action = None
            max_value = float('-inf')

            # Recalculamos la mejor acción para cada estado
            for a in actions:
                expected_value = 0
                for (next_state, prob) in transition_model[s][a]:
                    expected_value += prob * (reward(s, a, next_state) + gamma * V[next_state])

                # Seleccionamos la acción con el valor esperado más alto
                if expected_value > max_value:
                    max_value = expected_value
                    best_action = a

            policy[s] = best_action  # Actualizamos la política

            if old_action != best_action:
                policy_stable = False  # Si hubo un cambio, la política no es estable

        if policy_stable:  # Si la política no cambió, hemos encontrado la política óptima
            break

    return policy, V


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
            return 10  # premio por ir a B
        elif s == 'B' and s1 == 'A':
            return -1  # castigo por volver a A
        else:
            return 0  # sin cambio

    # Ejecutamos la iteración de políticas
    policy, V = policy_iteration(states, actions, transition_model, reward)

    # Mostramos la política final y los valores de cada estado
    print("Política final:")
    for state, action in policy.items():
        print(f"Estado {state}: Acción {action}")

    print("\nValores de los estados:")
    for state, value in V.items():
        print(f"Valor de {state}: {value:.2f}")