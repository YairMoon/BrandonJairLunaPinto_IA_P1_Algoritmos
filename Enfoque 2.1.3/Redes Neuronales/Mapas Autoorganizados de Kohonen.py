import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

# Generar datos de ejemplo (blobs)
X, y = make_blobs(n_samples=100, centers=3, random_state=42)

# Función para calcular la distancia euclidiana
def distancia_euclidiana(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))

# Mapa de Kohonen
class MapaKohonen:
    def __init__(self, n_filas, n_columnas, n_features, lr=0.1, epochs=100):
        self.n_filas = n_filas
        self.n_columnas = n_columnas
        self.lr = lr
        self.epochs = epochs
        self.mapa = np.random.rand(n_filas, n_columnas, n_features)

    def entrenar(self, X):
        for epoch in range(self.epochs):
            for x in X:
                # Calcular distancias de cada nodo
                distancias = np.linalg.norm(self.mapa - x, axis=2)
                ganador = np.unravel_index(np.argmin(distancias), distancias.shape)

                # Actualizar el nodo ganador y sus vecinos
                for i in range(self.n_filas):
                    for j in range(self.n_columnas):
                        distancia_vecino = np.linalg.norm(np.array([i, j]) - np.array(ganador))
                        if distancia_vecino < 2:
                            self.mapa[i, j] += self.lr * (x - self.mapa[i, j])

    def visualizar_mapa(self):
        plt.imshow(np.mean(self.mapa, axis=2), cmap='coolwarm')
        plt.colorbar()
        plt.title("Mapa Autoorganizado de Kohonen")
        plt.show()

# Crear e entrenar el mapa de Kohonen
kohonen = MapaKohonen(10, 10, X.shape[1], epochs=100)
kohonen.entrenar(X)

# Visualizar el mapa
kohonen.visualizar_mapa()
