import numpy as np
import matplotlib.pyplot as plt
# Importamos las bibliotecas necesarias para cálculos numéricos y visualización.

# Definición de la función de activación (sigmoide)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
# La función sigmoide transforma cualquier valor en un rango entre 0 y 1.

# Definición de la derivada de la sigmoide (para retropropagación)
def sigmoid_deriv(x):
    return x * (1 - x)
# La derivada de la sigmoide se utiliza para calcular los ajustes durante el entrenamiento.

# Parámetros de entrada
entradas = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # AND
salidas = np.array([[0], [0], [0], [1]])
# Definimos las entradas y salidas esperadas para la operación lógica AND.

# Inicialización de pesos y bias
np.random.seed(42)
pesos = np.random.rand(2, 1)  # Pesos aleatorios
bias = np.random.rand(1)  # Bias aleatorio
# Inicializamos los pesos y el bias con valores aleatorios.

# Tasa de aprendizaje
tasa_aprendizaje = 0.1
# Definimos la tasa de aprendizaje para ajustar los pesos y el bias.

# Entrenamiento (entrenamiento simple de una neurona)
for epoch in range(10000):
    # Cálculo de la salida
    entrada_suma = np.dot(entradas, pesos) + bias
    salida_pred = sigmoid(entrada_suma)
    # Calculamos la salida de la neurona aplicando la función sigmoide.

    # Cálculo del error
    error = salidas - salida_pred
    # Calculamos la diferencia entre la salida esperada y la predicción.

    # Retropropagación
    d_error = error * sigmoid_deriv(salida_pred)
    pesos += tasa_aprendizaje * np.dot(entradas.T, d_error)
    bias += tasa_aprendizaje * np.sum(d_error)
    # Ajustamos los pesos y el bias utilizando la derivada del error.

# Predicción final
predicciones = sigmoid(np.dot(entradas, pesos) + bias)
# Calculamos las predicciones finales después del entrenamiento.

# Mostrar resultados
print("Resultados de predicción después de entrenamiento:")
print(predicciones)
# Mostramos las predicciones finales para las entradas dadas.