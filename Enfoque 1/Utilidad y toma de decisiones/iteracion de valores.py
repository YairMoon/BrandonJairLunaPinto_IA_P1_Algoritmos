# Algoritmo de Iteración de Valores para resolver un MDP

def value_iteration(states, actions, transition_model, reward, gamma=0.9, epsilon=0.01):
    # Inicializamos los valores de cada estado en 0
    V = {s: 0 for s in states}

    # Bucle principal: continúa hasta que el cambio sea menor que epsilon
    while True:
        delta = 0  # Para verificar cuánto cambió el valor más grande
        new_V = {}  # Almacenamos los nuevos valores calculados

        # Recorremos cada estado del espacio
        for s in states:
            # Calculamos el valor máximo esperado de todas las acciones desde ese estado
            max_value = float('-inf')  # Inicializamos con un valor muy bajo

            for a in actions:
                # Calculamos el valor esperado de tomar acción 'a' en estado 's'
                expected_value = 0

                for (next_state, prob) in transition_model[s][a]:
                    # Sumamos la recompensa inmediata + valor futuro esperado
                    expected_value += prob * (reward(s, a, next_state) + gamma * V[next_state])

                # Nos quedamos con el valor máximo entre acciones
                max_value = max(max_value, expected_value)

            new_V[s] = max_value  # Actualizamos el nuevo valor del estado
            delta = max(delta, abs(V[s] - new_V[s]))  # Vemos cuánto cambió

        V = new_V  # Reemplazamos los valores antiguos por los nuevos

        # Si el cambio es menor al umbral, terminamos
        if delta < epsilon:
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
            return 10  # premio por ir a B
        elif s == 'B' and s1 == 'A':
            return -1  # castigo por volver a A
        else:
            return 0  # sin cambio

    # Ejecutamos la iteración de valores
    V = value_iteration(states, actions, transition_model, reward)

    # Mostramos los valores finales de cada estado
    for state, value in V.items():
        print(f"Valor de {state}: {value:.2f}")
