# Árbol de regresión M5 (simplificado)
from sklearn.tree import DecisionTreeRegressor
import numpy as np

# Generamos datos de ejemplo
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([1.5, 1.7, 1.9, 2.1, 2.3])

# Creamos el modelo de árbol de decisión para regresión
modelo = DecisionTreeRegressor()

# Entrenamos el modelo
modelo.fit(X, y)

# Predecimos nuevos valores
predicciones = modelo.predict([[6], [7]])
print("Predicciones:", predicciones)
