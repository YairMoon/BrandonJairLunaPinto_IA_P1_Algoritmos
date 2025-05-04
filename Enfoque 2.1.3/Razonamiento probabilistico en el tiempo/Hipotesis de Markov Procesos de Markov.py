import numpy as np

# Definimos los estados
estados = ['A', 'B', 'C']

# Matriz de transición: P(nuevo_estado | estado_actual)
# Las filas representan el estado actual, columnas el nuevo estado
#       A     B     C
T = [[0.1, 0.6, 0.3],   # desde A
     [0.4, 0.4, 0.2],   # desde B
     [0.3, 0.3, 0.4]]   # desde C

# Simulamos una cadena de Markov
def proceso_de_markov(estado_inicial='A', pasos=20):
    secuencia = [estado_inicial]
    estado_actual = estados.index(estado_inicial)

    for _ in range(pasos):
        siguiente_estado = np.random.choice(estados, p=T[estado_actual])
        secuencia.append(siguiente_estado)
        estado_actual = estados.index(siguiente_estado)

    return secuencia

# Ejecutamos
secuencia = proceso_de_markov()
print("Cadena de estados:", secuencia)
