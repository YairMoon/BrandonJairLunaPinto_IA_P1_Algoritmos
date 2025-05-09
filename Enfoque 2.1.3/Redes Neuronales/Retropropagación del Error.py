import numpy as np

# Función de activación sigmoide y su derivada
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_deriv(x):
    return x * (1 - x)

# Red Neuronal con Retropropagación
class RedNeuronal:
    def __init__(self, entradas, salidas, tasa_aprendizaje=0.1, epocas=10000):
        self.entradas = entradas
        self.salidas = salidas
        self.tasa_aprendizaje = tasa_aprendizaje
        self.epocas = epocas
        self.pesos1 = np.random.rand(self.entradas.shape[1], 4)  # Capa oculta (4 neuronas)
        self.pesos2 = np.random.rand(4, 1)  # Capa de salida (1 neurona)
        self.bias1 = np.random.rand(4)
        self.bias2 = np.random.rand(1)

    def entrenar(self):
        for epoch in range(self.epocas):
            # Propagación hacia adelante
            capa_oculta = sigmoid(np.dot(self.entradas, self.pesos1) + self.bias1)
            salida_pred = sigmoid(np.dot(capa_oculta, self.pesos2) + self.bias2)

            # Error
            error = self.salidas - salida_pred

            # Retropropagación
            d_error = error * sigmoid_deriv(salida_pred)
            d_capa_oculta = d_error.dot(self.pesos2.T) * sigmoid_deriv(capa_oculta)

            # Ajuste de pesos
            self.pesos2 += capa_oculta.T.dot(d_error) * self.tasa_aprendizaje
            self.pesos1 += self.entradas.T.dot(d_capa_oculta) * self.tasa_aprendizaje
            self.bias2 += np.sum(d_error, axis=0) * self.tasa_aprendizaje
            self.bias1 += np.sum(d_capa_oculta, axis=0) * self.tasa_aprendizaje

    def predecir(self, entradas):
        # Propagación hacia adelante para hacer predicciones
        capa_oculta = sigmoid(np.dot(entradas, self.pesos1) + self.bias1)
        salida_pred = sigmoid(np.dot(capa_oculta, self.pesos2) + self.bias2)
        return salida_pred

# Datos de entrenamiento (función XOR)
entradas = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
salidas = np.array([[0], [1], [1], [0]])

# Crear e entrenar la red neuronal
red_neuronal = RedNeuronal(entradas, salidas)
red_neuronal.entrenar()

# Predicciones después de entrenamiento
predicciones = red_neuronal.predecir(entradas)
print("Predicciones después de entrenamiento:")
print(predicciones)
