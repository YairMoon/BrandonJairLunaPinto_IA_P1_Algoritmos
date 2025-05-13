from itertools import product # Importamos product para generar todas las combinaciones posibles de valores booleanos.
# Importamos product para generar todas las combinaciones posibles de valores booleanos.

# Variables booleanas: True o False
# Definimos las probabilidades condicionales y marginales

# P(lluvia)
P_lluvia = {True: 0.2, False: 0.8} ## Probabilidad de que llueva o no.
# Probabilidad marginal de que llueva o no.

# P(sprinkler | lluvia)
P_sprinkler = {
    True: {True: 0.01, False: 0.99},  # Si llueve: probabilidad de que el aspersor esté encendido o apagado.
    False: {True: 0.4, False: 0.6}    # Si no llueve: probabilidad de que el aspersor esté encendido o apagado.
}

# P(mojado | lluvia, sprinkler)
P_mojado = {
    (True, True): {True: 0.99, False: 0.01},  # Si llueve y el aspersor está encendido.
    (True, False): {True: 0.8, False: 0.2},   # Si llueve y el aspersor está apagado.
    (False, True): {True: 0.9, False: 0.1},   # Si no llueve y el aspersor está encendido.
    (False, False): {True: 0.0, False: 1.0}   # Si no llueve y el aspersor está apagado.
}

# Objetivo: P(lluvia | mojado=True)

def enumerar_ponderado(): ## Definimos la función para realizar inferencia por enumeración.
    """
    Realiza inferencia por enumeración para calcular P(lluvia=True | mojado=True).
    """
    total = 0.0  # Suma total de probabilidades.
    lluvia_true = 0.0  # Suma de probabilidades donde lluvia=True.

    # Enumeramos todos los valores posibles de sprinkler y lluvia
    for lluvia_val, sprinkler_val in product([True, False], repeat=2):
        # P(lluvia) * P(sprinkler|lluvia) * P(mojado=True|lluvia, sprinkler)
        p = (
            P_lluvia[lluvia_val] *
            P_sprinkler[lluvia_val][sprinkler_val] *
            P_mojado[(lluvia_val, sprinkler_val)][True]
        )
        # Calculamos la probabilidad conjunta para cada combinación de valores.

        total += p  # Acumulamos la probabilidad total.
        if lluvia_val:
            lluvia_true += p  # Acumulamos la probabilidad donde lluvia=True.

    # Normalizamos
    return lluvia_true / total
    # Retornamos la probabilidad condicional normalizada.

# Ejecutamos la inferencia
resultado = enumerar_ponderado() # Llamamos a la función para realizar la inferencia.
print(f"P(lluvia = True | mojado = True) = {resultado:.4f}") ## Mostramos el resultado de la inferencia con 4 decimales.
# Mostramos el resultado de la inferencia.