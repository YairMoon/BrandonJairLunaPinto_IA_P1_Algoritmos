# MDP Parcialmente Observable (POMDP) - Resolución de un POMDP simple

def pomdp_value_iteration(states, actions, transition_model, reward, observation_model, gamma=0.9, epsilon=0.01):
    # Inicializamos los valores de los estados
    V = {s: 0 for s in states}

    while True:
        delta = 0
        new_V = V.copy()

        # Iteramos sobre cada estado
        for s in states:
            max_value = float('-inf')

            for a in actions:
                expected_value = 0
                for (next_state, prob) in transition_model[s][a]:
                    expected_value += prob * (reward(s, a, next_state) + gamma * V[next_state])

                # Para cada acción, calculamos la observación
                for observation, prob in observation_model[s][a]:
                    expected_value += prob * V[next_state]

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

    def reward(s, a, s1):
        if s == 'A' and s1 == 'B':
            return 10
        elif s == 'B' and s1 == 'A':
            return -1
        else:
            return 0

    V = pomdp_value_iteration(states, actions, transition_model, reward, observation_model)

    for state, value in V.items():
        print(f"Valor de {state}: {value:.2f}")
#     # Mostramos los valores finales de cada estado
#     for state, value in V.items():