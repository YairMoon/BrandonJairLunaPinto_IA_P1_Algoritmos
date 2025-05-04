import numpy as np
import matplotlib.pyplot as plt

# Funciones de activación
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def tanh(x):
    return np.tanh(x)

def relu(x):
    return np.maximum(0, x)

# Generar valores para graficar
x = np.linspace(-10, 10, 100)

# Graficar funciones de activación
plt.plot(x, sigmoid(x), label='Sigmoide')
plt.plot(x, tanh(x), label='Tanh')
plt.plot(x, relu(x), label='ReLU')
plt.legend()
plt.title('Funciones de Activación')
plt.xlabel('Entrada')
plt.ylabel('Salida')
plt.grid(True)
plt.show()
