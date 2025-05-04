import numpy as np
import matplotlib.pyplot as plt

# Generación de datos separables lineales
np.random.seed(42)
X = np.random.randn(100, 2)  # 100 puntos en 2D
y = (X[:, 0] + X[:, 1] > 0).astype(int)  # Clase 0 si x0 + x1 <= 0, clase 1 si x0 + x1 > 0

# Graficar los puntos
plt.scatter(X[y==0][:, 0], X[y==0][:, 1], color='red', label='Clase 0')
plt.scatter(X[y==1][:, 0], X[y==1][:, 1], color='blue', label='Clase 1')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.title('Datos Separables Lineales')
plt.legend()
plt.grid(True)
plt.show()
