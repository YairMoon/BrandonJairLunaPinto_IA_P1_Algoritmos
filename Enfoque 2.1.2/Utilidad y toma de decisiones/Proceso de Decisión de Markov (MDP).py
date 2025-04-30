# Proceso de Decisión de Markov (MDP) - Solución por Iteración de Valores

def mdp_value_iteration(states, actions, transition_model, reward, gamma=0.9, epsilon=0.01):
    # Inicializamos los valores de los estados en 0
    V = {s: 0 for s in states}

    while True:
        delta = 0
        new_V = V.copy()

        # Iteramos sobre cada estado
        for s in states:
            max_value = float('-inf')

            # Iteramos sobre todas las acciones
            for a in actions:
                expected_value = 0
                for (next_state, prob) in transition_model[s][a]:
                    expected_value += prob * (reward(s, a, next_state) + gamma * V[next_state])

                # Tomamos la acción que maximiza el valor esperado
                max_value = max(max_value, expected_value)

            new_V[s] = max_value
            delta = max(delta, abs(V[s] - new_V[s]))

        V = new_V

        if delta < epsilon:
            break

    return V


# ----------------------------
# Ejemplo de uso
# ----------------------------
if __name__ == "__main__":
    states = ['A', 'B']
    actions = ['ir_A', 'ir_B']
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

    def reward(s, a, s1):
        if s == 'A' and s1 == 'B':
            return 10
        elif s == 'B' and s1 == 'A':
            return -1
        else:
            return 0

    V = mdp_value_iteration(states, actions, transition_model, reward)

    for state, value in V.items():
        print(f"Valor de {state}: {value:.2f}")
# Proceso de Decisión de Markov (MDP) - Solución por Iteración de Políticas