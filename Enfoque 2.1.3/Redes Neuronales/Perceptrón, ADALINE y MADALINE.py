import numpy as np

# Función de activación (sigmoide)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Perceptrón
class Perceptron:
    def __init__(self, entradas, salidas, tasa_aprendizaje=0.1, epocas=1000):
        self.entradas = entradas
        self.salidas = salidas
        self.tasa_aprendizaje = tasa_aprendizaje
        self.epocas = epocas
        self.pesos = np.random.rand(self.entradas.shape[1], 1)
        self.bias = np.random.rand(1)

    def entrenar(self):
        for _ in range(self.epocas):
            salida_pred = self.predecir(self.entradas)
            error = self.salidas - salida_pred
            ajuste = self.tasa_aprendizaje * np.dot(self.entradas.T, error * salida_pred * (1 - salida_pred))
            self.pesos += ajuste
            self.bias += self.tasa_aprendizaje * np.sum(error)

    def predecir(self, entradas):
        return sigmoid(np.dot(entradas, self.pesos) + self.bias)

# Datos de entrenamiento (función AND)
entradas = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
salidas = np.array([[0], [0], [0], [1]])

# Crear y entrenar el perceptrón
perceptron = Perceptron(entradas, salidas)
perceptron.entrenar()

# Resultados
predicciones = perceptron.predecir(entradas)
print("Predicciones después de entrenamiento:")
print(predicciones)
