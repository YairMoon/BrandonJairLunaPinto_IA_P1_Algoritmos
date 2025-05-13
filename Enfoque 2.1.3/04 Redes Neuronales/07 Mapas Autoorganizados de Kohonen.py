import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
# Importamos las bibliotecas necesarias para cálculos numéricos, visualización y generación de datos.

# Generar datos de ejemplo (blobs)
X, y = make_blobs(n_samples=100, centers=3, random_state=42)
# Generamos un conjunto de datos con 3 centros (clústeres) para entrenar el mapa de Kohonen.

# Función para calcular la distancia euclidiana
def distancia_euclidiana(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))
# Calcula la distancia euclidiana entre dos puntos.

# Mapa de Kohonen
class MapaKohonen:
    def __init__(self, n_filas, n_columnas, n_features, lr=0.1, epochs=100):
        """
        Inicializa el mapa de Kohonen.

        :param n_filas: Número de filas en el mapa.
        :param n_columnas: Número de columnas en el mapa.
        :param n_features: Dimensión de las características de entrada.
        :param lr: Tasa de aprendizaje.
        :param epochs: Número de épocas de entrenamiento.
        """
        self.n_filas = n_filas
        self.n_columnas = n_columnas
        self.lr = lr
        self.epochs = epochs
        self.mapa = np.random.rand(n_filas, n_columnas, n_features)
        # Inicializamos el mapa con valores aleatorios.

    def entrenar(self, X):
        """
        Entrena el mapa de Kohonen con los datos de entrada.

        :param X: Datos de entrada.
        """
        for epoch in range(self.epochs):
            for x in X:
                # Calcular distancias de cada nodo
                distancias = np.linalg.norm(self.mapa - x, axis=2)
                # Calculamos la distancia euclidiana entre el vector de entrada y cada nodo del mapa.

                ganador = np.unravel_index(np.argmin(distancias), distancias.shape)
                # Identificamos el nodo ganador (el más cercano al vector de entrada).

                # Actualizar el nodo ganador y sus vecinos
                for i in range(self.n_filas):
                    for j in range(self.n_columnas):
                        distancia_vecino = np.linalg.norm(np.array([i, j]) - np.array(ganador))
                        # Calculamos la distancia entre el nodo actual y el nodo ganador.

                        if distancia_vecino < 2:
                            # Si el nodo está dentro del vecindario, actualizamos su peso.
                            self.mapa[i, j] += self.lr * (x - self.mapa[i, j])

    def visualizar_mapa(self):
        """
        Visualiza el mapa de Kohonen.
        """
        plt.imshow(np.mean(self.mapa, axis=2), cmap='coolwarm')
        # Mostramos el mapa promediando las características de cada nodo.

        plt.colorbar()
        plt.title("Mapa Autoorganizado de Kohonen")
        plt.show()
        # Mostramos la gráfica del mapa.

# Crear y entrenar el mapa de Kohonen
kohonen = MapaKohonen(10, 10, X.shape[1], epochs=100)
# Creamos un mapa de Kohonen de 10x10 nodos con las características de los datos generados.

kohonen.entrenar(X)
# Entrenamos el mapa con los datos generados.

# Visualizar el mapa
kohonen.visualizar_mapa()
# Visualizamos el mapa autoorganizado.