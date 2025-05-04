from itertools import product

# Variables booleanas: True o False
# Definimos las probabilidades condicionales y marginales

# P(lluvia)
P_lluvia = {True: 0.2, False: 0.8}

# P(sprinkler | lluvia)
P_sprinkler = {
    True: {True: 0.01, False: 0.99},
    False: {True: 0.4, False: 0.6}
}

# P(mojado | lluvia, sprinkler)
P_mojado = {
    (True, True): {True: 0.99, False: 0.01},
    (True, False): {True: 0.8, False: 0.2},
    (False, True): {True: 0.9, False: 0.1},
    (False, False): {True: 0.0, False: 1.0}
}

# Objetivo: P(lluvia | mojado=True)

def enumerar_ponderado():
    total = 0.0
    lluvia_true = 0.0

    # Enumeramos todos los valores posibles de sprinkler y lluvia
    for lluvia_val, sprinkler_val in product([True, False], repeat=2):
        # P(lluvia) * P(sprinkler|lluvia) * P(mojado=True|lluvia, sprinkler)
        p = (
            P_lluvia[lluvia_val] *
            P_sprinkler[lluvia_val][sprinkler_val] *
            P_mojado[(lluvia_val, sprinkler_val)][True]
        )
        total += p
        if lluvia_val:
            lluvia_true += p

    # Normalizamos
    return lluvia_true / total

# Ejecutamos la inferencia
resultado = enumerar_ponderado()
print(f"P(lluvia = True | mojado = True) = {resultado:.4f}")
# Resultado esperado: 0.2