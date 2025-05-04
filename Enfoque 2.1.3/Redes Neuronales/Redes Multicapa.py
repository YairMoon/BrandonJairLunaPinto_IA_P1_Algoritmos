from sklearn.neural_network import MLPClassifier
import numpy as np
import matplotlib.pyplot as plt

# Datos de entrenamiento (función XOR)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 0])

# Red Neuronal Multicapa (MLP)
mlp = MLPClassifier(hidden_layer_sizes=(3,), max_iter=1000, activation='relu', solver='adam')
mlp.fit(X, y)

# Predicción
predicciones = mlp.predict(X)

# Resultados
print("Predicciones:", predicciones)

# Mostrar gráfico de frontera de decisión
xx, yy = np.meshgrid(np.linspace(-0.1, 1.1, 100), np.linspace(-0.1, 1.1, 100))
Z = mlp.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.contourf(xx, yy, Z, alpha=0.8)
plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', marker='o')
plt.title('Red Neuronal Multicapa')
plt.show()
