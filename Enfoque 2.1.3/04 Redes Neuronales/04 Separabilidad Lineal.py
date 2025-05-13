import numpy as np
import matplotlib.pyplot as plt
# Importamos las bibliotecas necesarias para cálculos numéricos y visualización.

# Generación de datos separables lineales
np.random.seed(42)
# Fijamos una semilla para reproducibilidad de los datos generados.

X = np.random.randn(100, 2)  # 100 puntos en 2D
# Generamos 100 puntos aleatorios en un espacio bidimensional siguiendo una distribución normal.

y = (X[:, 0] + X[:, 1] > 0).astype(int)
# Asignamos una clase a cada punto:
# - Clase 0 si la suma de las coordenadas (x0 + x1) es menor o igual a 0.
# - Clase 1 si la suma de las coordenadas (x0 + x1) es mayor a 0.

# Graficar los puntos
plt.scatter(X[y==0][:, 0], X[y==0][:, 1], color='red', label='Clase 0')
# Graficamos los puntos de la clase 0 en color rojo.

plt.scatter(X[y==1][:, 0], X[y==1][:, 1], color='blue', label='Clase 1')
# Graficamos los puntos de la clase 1 en color azul.

plt.axhline(0, color='black', linewidth=0.5)
# Dibujamos una línea horizontal en y=0 para referencia.

plt.axvline(0, color='black', linewidth=0.5)
# Dibujamos una línea vertical en x=0 para referencia.

plt.title('Datos Separables Lineales')
# Añadimos un título a la gráfica.

plt.legend()
# Añadimos una leyenda para identificar las clases.

plt.grid(True)
# Añadimos una cuadrícula para facilitar la visualización.

plt.show()
# Mostramos la gráfica.