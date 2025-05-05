# En un modelo de aprendizaje supervisado, la mejor hipótesis es el modelo que minimiza el error de predicción.
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
import numpy as np

# Generamos un dataset de ejemplo
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([1.5, 1.7, 1.9, 2.1, 2.3])

# Creamos y entrenamos un modelo de regresión
modelo = LinearRegression()
modelo.fit(X, y)

# Predecimos
predicciones = modelo.predict(X)

# Calculamos el error cuadrático medio (MSE)
mse = mean_squared_error(y, predicciones)
print("Mejor hipótesis actual (MSE):", mse)
