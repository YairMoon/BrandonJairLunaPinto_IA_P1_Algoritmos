from sklearn.neural_network import MLPClassifier
import numpy as np
import matplotlib.pyplot as plt
# Importamos las bibliotecas necesarias para crear y entrenar una red neuronal multicapa, y para visualizar los resultados.

# Datos de entrenamiento (función XOR)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 0])
# Definimos las entradas y salidas esperadas para la operación lógica XOR.

# Red Neuronal Multicapa (MLP)
mlp = MLPClassifier(hidden_layer_sizes=(3,), max_iter=1000, activation='relu', solver='adam')
# Creamos un clasificador de red neuronal multicapa con:
# - Una capa oculta de 3 neuronas.
# - Un máximo de 1000 iteraciones para el entrenamiento.
# - Función de activación ReLU.
# - Optimizador Adam.

mlp.fit(X, y)
# Entrenamos la red neuronal con los datos de entrada (X) y las salidas esperadas (y).

# Predicción
predicciones = mlp.predict(X)
# Realizamos predicciones para las entradas de entrenamiento.

# Resultados
print("Predicciones:", predicciones)
# Mostramos las predicciones realizadas por la red neuronal.

# Mostrar gráfico de frontera de decisión
xx, yy = np.meshgrid(np.linspace(-0.1, 1.1, 100), np.linspace(-0.1, 1.1, 100))
# Creamos una malla de puntos para visualizar la frontera de decisión.

Z = mlp.predict(np.c_[xx.ravel(), yy.ravel()])
# Realizamos predicciones para cada punto de la malla.

Z = Z.reshape(xx.shape)
# Damos forma a las predicciones para que coincidan con la malla.

plt.contourf(xx, yy, Z, alpha=0.8)
# Dibujamos la frontera de decisión como un mapa de colores.

plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', marker='o')
# Dibujamos los puntos de datos de entrada con sus respectivas etiquetas.

plt.title('Red Neuronal Multicapa')
# Añadimos un título al gráfico.

plt.show()
# Mostramos el gráfico.
