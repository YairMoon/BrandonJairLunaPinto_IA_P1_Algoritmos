import random

# -------------------------------
# Definición del HMM
# -------------------------------

# Estados ocultos posibles
estados = ['Lluvia', 'Soleado']

# Observaciones posibles
observaciones_posibles = ['Caminar', 'Comprar', 'Limpiar']

# Probabilidad inicial de los estados
P_inicial = {
    'Lluvia': 0.6,
    'Soleado': 0.4
}

# Matriz de transición entre estados
transiciones = {
    'Lluvia': {'Lluvia': 0.7, 'Soleado': 0.3},
    'Soleado': {'Lluvia': 0.4, 'Soleado': 0.6}
}

# Probabilidades de emisión (observaciones)
emisiones = {
    'Lluvia': {'Caminar': 0.1, 'Comprar': 0.4, 'Limpiar': 0.5},
    'Soleado': {'Caminar': 0.6, 'Comprar': 0.3, 'Limpiar': 0.1}
}

# -------------------------------
# Generar una secuencia aleatoria de estados y observaciones
# -------------------------------

def generar_secuencia_hmm(longitud):
    secuencia_estados = []
    secuencia_observaciones = []

    # Elegimos estado inicial
    estado_actual = random.choices(estados, weights=[P_inicial[s] for s in estados])[0]
    secuencia_estados.append(estado_actual)

    # Generamos primera observación
    obs = random.choices(observaciones_posibles, weights=[emisiones[estado_actual][o] for o in observaciones_posibles])[0]
    secuencia_observaciones.append(obs)

    for _ in range(1, longitud):
        # Transición a siguiente estado
        estado_actual = random.choices(estados, weights=[transiciones[estado_actual][s] for s in estados])[0]
        secuencia_estados.append(estado_actual)

        # Emisión de observación basada en estado actual
        obs = random.choices(observaciones_posibles, weights=[emisiones[estado_actual][o] for o in observaciones_posibles])[0]
        secuencia_observaciones.append(obs)

    return secuencia_estados, secuencia_observaciones

# -------------------------------
# Ejemplo de uso
# -------------------------------

# Generamos una secuencia de 10 pasos
estados_generados, observaciones_generadas = generar_secuencia_hmm(10)

# Mostramos los resultados
print("Secuencia de estados ocultos:")
print(estados_generados)
print("\nSecuencia de observaciones:")
print(observaciones_generadas)
