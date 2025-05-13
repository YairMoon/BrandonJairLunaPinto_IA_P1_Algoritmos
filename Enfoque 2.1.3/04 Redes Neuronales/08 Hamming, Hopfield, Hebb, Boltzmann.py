import numpy as np
# Importamos NumPy para realizar cálculos matriciales y operaciones con vectores.

# Función de activación de Heaviside (umbral)
def heaviside(x):
    return np.where(x >= 0, 1, -1)
# La función de activación Heaviside devuelve 1 si el valor es mayor o igual a 0, y -1 en caso contrario.

# Red de Hopfield
class RedHopfield:
    def __init__(self, n_neuronas):
        self.n_neuronas = n_neuronas
        self.pesos = np.zeros((n_neuronas, n_neuronas))  # Inicialización de pesos
        # Creamos una matriz de pesos inicializada en ceros.

    def entrenar(self, patrones):
        # Algoritmo de aprendizaje de Hopfield (Hebb)
        for p in patrones:
            self.pesos += np.outer(p, p)
            # Actualizamos los pesos utilizando la regla de Hebb: w_ij += p_i * p_j.
        np.fill_diagonal(self.pesos, 0)  # No hay conexiones consigo misma
        # Establecemos los pesos en la diagonal a 0 para evitar conexiones de una neurona consigo misma.

    def recordar(self, entrada):
        # Propagación de la red
        salida = entrada.copy()
        # Copiamos la entrada para no modificarla directamente.
        for _ in range(10):  # Iterar varias veces
            salida = heaviside(np.dot(self.pesos, salida))  # Actualización de las neuronas
            # Calculamos la salida aplicando la función de activación Heaviside.
        return salida
        # Retornamos el patrón recordado.

# Patrones de entrenamiento (memoria)
patrones = np.array([[1, -1, 1], [-1, 1, -1]])
# Definimos los patrones que la red debe memorizar.

# Crear y entrenar la red de Hopfield
hopfield = RedHopfield(n_neuronas=3)
# Creamos una red de Hopfield con 3 neuronas.

hopfield.entrenar(patrones)
# Entrenamos la red con los patrones definidos.

# Recordar un patrón perturbado
entrada_perturbada = np.array([1, -1, -1])  # Un patrón de entrada ruidoso
recuerdo = hopfield.recordar(entrada_perturbada)
# La red intenta recordar el patrón más cercano al patrón perturbado.

# Mostrar resultados
print("Patrón Recordado:", recuerdo)
# Mostramos el patrón recordado por la red.