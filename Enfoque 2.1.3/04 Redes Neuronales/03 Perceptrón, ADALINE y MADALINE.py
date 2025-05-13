import numpy as np
# Importamos NumPy para realizar cálculos matriciales y operaciones con vectores.

# Función de activación (sigmoide)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
# La función sigmoide transforma cualquier valor en un rango entre 0 y 1.

# Perceptrón
class Perceptron:
    def __init__(self, entradas, salidas, tasa_aprendizaje=0.1, epocas=1000):
        """
        Inicializa el perceptrón con los datos de entrada, salida y parámetros de entrenamiento.

        :param entradas: Matriz de entradas.
        :param salidas: Vector de salidas esperadas.
        :param tasa_aprendizaje: Tasa de aprendizaje para ajustar los pesos.
        :param epocas: Número de iteraciones para el entrenamiento.
        """
        self.entradas = entradas
        self.salidas = salidas
        self.tasa_aprendizaje = tasa_aprendizaje
        self.epocas = epocas
        self.pesos = np.random.rand(self.entradas.shape[1], 1)
        # Inicializamos los pesos con valores aleatorios.

        self.bias = np.random.rand(1)
        # Inicializamos el bias con un valor aleatorio.

    def entrenar(self):
        """
        Entrena el perceptrón ajustando los pesos y el bias.
        """
        for _ in range(self.epocas):
            salida_pred = self.predecir(self.entradas)
            # Calculamos la salida predicha para las entradas actuales.

            error = self.salidas - salida_pred
            # Calculamos el error entre la salida esperada y la predicha.

            ajuste = self.tasa_aprendizaje * np.dot(self.entradas.T, error * salida_pred * (1 - salida_pred))
            # Calculamos el ajuste para los pesos utilizando la regla de aprendizaje.

            self.pesos += ajuste
            # Actualizamos los pesos.

            self.bias += self.tasa_aprendizaje * np.sum(error)
            # Actualizamos el bias.

    def predecir(self, entradas):
        """
        Realiza una predicción para las entradas dadas.

        :param entradas: Matriz de entradas.
        :return: Salidas predichas.
        """
        return sigmoid(np.dot(entradas, self.pesos) + self.bias)
        # Calculamos la salida aplicando la función sigmoide.

# Datos de entrenamiento (función AND)
entradas = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
# Definimos las entradas para la operación lógica AND.

salidas = np.array([[0], [0], [0], [1]])
# Definimos las salidas esperadas para la operación lógica AND.

# Crear y entrenar el perceptrón
perceptron = Perceptron(entradas, salidas)
# Creamos una instancia del perceptrón con las entradas y salidas.

perceptron.entrenar()
# Entrenamos el perceptrón.

# Resultados
predicciones = perceptron.predecir(entradas)
# Calculamos las predicciones para las entradas después del entrenamiento.

print("Predicciones después de entrenamiento:")
print(predicciones)
# Mostramos las predicciones finales.