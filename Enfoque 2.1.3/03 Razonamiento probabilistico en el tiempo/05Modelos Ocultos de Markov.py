import random
# Importamos la biblioteca random para generar valores aleatorios.

# -------------------------------
# Definición del HMM
# -------------------------------

# Estados ocultos posibles
estados = ['Lluvia', 'Soleado']
# Lista de estados ocultos en el modelo.

# Observaciones posibles
observaciones_posibles = ['Caminar', 'Comprar', 'Limpiar']
# Lista de observaciones posibles que dependen de los estados ocultos.

# Probabilidad inicial de los estados
P_inicial = {
    'Lluvia': 0.6,
    'Soleado': 0.4
}
# Probabilidades iniciales de estar en cada estado oculto.

# Matriz de transición entre estados
transiciones = {
    'Lluvia': {'Lluvia': 0.7, 'Soleado': 0.3},
    'Soleado': {'Lluvia': 0.4, 'Soleado': 0.6}
}
# Matriz de transición que define las probabilidades de moverse de un estado oculto a otro.

# Probabilidades de emisión (observaciones)
emisiones = {
    'Lluvia': {'Caminar': 0.1, 'Comprar': 0.4, 'Limpiar': 0.5},
    'Soleado': {'Caminar': 0.6, 'Comprar': 0.3, 'Limpiar': 0.1}
}
# Probabilidades de observar un evento dado un estado oculto.

# -------------------------------
# Generar una secuencia aleatoria de estados y observaciones
# -------------------------------

def generar_secuencia_hmm(longitud):
    """
    Genera una secuencia de estados ocultos y observaciones para un HMM.

    :param longitud: Número de pasos en la secuencia.
    :return: Una tupla con la secuencia de estados ocultos y observaciones.
    """
    secuencia_estados = []
    secuencia_observaciones = []

    # Elegimos estado inicial
    estado_actual = random.choices(estados, weights=[P_inicial[s] for s in estados])[0]
    # Seleccionamos el estado inicial basado en las probabilidades iniciales.
    secuencia_estados.append(estado_actual)

    # Generamos primera observación
    obs = random.choices(observaciones_posibles, weights=[emisiones[estado_actual][o] for o in observaciones_posibles])[0]
    # Generamos la primera observación basada en el estado inicial.
    secuencia_observaciones.append(obs)

    for _ in range(1, longitud):
        # Transición a siguiente estado
        estado_actual = random.choices(estados, weights=[transiciones[estado_actual][s] for s in estados])[0]
        # Seleccionamos el siguiente estado basado en la matriz de transición.
        secuencia_estados.append(estado_actual)

        # Emisión de observación basada en estado actual
        obs = random.choices(observaciones_posibles, weights=[emisiones[estado_actual][o] for o in observaciones_posibles])[0]
        # Generamos una observación basada en el estado actual.
        secuencia_observaciones.append(obs)

    return secuencia_estados, secuencia_observaciones
    # Retornamos la secuencia de estados ocultos y observaciones.

# -------------------------------
# Ejemplo de uso
# -------------------------------

# Generamos una secuencia de 10 pasos
estados_generados, observaciones_generadas = generar_secuencia_hmm(10)
# Simulamos una secuencia de 10 pasos en el HMM.

# Mostramos los resultados
print("Secuencia de estados ocultos:")
print(estados_generados)
# Mostramos la secuencia de estados ocultos generada.

print("\nSecuencia de observaciones:")
print(observaciones_generadas)
# Mostramos la secuencia de observaciones generada.