import numpy as np
# Importamos NumPy para realizar cálculos matriciales y operaciones con vectores.

# Función de activación sigmoide y su derivada
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
# La función sigmoide transforma cualquier valor en un rango entre 0 y 1.

def sigmoid_deriv(x):
    return x * (1 - x)
# La derivada de la sigmoide se utiliza para calcular los ajustes durante la retropropagación.

# Red Neuronal con Retropropagación
class RedNeuronal:
    def __init__(self, entradas, salidas, tasa_aprendizaje=0.1, epocas=10000):
        """
        Inicializa la red neuronal con los datos de entrada, salida y parámetros de entrenamiento.

        :param entradas: Matriz de entradas.
        :param salidas: Vector de salidas esperadas.
        :param tasa_aprendizaje: Tasa de aprendizaje para ajustar los pesos.
        :param epocas: Número de iteraciones para el entrenamiento.
        """
        self.entradas = entradas
        self.salidas = salidas
        self.tasa_aprendizaje = tasa_aprendizaje
        self.epocas = epocas
        self.pesos1 = np.random.rand(self.entradas.shape[1], 4)  # Capa oculta (4 neuronas)
        self.pesos2 = np.random.rand(4, 1)  # Capa de salida (1 neurona)
        self.bias1 = np.random.rand(4)
        self.bias2 = np.random.rand(1)
        # Inicializamos los pesos y bias con valores aleatorios.

    def entrenar(self):
        """
        Entrena la red neuronal ajustando los pesos y bias mediante retropropagación.
        """
        for epoch in range(self.epocas):
            # Propagación hacia adelante
            capa_oculta = sigmoid(np.dot(self.entradas, self.pesos1) + self.bias1)
            salida_pred = sigmoid(np.dot(capa_oculta, self.pesos2) + self.bias2)
            # Calculamos las salidas de la capa oculta y la capa de salida.

            # Error
            error = self.salidas - salida_pred
            # Calculamos el error entre la salida esperada y la predicha.

            # Retropropagación
            d_error = error * sigmoid_deriv(salida_pred)
            d_capa_oculta = d_error.dot(self.pesos2.T) * sigmoid_deriv(capa_oculta)
            # Calculamos los gradientes para ajustar los pesos y bias.

            # Ajuste de pesos
            self.pesos2 += capa_oculta.T.dot(d_error) * self.tasa_aprendizaje
            self.pesos1 += self.entradas.T.dot(d_capa_oculta) * self.tasa_aprendizaje
            self.bias2 += np.sum(d_error, axis=0) * self.tasa_aprendizaje
            self.bias1 += np.sum(d_capa_oculta, axis=0) * self.tasa_aprendizaje
            # Actualizamos los pesos y bias utilizando los gradientes calculados.

    def predecir(self, entradas):
        """
        Realiza una predicción para las entradas dadas.

        :param entradas: Matriz de entradas.
        :return: Salidas predichas.
        """
        capa_oculta = sigmoid(np.dot(entradas, self.pesos1) + self.bias1)
        salida_pred = sigmoid(np.dot(capa_oculta, self.pesos2) + self.bias2)
        # Calculamos las salidas de la red neuronal.
        return salida_pred

# Datos de entrenamiento (función XOR)
entradas = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
# Definimos las entradas para la operación lógica XOR.

salidas = np.array([[0], [1], [1], [0]])
# Definimos las salidas esperadas para la operación lógica XOR.

# Crear y entrenar la red neuronal
red_neuronal = RedNeuronal(entradas, salidas)
# Creamos una instancia de la red neuronal con las entradas y salidas.

red_neuronal.entrenar()
# Entrenamos la red neuronal.

# Predicciones después de entrenamiento
predicciones = red_neuronal.predecir(entradas)
# Calculamos las predicciones para las entradas después del entrenamiento.

print("Predicciones después de entrenamiento:")
print(predicciones)
# Mostramos las predicciones finales.