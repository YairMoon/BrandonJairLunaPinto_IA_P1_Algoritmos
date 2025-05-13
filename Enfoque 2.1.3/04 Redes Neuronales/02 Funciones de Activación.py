import numpy as np
import matplotlib.pyplot as plt
# Importamos las bibliotecas necesarias para cálculos numéricos y visualización.

# Funciones de activación
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
# La función sigmoide transforma cualquier valor en un rango entre 0 y 1.

def tanh(x):
    return np.tanh(x)
# La función tangente hiperbólica transforma valores en un rango entre -1 y 1.

def relu(x):
    return np.maximum(0, x)
# La función ReLU (Rectified Linear Unit) devuelve 0 para valores negativos y el valor original para valores positivos.

# Generar valores para graficar
x = np.linspace(-10, 10, 100)
# Generamos un rango de valores entre -10 y 10 para graficar las funciones de activación.

# Graficar funciones de activación
plt.plot(x, sigmoid(x), label='Sigmoide')
# Graficamos la función sigmoide.

plt.plot(x, tanh(x), label='Tanh')
# Graficamos la función tangente hiperbólica.

plt.plot(x, relu(x), label='ReLU')
# Graficamos la función ReLU.

plt.legend()
# Añadimos una leyenda para identificar cada función.

plt.title('Funciones de Activación')
# Añadimos un título a la gráfica.

plt.xlabel('Entrada')
# Etiquetamos el eje X como "Entrada".

plt.ylabel('Salida')
# Etiquetamos el eje Y como "Salida".

plt.grid(True)
# Añadimos una cuadrícula para facilitar la visualización.

plt.show()
# Mostramos la gráfica.