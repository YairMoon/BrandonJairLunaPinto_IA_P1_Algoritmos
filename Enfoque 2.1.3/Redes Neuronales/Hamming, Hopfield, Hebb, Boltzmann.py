import numpy as np

# Función de activación de Heaviside (umbral)
def heaviside(x):
    return np.where(x >= 0, 1, -1)

# Red de Hopfield
class RedHopfield:
    def __init__(self, n_neuronas):
        self.n_neuronas = n_neuronas
        self.pesos = np.zeros((n_neuronas, n_neuronas))  # Inicialización de pesos

    def entrenar(self, patrones):
        # Algoritmo de aprendizaje de Hopfield (Hebb)
        for p in patrones:
            self.pesos += np.outer(p, p)
        np.fill_diagonal(self.pesos, 0)  # No hay conexiones consigo misma

    def recordar(self, entrada):
        # Propagación de la red
        salida = entrada.copy()
        for _ in range(10):  # Iterar varias veces
            salida = heaviside(np.dot(self.pesos, salida))  # Actualización de las neuronas
        return salida

# Patrones de entrenamiento (memoria)
patrones = np.array([[1, -1, 1], [-1, 1, -1]])

# Crear e entrenar la red de Hopfield
hopfield = RedHopfield(n_neuronas=3)
hopfield.entrenar(patrones)

# Recordar un patrón perturbado
entrada_perturbada = np.array([1, -1, -1])  # Un patrón de entrada ruidoso
recuerdo = hopfield.recordar(entrada_perturbada)

# Mostrar resultados
print("Patrón Recordado:", recuerdo)
