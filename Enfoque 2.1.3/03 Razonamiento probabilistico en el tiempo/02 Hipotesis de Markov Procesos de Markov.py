import numpy as np
# Importamos NumPy para realizar cálculos numéricos, como la selección aleatoria basada en probabilidades.

# Definimos los estados
estados = ['A', 'B', 'C']
# Lista de estados posibles en el proceso de Markov.

# Matriz de transición: P(nuevo_estado | estado_actual)
# Las filas representan el estado actual, columnas el nuevo estado
#       A     B     C
T = [[0.1, 0.6, 0.3],   # desde A
     [0.4, 0.4, 0.2],   # desde B
     [0.3, 0.3, 0.4]]   # desde C
# Matriz de transición que define las probabilidades de moverse de un estado actual a un nuevo estado.

# Simulamos una cadena de Markov
def proceso_de_markov(estado_inicial='A', pasos=20):
    """
    Simula una cadena de Markov a partir de un estado inicial.

    :param estado_inicial: Estado inicial de la cadena (por defecto 'A').
    :param pasos: Número de pasos a simular.
    :return: Lista con la secuencia de estados visitados.
    """
    secuencia = [estado_inicial]
    # Inicializamos la secuencia con el estado inicial.

    estado_actual = estados.index(estado_inicial)
    # Obtenemos el índice del estado inicial en la lista de estados.

    for _ in range(pasos):
        # Seleccionamos el siguiente estado basado en las probabilidades de la matriz de transición.
        siguiente_estado = np.random.choice(estados, p=T[estado_actual])
        secuencia.append(siguiente_estado)
        # Añadimos el siguiente estado a la secuencia.

        estado_actual = estados.index(siguiente_estado)
        # Actualizamos el estado actual al índice del siguiente estado.

    return secuencia
    # Retornamos la secuencia completa de estados visitados.

# Ejecutamos
secuencia = proceso_de_markov()
# Simulamos una cadena de Markov con el estado inicial por defecto ('A') y 20 pasos.

print("Cadena de estados:", secuencia)
# Mostramos la secuencia de estados generada.