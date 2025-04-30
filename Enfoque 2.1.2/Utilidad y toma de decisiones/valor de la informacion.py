# Valor de la Información - Utilidad esperada y cálculo del valor de la información.

# 1. Calculamos la utilidad esperada dada una lista de acciones, probabilidades y utilidades.
def expected_utility(actions, probabilities, utilities):
    """
    Calcula la utilidad esperada dada una lista de acciones posibles,
    un diccionario de probabilidades de cada acción y un diccionario de utilidades asociadas a cada acción.
    
    actions: lista de acciones posibles
    probabilities: diccionario con probabilidades de cada acción
    utilities: diccionario con las utilidades asociadas a cada acción
    """
    expected_value = 0
    # Calculamos la utilidad esperada sumando (probabilidad * utilidad)
    for action in actions:
        expected_value += probabilities[action] * utilities[action]
    
    return expected_value


# 2. Calculamos el valor de la información. 
def value_of_information(actions, probabilities, utilities, with_info_utilities):
    """
    Calcula el valor de la información como la diferencia entre la utilidad esperada
    cuando se tiene información y la utilidad esperada sin información.
    
    actions: lista de acciones posibles
    probabilities: diccionario con probabilidades de cada acción
    utilities: diccionario con las utilidades asociadas a cada acción sin información
    with_info_utilities: diccionario con las utilidades asociadas a cada acción con información
    """
    # Utilidad esperada sin información
    expected_utility_without_info = expected_utility(actions, probabilities, utilities)
    
    # Utilidad esperada con información
    expected_utility_with_info = expected_utility(actions, probabilities, with_info_utilities)
    
    # El valor de la información es la diferencia entre ambas utilidades esperadas
    return expected_utility_with_info - expected_utility_without_info


# ----------------------------
# Ejemplo de uso
# ----------------------------
if __name__ == "__main__":
    # Definimos las acciones posibles
    actions = ['A', 'B', 'C']

    # Probabilidades de cada acción
    probabilities = {
        'A': 0.4,
        'B': 0.3,
        'C': 0.3
    }

    # Utilidades sin información
    utilities = {
        'A': 50,
        'B': 30,
        'C': 10
    }

    # Utilidades con información
    with_info_utilities = {
        'A': 60,  # Después de obtener información, la utilidad de A mejora
        'B': 40,  # La utilidad de B también mejora
        'C': 20   # La utilidad de C mejora
    }

    # Calculamos la utilidad esperada sin información
    expected_value_no_info = expected_utility(actions, probabilities, utilities)
    print(f"Utilidad esperada sin información: {expected_value_no_info:.2f}")

    # Calculamos la utilidad esperada con información
    expected_value_with_info = expected_utility(actions, probabilities, with_info_utilities)
    print(f"Utilidad esperada con información: {expected_value_with_info:.2f}")

    # Calculamos el valor de la información
    value_info = value_of_information(actions, probabilities, utilities, with_info_utilities)
    print(f"Valor de la información: {value_info:.2f}")
