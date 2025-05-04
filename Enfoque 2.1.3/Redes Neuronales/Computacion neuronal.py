import numpy as np
import matplotlib.pyplot as plt

# Definición de la función de activación (sigmoide)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Definición de la derivada de la sigmoide (para retropropagación)
def sigmoid_deriv(x):
    return x * (1 - x)

# Parámetros de entrada
entradas = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # AND
salidas = np.array([[0], [0], [0], [1]])

# Inicialización de pesos y bias
np.random.seed(42)
pesos = np.random.rand(2, 1)  # Pesos aleatorios
bias = np.random.rand(1)  # Bias aleatorio

# Tasa de aprendizaje
tasa_aprendizaje = 0.1

# Entrenamiento (entrenamiento simple de una neurona)
for epoch in range(10000):
    # Cálculo de la salida
    entrada_suma = np.dot(entradas, pesos) + bias
    salida_pred = sigmoid(entrada_suma)

    # Cálculo del error
    error = salidas - salida_pred

    # Retropropagación
    d_error = error * sigmoid_deriv(salida_pred)
    pesos += tasa_aprendizaje * np.dot(entradas.T, d_error)
    bias += tasa_aprendizaje * np.sum(d_error)

# Predicción final
predicciones = sigmoid(np.dot(entradas, pesos) + bias)

# Mostrar resultados
print("Resultados de predicción después de entrenamiento:")
print(predicciones)
